# 에이전트 기본 클래스
import json
import re
from typing import List
from agentic_framework.providers.bedrock_client import BedrockClient
from agentic_framework.tools.tool import BaseTool


class Agent:
    """
    가장 기본적인 Agent
    질의와 툴 목록을 받아서 사용자 질의에 대해 필요한 작업을 판단해서 처리한다.
    """

    def __init__(
        self,
        user_query: str,
        tools: List[BaseTool] = [],
        system_prompt: str = "",
        llm_client=None,
    ):
        self.user_query = user_query
        self.tools = tools
        self.system_prompt = system_prompt

        # llm 클라이언트 초기화
        if llm_client is None:
            self.llm_client = BedrockClient()
        else:
            self.llm_client = llm_client

    # 실행을 담당하는 run 함수 구현
    # tool list가 비어있으면
    def run(self) -> str:
        if not self.tools:
            return self._run_without_tools()
        else:
            return self._run_with_tools()

    def _run_without_tools(self) -> str:
        """
        단순 질의응답 패턴을 구현하는 run 함수
        """
        try:
            response = self.llm_client.invoke_model(self.user_query, self.system_prompt)
            return response
        except Exception as e:
            return f"오류: {e}"

    def _run_with_tools(self) -> str:
        """
        도구 목록이 같이 제공되었을 때, ReAct 패턴을 활용해서 Loop를 돌면서 질의를 처리하는 함수
        """
        # ReAct 패턴을 위한 프롬프트 템플릿
        react_prompt_template = """
당신은 질문에 대한 답변을 찾기 위해 '생각'하고, '도구'를 사용하는 AI 어시스턴트입니다.

당신은 매 단계마다 다음 두 가지 중 하나의 행동을 선택해야 합니다.

1. **도구 사용**: 문제 해결을 위해 도구가 필요하다고 판단될 때.
   - 먼저 `Thought:`에 도구를 사용하는 이유를 설명합니다.
   - 그 다음 `Action:`에 사용할 도구와 입력값을 JSON 형식으로 지정합니다.

2. **최종 답변**: 사용자에게 전달할 최종 답변을 찾았다고 확신할 때.
   - 먼저 `Thought:`에 최종 답변을 하는 이유를 설명합니다.
   - 그 다음 `Final Answer:`에 사용자에게 보여줄 최종 답변을 작성합니다.

---

**사용 가능한 도구:**
{tools_string}

---

**응답 형식:**

**옵션 1: 도구 사용**
Thought: [여기에 도구를 사용하려는 이유와 계획을 서술합니다.]
Action:
```json
{{
  "tool_name": "[사용할 도구의 이름]",
  "tool_input": "[도구에 전달할 입력값]"
}}
```

**옵션 2: 최종 답변**
Thought: [여기에 최종 답변을 하려는 이유를 서술합니다.]
Final Answer: [사용자에게 전달할 최종 답변입니다.]

---

**작업 흐름 예시:**

사용자 질문: 지금 몇 시야?
Thought: 사용자가 현재 시간을 물어보고 있으므로, 'current_time' 도구를 사용해야 합니다. 입력값은 필요 없습니다.
Action:
```json
{{
  "tool_name": "current_time",
  "tool_input": {{}}
}}
```
Observation: 2025년 10월 2일 10시 30분
Thought: 'current_time' 도구를 통해 현재 시간을 확인했습니다. 이제 이 정보를 바탕으로 최종 답변을 할 수 있습니다.
Final Answer: 현재 시간은 2025년 10월 2일 10시 30분입니다.

---

이제 시작하겠습니다. 이전 대화 내용과 도구 실행 결과(Observation)가 있다면 아래에 표시됩니다.

사용자 질문: {user_query}
"""

        # 1. 초기 설정
        max_loops = 5
        intermediate_steps = ""
        tools_string = "\n".join(
            [f"- {tool.name}: {tool.description}" for tool in self.tools]
        )
        tool_map = {tool.name: tool for tool in self.tools}

        prompt = react_prompt_template.format(
            tools_string=tools_string,
            user_query=self.user_query,
        )

        # 2. ReAct 루프 실행
        for i in range(max_loops):
            print(f"--- Iteration {i+1} ---")

            # LLM 호출
            llm_response = self.llm_client.invoke_model(prompt + intermediate_steps)
            print(llm_response)

            # 3. 최종 답변 확인
            if "Final Answer:" in llm_response:
                final_answer = llm_response.split("Final Answer:")[-1].strip()
                return final_answer

            # 4. Action 파싱 및 도구 실행
            action_match = re.search(
                r"Action:\s*```json\s*({.*?})\s*```", llm_response, re.DOTALL
            )
            if action_match:
                try:
                    action_json = action_match.group(1)
                    action_data = json.loads(action_json)  # JSON 파싱
                    tool_name = action_data["tool_name"]
                    tool_input = action_data["tool_input"]

                    if tool_name in tool_map:
                        print(f"도구 호출: {tool_name} with input {tool_input}")
                        tool_to_use = tool_map[tool_name]
                        observation = tool_to_use.run(tool_input)
                        print(f"도구 호출 결과: {observation}")
                    else:
                        observation = (
                            f"오류: '{tool_name}'이라는 도구를 찾을 수 없습니다."
                        )

                except Exception as e:
                    observation = f"오류: Action 파싱 또는 도구 실행 중 오류 발생 - {e}"

                intermediate_steps += f"\n{llm_response}\nObservation: {observation}"
            else:
                # Action을 찾지 못하면 루프를 중단하고 현재까지의 응답을 반환
                return "오류: LLM이 유효한 Action을 생성하지 못했습니다."

        return "오류: 최대 반복 횟수를 초과했습니다. 최종 답변을 찾지 못했습니다."
