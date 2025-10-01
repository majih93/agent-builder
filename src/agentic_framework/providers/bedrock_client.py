# Default로 사용되는 AWS Bedrock 클라이언트
import json
import boto3
from pydantic import BaseModel
from pydantic import Field
from decimal import Decimal
from typing import Annotated, Dict, Any


DEFAULT_MODEL_ID = "us.anthropic.claude-sonnet-4-20250514-v1:0"


class BedrockParams(BaseModel):
    """
    Bedrock Client 호출 시 사용되는 기본 Parameter 정의
    """

    temperature: Annotated[
        Decimal,
        Field(
            gt=0,
            lt=1,
            description="Controls the randomness of the output. Higher values produce more random results.",
        ),
    ] = Decimal("0.7")
    max_tokens: int = Field(
        default=2048,
        gt=1,
        description="Maximum number of tokens to generate in the response.",
    )


class BedrockClient:
    """
    AWS Bedrock에서 LLM 모델을 호출하는 클라이언트
    Boto3를 사용해서 AWS 환경 설정을 가져오도록 구현됨
    """

    def __init__(
        self, model_id: str = DEFAULT_MODEL_ID, params: BedrockParams = BedrockParams()
    ):
        # init 시에 필요한 속성 저장
        self.model_id = model_id
        self.params = params

        # boto3 client 초기화
        try:
            self.client = boto3.client("bedrock-runtime")
        except Exception as e:
            raise ConnectionError(
                f"AWS Bedrock 클라이언트 초기화 실패. AWS 인증/설정을 확인하세요: {e}"
            )

    def invoke_model(self, query: str, system_prompt: str) -> str:
        """
        주어진 프롬프트 사용하여 Bedrock 모델 호출 후 텍스트 응답 반환
        """
        call_params = self.params.model_dump()

        # 입력한 질의가 없으면 에러 발생
        if not query:
            raise ValueError("Query cannot be empty.")

        # 메시지 바디 구성
        message_body = {
            "anthropic_version": "bedrock-2023-05-31",
            "messages": [
                {"role": "user", "content": query},
            ],
            **call_params,
        }

        if system_prompt:
            message_body["system"] = system_prompt

        # 모델 호출
        try:
            # Decimal 타입을 float으로 변환하는 헬퍼 함수
            def decimal_default(obj):
                if isinstance(obj, Decimal):
                    return float(obj)
                raise TypeError

            response = self.client.invoke_model(
                modelId=self.model_id,
                body=json.dumps(message_body, default=decimal_default).encode("utf-8"),
                contentType="application/json",
            )
            # 응답 파싱 및 반환
            response_body = json.loads(response["body"].read())
            return response_body["content"][0]["text"]
        except Exception as e:
            print(f"Bedrock 모델 호출 실패: {e}")
            return "오류: 모델 호출 실패"
