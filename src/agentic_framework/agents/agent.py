# 에이전트 기본 클래스
from typing import List
from agentic_framework.providers.bedrock_client import BedrockClient
from agentic_framework.tools.tool import Tool


class Agent:
    """
    가장 기본적인 Agent
    질의와 툴 목록을 받아서 사용자 질의에 대해 필요한 작업을 판단해서 처리한다.
    """

    def __init__(
        self,
        user_query: str,
        tools: List[Tool],
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
    def run(self) -> str:
        try:
            response = self.llm_client.invoke_model(self.user_query, self.system_prompt)
            return response
        except Exception as e:
            return f"오류: {e}"
