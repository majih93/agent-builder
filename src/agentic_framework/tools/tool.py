from abc import ABC, abstractmethod
from typing import Dict, Any, Type
from pydantic import BaseModel


class BaseTool(ABC):
    """모든 Tool이 상속받아야 하는 기본 인터페이스"""

    # Tool의 이름 (LLM이 호출할 때 사용)
    name: str = "base_tool"
    # Tool에 대한 설명 (LLM이 언제 사용할지 판단하는 기준)
    description: str = "실제 tool을 정의하기 위한 기본 Tool 클래스"
    # Tool의 입력 구조를 정의하는 Pydantic 모델
    # BaseModel을 상속받은 클래스 타입의 데이터로 추후 구현 시 지정하도록 하는 것.
    args_schema: Type[BaseModel] = BaseModel

    @abstractmethod
    def _run(self, *args: Any, **kwargs: Any) -> Dict[str, Any]:
        """
        Tool의 실제 로직을 구현하는 메소드.
        자식 클래스에서 반드시 구현해야 합니다.
        """
        pass

    def run(self, tool_input: Dict[str, Any]) -> Dict[str, Any]:
        """
        Agent가 Tool을 호출할 때 사용하는 표준 메소드.
        입력 유효성 검사 및 에러 처리를 담당합니다.
        """
        try:
            # args_schema가 있고, 기본 BaseModel이 아닌 경우에만 파싱을 시도합니다.
            # 그냥 통으로 **tool_input으로 처리하면 빈 객체인 경우에 NoneType object is not callable 에러 발생함.
            if self.args_schema and self.args_schema is not BaseModel:
                parsed_args = self.args_schema(**tool_input)
                result = self._run(**parsed_args.model_dump())
            else:
                # args_schema가 없거나 기본 BaseModel이면 인자 없이 _run을 호출합니다.
                result = self._run()

            return {"status": "success", "result": result}
        except Exception as e:
            # 에러 발생 시 표준화된 형식으로 반환
            return {"status": "error", "message": str(e)}
