# Implementation Plan

## Phase 1: 기본 인프라 구축

- [x] 1. Python 프로젝트 기본 구조 설정

  **목적**: 확장 가능하고 유지보수가 용이한 Python 프로젝트 구조를 설정하여 개발 효율성과 코드 품질을 보장

  **왜 필요한가**: 체계적인 프로젝트 구조 없이는 코드가 복잡해질수록 관리가 어려워지고, 테스트와 배포가 복잡해짐. 초기에 올바른 구조를 잡아야 향후 확장과 유지보수가 용이함

  **프로그래밍 관점에서의 의미**:

  - **Separation of Concerns**: 소스 코드, 테스트, 설정, 문서를 명확히 분리하여 각각의 책임을 명확히 함
  - **Package Structure**: Python의 패키지 시스템을 활용하여 모듈 간 의존성을 체계적으로 관리
  - **Build System**: pyproject.toml을 통한 현대적인 Python 빌드 시스템 활용으로 의존성 관리 표준화
  - **Testing Strategy**: 테스트 코드를 별도 디렉토리로 분리하여 프로덕션 코드와 테스트 코드의 명확한 구분
  - **Documentation as Code**: 예제와 문서를 코드와 함께 관리하여 일관성 유지

  **상세 폴더 구조**:

  ```
  agentic-framework/
  ├── pyproject.toml              # 프로젝트 메타데이터 및 빌드 설정
  ├── requirements.txt            # 의존성 목록 (개발용)
  ├── requirements-dev.txt        # 개발 전용 의존성 (pytest, black, mypy 등)
  ├── README.md                   # 프로젝트 개요 및 사용법
  ├── .gitignore                  # Git 무시 파일 목록
  ├── .env.example               # 환경변수 템플릿
  ├── Makefile                   # 개발 작업 자동화 스크립트
  │
  ├── src/                       # 소스 코드 루트
  │   └── agentic_framework/     # 메인 패키지
  │       ├── __init__.py        # 패키지 초기화 및 공개 API
  │       ├── types/             # 데이터 타입 및 모델 정의
  │       │   ├── __init__.py
  │       │   ├── messages.py    # 메시지 관련 타입
  │       │   ├── tools.py       # 도구 관련 타입
  │       │   ├── errors.py      # 에러 및 예외 타입
  │       │   └── config.py      # 설정 관련 타입
  │       │
  │       ├── core/              # 핵심 에이전트 시스템
  │       │   ├── __init__.py
  │       │   ├── agent.py       # 기본 에이전트 클래스
  │       │   ├── messaging.py   # 메시지 처리 시스템
  │       │   ├── context.py     # 실행 컨텍스트 관리
  │       │   ├── tool_integration.py  # 도구 통합 로직
  │       │   ├── tool_results.py      # 도구 결과 처리
  │       │   └── tool_error_handling.py # 도구 에러 처리
  │       │
  │       ├── tools/             # 도구 시스템
  │       │   ├── __init__.py
  │       │   ├── base.py        # 도구 추상 클래스
  │       │   ├── results.py     # 도구 실행 결과
  │       │   ├── error_handling.py # 도구 에러 처리
  │       │   ├── registry.py    # 도구 레지스트리
  │       │   ├── manager.py     # 도구 매니저
  │       │   ├── security.py    # 도구 보안 관리
  │       │   └── builtin/       # 내장 도구들
  │       │       ├── __init__.py
  │       │       ├── calculator.py    # 계산기 도구
  │       │       └── text_processor.py # 텍스트 처리 도구
  │       │
  │       ├── llm/               # LLM 연동 시스템
  │       │   ├── __init__.py
  │       │   ├── base.py        # LLM 제공자 추상 클래스
  │       │   ├── prompts.py     # 프롬프트 관리
  │       │   ├── config.py      # LLM 설정 관리
  │       │   └── providers/     # LLM 제공자 구현체
  │       │       ├── __init__.py
  │       │       ├── mock.py           # Mock LLM 제공자
  │       │       ├── mock_scenarios.py # Mock 시나리오
  │       │       ├── mock_config.py    # Mock 설정
  │       │       ├── openai.py         # OpenAI 연동
  │       │       ├── openai_auth.py    # OpenAI 인증
  │       │       └── openai_retry.py   # OpenAI 재시도 로직
  │       │
  │       ├── agents/            # 구체적인 에이전트 구현
  │       │   ├── __init__.py
  │       │   ├── llm_agent.py   # LLM 기반 에이전트
  │       │   ├── tool_decision.py # 도구 선택 로직
  │       │   └── execution_loop.py # 실행 루프
  │       │
  │       ├── memory/            # 메모리 및 컨텍스트 관리
  │       │   ├── __init__.py
  │       │   ├── in_memory_store.py # 인메모리 저장소
  │       │   ├── session_manager.py # 세션 관리
  │       │   ├── query.py           # 컨텍스트 조회
  │       │   ├── context_manager.py # 컨텍스트 매니저
  │       │   ├── size_manager.py    # 크기 제한 관리
  │       │   └── cleanup.py         # 자동 정리
  │       │
  │       ├── orchestration/     # 다중 에이전트 오케스트레이션
  │       │   ├── __init__.py
  │       │   ├── registry.py    # 에이전트 레지스트리
  │       │   ├── discovery.py   # 에이전트 검색
  │       │   ├── monitoring.py  # 상태 모니터링
  │       │   ├── scheduler.py   # 실행 스케줄러
  │       │   ├── messaging.py   # 메시지 전달
  │       │   └── result_collector.py # 결과 수집
  │       │
  │       ├── workflow/          # 워크플로우 시스템
  │       │   ├── __init__.py
  │       │   ├── definition.py  # 워크플로우 정의
  │       │   ├── agent_mapping.py # 에이전트 매핑
  │       │   ├── validation.py  # 워크플로우 검증
  │       │   ├── executor.py    # 실행 엔진
  │       │   ├── data_flow.py   # 데이터 흐름 관리
  │       │   └── error_handling.py # 에러 처리
  │       │
  │       ├── monitoring/        # 모니터링 및 메트릭
  │       │   ├── __init__.py
  │       │   ├── execution_tracker.py # 실행 추적
  │       │   ├── tool_metrics.py      # 도구 메트릭
  │       │   └── system_metrics.py    # 시스템 메트릭
  │       │
  │       ├── logging/           # 로깅 시스템
  │       │   ├── __init__.py
  │       │   ├── structured_logger.py # 구조화된 로깅
  │       │   ├── level_manager.py     # 로그 레벨 관리
  │       │   └── output_handlers.py   # 출력 핸들러
  │       │
  │       ├── config/            # 설정 관리
  │       │   ├── __init__.py
  │       │   ├── env_loader.py  # 환경변수 로더
  │       │   ├── file_loader.py # 설정 파일 로더
  │       │   └── validator.py   # 설정 검증
  │       │
  │       └── utils/             # 유틸리티 함수들
  │           ├── __init__.py
  │           ├── async_utils.py # 비동기 유틸리티
  │           ├── serialization.py # 직렬화 유틸리티
  │           └── validation.py  # 검증 유틸리티
  │
  ├── tests/                     # 테스트 코드
  │   ├── __init__.py
  │   ├── conftest.py           # pytest 설정 및 픽스처
  │   ├── unit/                 # 단위 테스트
  │   │   ├── __init__.py
  │   │   ├── types/            # 타입 테스트
  │   │   ├── core/             # 핵심 기능 테스트
  │   │   ├── tools/            # 도구 테스트
  │   │   ├── llm/              # LLM 테스트
  │   │   └── ...               # 각 모듈별 테스트
  │   │
  │   ├── integration/          # 통합 테스트
  │   │   ├── __init__.py
  │   │   ├── test_agent_tool_integration.py
  │   │   ├── test_multi_agent_workflow.py
  │   │   └── test_end_to_end.py
  │   │
  │   └── fixtures/             # 테스트 데이터 및 픽스처
  │       ├── __init__.py
  │       ├── sample_configs/   # 샘플 설정 파일
  │       ├── mock_responses/   # Mock 응답 데이터
  │       └── test_workflows/   # 테스트용 워크플로우
  │
  ├── examples/                 # 사용 예제
  │   ├── __init__.py
  │   ├── simple_chatbot.py     # 간단한 챗봇 예제
  │   ├── multi_agent_collaboration.py # 다중 에이전트 협업
  │   ├── automation_workflow.py       # 작업 자동화 예제
  │   ├── custom_tools/         # 커스텀 도구 예제
  │   └── configs/              # 예제용 설정 파일
  │
  ├── docs/                     # 문서
  │   ├── api/                  # API 문서
  │   ├── tutorials/            # 튜토리얼
  │   ├── architecture.md       # 아키텍처 문서
  │   └── deployment.md         # 배포 가이드
  │
  └── scripts/                  # 개발 및 배포 스크립트
      ├── setup_dev.py         # 개발 환경 설정
      ├── run_tests.py         # 테스트 실행
      ├── build.py             # 빌드 스크립트
      └── deploy.py            # 배포 스크립트
  ```

  **폴더 구조 설계 원칙**:

  - **Domain-Driven Structure**: 비즈니스 도메인(agents, tools, workflow)별로 모듈 분리
  - **Layered Architecture**: types(도메인) → core(애플리케이션) → infrastructure(외부 연동) 계층 구조
  - **Test Mirroring**: 소스 코드 구조와 동일한 테스트 구조로 일관성 유지
  - **Configuration Separation**: 환경별 설정을 별도 관리하여 배포 유연성 확보
  - **Documentation Co-location**: 코드와 문서를 함께 관리하여 동기화 유지

  **세부 작업**:

  - Python 프로젝트 초기화 (pyproject.toml, requirements.txt)
  - 테스트 환경 설정 (pytest, coverage, mypy)
  - 위 폴더 구조에 따른 디렉토리 생성 및 **init**.py 파일 생성
  - 가상환경 설정 및 기본 의존성 설치
  - 개발 도구 설정 (black, isort, pre-commit hooks)
  - _Requirements: 모든 요구사항의 기반_

- [ ] 2. 핵심 데이터 클래스 및 타입 정의

  **목적**: 프레임워크 전체에서 사용할 표준화된 데이터 구조를 정의하여 컴포넌트 간 일관된 데이터 교환을 가능하게 함

  **왜 필요한가**: 에이전트 간 통신, 도구 호출 결과, 컨텍스트 관리 등 모든 기능이 의존하는 기본 데이터 타입들을 먼저 정의해야 이후 구현이 일관성 있게 진행됨

  **프로그래밍 관점에서의 의미**:

  - **Domain-Driven Design (DDD)**: 비즈니스 도메인의 핵심 개념들을 코드로 명확히 표현하여 도메인 전문가와 개발자 간 공통 언어 구축
  - **Type Safety**: 정적 타입 시스템을 활용하여 컴파일 타임에 오류를 발견하고 IDE의 자동완성 및 리팩토링 지원 향상
  - **Contract-First Design**: 인터페이스를 먼저 정의함으로써 컴포넌트 간 의존성을 명확히 하고 병렬 개발 가능
  - **Immutability**: 데이터 클래스를 불변으로 설계하여 동시성 문제를 방지하고 예측 가능한 동작 보장
  - **Single Source of Truth**: 데이터 구조를 한 곳에서 정의하여 중복을 제거하고 변경 시 일관성 유지

  **세부 작업**:

  - [ ] 2.1 메시지 및 통신 데이터 클래스 생성

    - `Message` 클래스: 에이전트 간 통신을 위한 기본 메시지 구조 (발신자, 수신자, 내용, 타임스탬프, 우선순위)
    - `AgentRequest`/`AgentResponse` 클래스: 에이전트 실행 요청과 응답을 위한 표준 구조
    - `ConversationContext` 클래스: 대화 맥락 정보를 담는 구조 (세션 ID, 사용자 정보, 대화 기록 참조)
    - 파일 위치: `src/agentic_framework/types/messages.py`
    - _Requirements: 1.1 (에이전트 통신), 3.1 (컨텍스트 관리)_

    **학습 포인트**:

    - **Value Object Pattern**: 메시지는 식별자가 아닌 값으로 구분되는 불변 객체로 설계
    - **Message Envelope Pattern**: 메타데이터(발신자, 타임스탬프)와 페이로드(내용)를 분리하여 라우팅과 처리 로직 분리

  - [ ] 2.2 도구 관련 데이터 클래스 생성

    - `ToolCall` 클래스: 도구 호출 정보 (도구명, 파라미터, 호출 ID)
    - `ToolResult` 클래스: 도구 실행 결과 (성공/실패, 결과 데이터, 에러 정보, 실행 시간)
    - `ToolMetadata` 클래스: 도구 메타정보 (이름, 설명, 파라미터 스키마, 권한 요구사항)
    - 파일 위치: `src/agentic_framework/types/tools.py`
    - _Requirements: 2.1 (도구 인터페이스), 2.2 (도구 통합)_

  - [ ] 2.3 에러 및 결과 타입 정의

    - `AgentError` 기본 예외 클래스와 하위 예외들 (ToolError, LLMError, ConfigError)
    - `ExecutionResult` 제네릭 클래스: 성공/실패 상태와 결과 데이터를 담는 Result 타입
    - `ErrorSeverity` Enum: 에러 심각도 분류 (INFO, WARNING, ERROR, CRITICAL)
    - 파일 위치: `src/agentic_framework/types/errors.py`
    - _Requirements: 모든 요구사항 (에러 처리는 모든 기능에 필요)_

  - [ ] 2.4 설정 및 옵션 클래스 정의
    - `AgentConfig` 클래스: 에이전트 설정 (이름, 역할, LLM 설정, 도구 목록)
    - `FrameworkConfig` 클래스: 전체 프레임워크 설정 (로깅 레벨, 메모리 제한, 재시도 정책)
    - `LLMConfig` 클래스: LLM 제공자별 설정 (API 키, 모델명, 온도, 최대 토큰)
    - Pydantic을 사용하여 설정 검증 및 환경변수 자동 로딩 구현
    - 파일 위치: `src/agentic_framework/types/config.py`
    - _Requirements: 4.1 (LLM 추상화), 7.1 (설정 관리)_

## Phase 2: 단순한 에이전트 실행 시스템

- [ ] 3. 기본 에이전트 클래스 구현

  **목적**: 단일 에이전트의 생명주기 관리와 기본 실행 로직을 구현하여 에이전트 시스템의 핵심 기반을 마련

  **왜 필요한가**: 복잡한 다중 에이전트 시스템을 구축하기 전에 단일 에이전트가 안정적으로 동작하는 것을 먼저 확보해야 함. 상태 관리와 메시지 처리는 모든 에이전트 기능의 기반이 됨

  **프로그래밍 관점에서의 의미**:

  - **State Pattern**: 에이전트의 다양한 상태(IDLE, RUNNING, COMPLETED 등)를 명시적으로 모델링하여 상태별 행동을 캡슐화
  - **Template Method Pattern**: BaseAgent에서 공통 실행 흐름을 정의하고 구체적인 에이전트에서 세부 구현을 오버라이드
  - **Observer Pattern**: 상태 변경 이벤트를 통해 느슨한 결합으로 모니터링 및 로깅 시스템 연동
  - **Single Responsibility Principle**: 에이전트 클래스는 오직 에이전트의 생명주기 관리에만 집중하고 다른 책임은 별도 클래스로 분리
  - **Async/Await Pattern**: 비동기 메시지 처리를 통해 블로킹 없는 반응형 시스템 구축

  **세부 작업**:

  - [ ] 3.1 기본 Agent 추상 클래스 구현

    - `BaseAgent` 추상 클래스: 모든 에이전트가 상속받을 기본 인터페이스
    - 에이전트 상태 관리: `AgentState` Enum (IDLE, RUNNING, COMPLETED, FAILED, PAUSED)
    - 상태 전환 로직과 상태 변경 이벤트 콜백 시스템
    - 파일 위치: `src/agentic_framework/core/agent.py`
    - _Requirements: 1.1 (에이전트 정의), 1.2 (에이전트 관리)_

    **학습 포인트**:

    - **Finite State Machine**: 에이전트 상태를 명시적으로 모델링하여 예측 가능한 동작 보장
    - **Template Method + Hook Methods**: 공통 실행 흐름은 부모에서, 구체적 구현은 자식에서 담당하는 확장점 제공

  - [ ] 3.2 메시지 처리 메커니즘 구현

    - 에이전트 내부 메시지 큐 시스템 (asyncio.Queue 활용)
    - 메시지 우선순위 처리 및 타임아웃 관리
    - 메시지 처리 실패 시 재시도 및 데드레터 큐 구현
    - 파일 위치: `src/agentic_framework/core/messaging.py`
    - _Requirements: 1.1 (에이전트 통신), 1.2 (메시지 라우팅)_

  - [ ] 3.3 에이전트 실행 컨텍스트 관리
    - 실행 중인 에이전트의 컨텍스트 정보 추적 (시작 시간, 현재 작업, 리소스 사용량)
    - 에이전트별 로깅 컨텍스트 설정 (에이전트 ID, 세션 정보 자동 포함)
    - 실행 통계 수집 (처리한 메시지 수, 평균 응답 시간, 에러 발생률)
    - 파일 위치: `src/agentic_framework/core/context.py`
    - _Requirements: 6.1 (실행 추적), 6.2 (성능 메트릭)_

- [ ] 4. 기본 에이전트 실행 테스트 작성

  **목적**: 에이전트 핵심 기능의 정확성을 검증하고 회귀 방지를 위한 테스트 기반 구축

  **왜 필요한가**: 에이전트 시스템은 비동기적이고 상태 기반이므로 복잡한 버그가 발생하기 쉬움. 초기부터 견고한 테스트를 구축해야 안정적인 시스템 개발 가능

  **프로그래밍 관점에서의 의미**:

  - **Test-Driven Development (TDD)**: 구현 전에 테스트를 작성하여 요구사항을 명확히 하고 설계 품질 향상
  - **Arrange-Act-Assert Pattern**: 테스트 구조를 일관되게 유지하여 가독성과 유지보수성 향상
  - **Test Doubles (Mock, Stub, Fake)**: 외부 의존성을 격리하여 단위 테스트의 독립성과 실행 속도 보장
  - **Boundary Value Testing**: 상태 전환의 경계 조건을 테스트하여 edge case에서의 안정성 확보
  - **Async Testing Patterns**: 비동기 코드의 테스트 복잡성을 관리하고 race condition 등의 문제 사전 발견

  **세부 작업**:

  - [ ] 4.1 에이전트 생성 및 초기화 테스트

    - 다양한 설정으로 에이전트 생성 테스트
    - 잘못된 설정에 대한 에러 처리 테스트
    - 에이전트 ID 중복 방지 테스트
    - 파일 위치: `tests/core/test_agent_creation.py`
    - _Requirements: 1.1 (에이전트 정의)_

  - [ ] 4.2 상태 전환 및 생명주기 테스트

    - 정상적인 상태 전환 시나리오 테스트 (IDLE → RUNNING → COMPLETED)
    - 비정상적인 상태 전환 방지 테스트 (COMPLETED → RUNNING 등)
    - 에이전트 강제 종료 및 정리 테스트
    - 파일 위치: `tests/core/test_agent_lifecycle.py`
    - _Requirements: 1.2 (에이전트 관리)_

  - [ ] 4.3 메시지 처리 및 에러 핸들링 테스트
    - 메시지 큐 처리 순서 및 우선순위 테스트
    - 메시지 처리 중 예외 발생 시 복구 테스트
    - 타임아웃 및 재시도 로직 테스트
    - 파일 위치: `tests/core/test_message_handling.py`
    - _Requirements: 1.1 (메시지 처리), 에러 처리_

## Phase 3: 도구 시스템 기초

- [ ] 5. 기본 도구 추상 클래스 구현

  **목적**: 외부 서비스와의 통합을 위한 표준화된 도구 인터페이스를 구축하여 확장 가능한 도구 생태계 기반 마련

  **왜 필요한가**: 에이전트가 실제 작업을 수행하려면 외부 API, 데이터베이스, 파일 시스템 등과 상호작용해야 함. 표준화된 인터페이스 없이는 각 도구마다 다른 방식으로 구현되어 유지보수가 어려워짐

  **프로그래밍 관점에서의 의미**:

  - **Strategy Pattern**: 다양한 도구 구현체를 런타임에 교체 가능하게 하여 유연성 확보
  - **Interface Segregation Principle**: 도구별로 필요한 메서드만 노출하여 불필요한 의존성 제거
  - **Command Pattern**: 도구 실행을 객체로 캡슐화하여 실행 취소, 로깅, 큐잉 등의 기능 추가 가능
  - **Circuit Breaker Pattern**: 외부 서비스 장애 시 시스템 전체 장애를 방지하는 회복력 있는 설계
  - **Dependency Inversion Principle**: 고수준 모듈(에이전트)이 저수준 모듈(구체적 도구)에 의존하지 않도록 추상화 계층 도입

  **세부 작업**:

  - [ ] 5.1 Tool 추상 베이스 클래스 정의

    - `BaseTool` ABC 클래스: 모든 도구가 구현해야 할 인터페이스
    - `execute()` 추상 메서드: 도구 실행 로직
    - `validate_input()` 메서드: 입력 파라미터 검증
    - `get_schema()` 메서드: 도구 파라미터 스키마 반환
    - 파일 위치: `src/agentic_framework/tools/base.py`
    - _Requirements: 2.1 (도구 인터페이스)_

    **학습 포인트**:

    - **Fail Fast Principle**: validate_input()으로 잘못된 입력을 조기에 발견하여 시스템 안정성 향상
    - **Self-Documenting Code**: get_schema()로 도구가 스스로 사용법을 설명할 수 있는 자기 문서화 구조

  - [ ] 5.2 도구 실행 결과 처리 시스템

    - 성공/실패 상태와 결과 데이터를 포함하는 `ToolExecutionResult` 클래스
    - 실행 시간, 리소스 사용량 등 메타데이터 수집
    - 도구별 결과 직렬화/역직렬화 지원 (JSON, 바이너리 데이터 등)
    - 파일 위치: `src/agentic_framework/tools/results.py`
    - _Requirements: 2.1 (도구 결과 처리)_

  - [ ] 5.3 도구 에러 처리 및 재시도 메커니즘
    - 도구별 에러 분류 (일시적 vs 영구적 에러)
    - Exponential backoff를 적용한 재시도 로직
    - Circuit breaker 패턴으로 반복 실패하는 도구 격리
    - 파일 위치: `src/agentic_framework/tools/error_handling.py`
    - _Requirements: 2.3 (에러 처리), 2.4 (재시도 로직)_

- [ ] 6. 첫 번째 간단한 도구 구현

  **목적**: 도구 시스템의 실제 동작을 검증하고 개발자들이 참고할 수 있는 구체적인 구현 예제 제공

  **왜 필요한가**: 추상적인 인터페이스만으로는 실제 동작을 확인하기 어려움. 간단한 도구를 구현하여 전체 시스템이 올바르게 작동하는지 검증하고 향후 복잡한 도구 개발의 기반 마련

  **세부 작업**:

  - [ ] 6.1 계산기 도구 구현

    - 기본 수학 연산 (덧셈, 뺄셈, 곱셈, 나눗셈) 지원
    - 입력 검증 (숫자 타입 확인, 0으로 나누기 방지)
    - 연산 결과와 함께 계산 과정 로그 제공
    - 파일 위치: `src/agentic_framework/tools/builtin/calculator.py`
    - _Requirements: 2.1 (기본 도구), 2.2 (도구 통합)_

  - [ ] 6.2 텍스트 처리 도구 구현

    - 문자열 길이 계산, 대소문자 변환, 공백 제거 등 기본 기능
    - 정규표현식 기반 패턴 매칭 및 치환
    - 텍스트 인코딩 변환 및 유효성 검사
    - 파일 위치: `src/agentic_framework/tools/builtin/text_processor.py`
    - _Requirements: 2.1 (기본 도구), 2.2 (도구 통합)_

  - [ ] 6.3 도구 실행 및 결과 검증 테스트
    - 각 도구의 정상 동작 시나리오 테스트
    - 잘못된 입력에 대한 에러 처리 테스트
    - 도구 실행 시간 및 성능 측정 테스트
    - 파일 위치: `tests/tools/test_builtin_tools.py`
    - _Requirements: 2.1 (도구 검증)_

- [ ] 7. 도구 매니저 기본 구현

  **목적**: 여러 도구들을 중앙에서 관리하고 에이전트가 필요한 도구를 쉽게 찾아 사용할 수 있는 시스템 구축

  **왜 필요한가**: 에이전트가 여러 도구를 사용할 때 각각을 개별적으로 관리하면 복잡성이 증가함. 중앙화된 도구 관리 시스템으로 도구 등록, 검색, 실행을 통합 관리해야 함

  **프로그래밍 관점에서의 의미**:

  - **Registry Pattern**: 도구 인스턴스들을 중앙에서 관리하여 전역 접근점 제공하면서도 Singleton의 단점 회피
  - **Factory Pattern**: 도구 생성 로직을 캡슐화하여 클라이언트 코드와 구체적인 도구 클래스 간 결합도 감소
  - **Facade Pattern**: 복잡한 도구 관리 로직을 단순한 인터페이스로 감싸서 사용성 향상
  - **Resource Management**: 도구 실행 시 메모리, CPU, 네트워크 등 시스템 리소스의 효율적 관리
  - **Security by Design**: 도구 실행 권한을 체계적으로 관리하여 보안 취약점 사전 방지

  **세부 작업**:

  - [ ] 7.1 도구 레지스트리 시스템 구현

    - 도구 등록 및 해제 기능 (`register_tool()`, `unregister_tool()`)
    - 도구 이름 및 카테고리별 검색 기능
    - 도구 메타데이터 관리 (버전, 설명, 의존성 정보)
    - 파일 위치: `src/agentic_framework/tools/registry.py`
    - _Requirements: 2.1 (도구 관리), 2.2 (도구 검색)_

  - [ ] 7.2 도구 실행 중앙화 처리

    - `ToolManager` 클래스: 모든 도구 실행을 중앙에서 처리
    - 도구 실행 전후 로깅 및 메트릭 수집
    - 동시 실행 제한 및 리소스 관리 (세마포어 활용)
    - 파일 위치: `src/agentic_framework/tools/manager.py`
    - _Requirements: 2.2 (도구 실행), 2.3 (리소스 관리)_

  - [ ] 7.3 도구 권한 및 보안 관리
    - 도구별 실행 권한 설정 (읽기 전용, 쓰기 허용 등)
    - 민감한 도구에 대한 사용자 승인 요청 메커니즘
    - 도구 실행 로그 및 감사 추적 기능
    - 파일 위치: `src/agentic_framework/tools/security.py`
    - _Requirements: 2.4 (보안), 6.1 (감사 로그)_

## Phase 4: LLM 연동 기초

- [ ] 8. LLM 제공자 추상 클래스 구현

  **목적**: 다양한 LLM 제공자들의 API 차이를 추상화하여 에이전트가 제공자에 관계없이 일관된 방식으로 LLM을 사용할 수 있게 함

  **왜 필요한가**: OpenAI, Anthropic, Google 등 각 제공자마다 API 형식, 파라미터, 응답 구조가 다름. 에이전트 코드에서 이런 차이를 직접 처리하면 제공자 변경 시 대규모 코드 수정이 필요함

  **프로그래밍 관점에서의 의미**:

  - **Adapter Pattern**: 서로 다른 LLM API들을 공통 인터페이스로 통합하여 호환성 문제 해결
  - **Open/Closed Principle**: 새로운 LLM 제공자 추가 시 기존 코드 수정 없이 확장 가능한 구조
  - **Abstract Factory Pattern**: 제공자별로 관련된 객체들(클라이언트, 파서, 설정)을 일관되게 생성
  - **Cost Optimization**: API 호출 비용을 추상화 계층에서 추적하고 최적화하는 횡단 관심사 처리
  - **Vendor Lock-in 방지**: 특정 제공자에 종속되지 않는 설계로 비즈니스 유연성 확보

  **세부 작업**:

  - [ ] 8.1 LLM 제공자 추상 인터페이스 정의

    - `BaseLLMProvider` ABC 클래스: 모든 LLM 제공자가 구현할 인터페이스
    - `generate()` 추상 메서드: 텍스트 생성 요청
    - `get_models()` 메서드: 사용 가능한 모델 목록 반환
    - `estimate_cost()` 메서드: 요청 비용 추정
    - 파일 위치: `src/agentic_framework/llm/base.py`
    - _Requirements: 4.1 (LLM 추상화), 4.2 (제공자 통합)_

  - [ ] 8.2 프롬프트 및 응답 처리 구조

    - `Prompt` 클래스: 시스템 메시지, 사용자 메시지, 어시스턴트 메시지 구조화
    - `LLMResponse` 클래스: 생성된 텍스트, 토큰 사용량, 메타데이터 포함
    - 프롬프트 템플릿 시스템: 변수 치환 및 조건부 섹션 지원
    - 파일 위치: `src/agentic_framework/llm/prompts.py`
    - _Requirements: 4.1 (프롬프트 관리), 4.4 (템플릿 시스템)_

  - [ ] 8.3 LLM 설정 옵션 관리
    - 온도, max_tokens, top_p 등 생성 파라미터 표준화
    - 제공자별 고유 파라미터 지원 (extra_params 딕셔너리)
    - 설정 검증 및 기본값 적용 로직
    - 파일 위치: `src/agentic_framework/llm/config.py`
    - _Requirements: 4.2 (설정 관리), 7.1 (구성 관리)_

- [ ] 9. Mock LLM 제공자 구현

  **목적**: 실제 LLM API 호출 없이 테스트와 개발을 가능하게 하는 가짜 LLM 제공자 구현

  **왜 필요한가**: 개발 초기 단계에서 실제 LLM API를 호출하면 비용이 발생하고 응답 시간이 길어 개발 속도가 저하됨. 예측 가능한 응답을 제공하는 Mock을 통해 빠른 개발과 테스트 가능

  **세부 작업**:

  - [ ] 9.1 테스트용 가짜 응답 생성기

    - 미리 정의된 응답 패턴 기반 텍스트 생성
    - 프롬프트 키워드에 따른 조건부 응답 시스템
    - 실제 LLM과 유사한 응답 지연 시뮬레이션
    - 파일 위치: `src/agentic_framework/llm/providers/mock.py`
    - _Requirements: 4.1 (테스트 지원)_

  - [ ] 9.2 다양한 응답 시나리오 지원

    - 정상 응답, 에러 응답, 타임아웃 시나리오 설정 가능
    - 토큰 사용량 시뮬레이션 (입력/출력 토큰 계산)
    - 응답 품질 변화 시뮬레이션 (때로는 좋은 답변, 때로는 부정확한 답변)
    - 파일 위치: `src/agentic_framework/llm/providers/mock_scenarios.py`
    - _Requirements: 4.1 (시나리오 테스트)_

  - [ ] 9.3 Mock 제공자 설정 및 제어
    - 응답 패턴 설정 파일 (JSON/YAML) 지원
    - 런타임에 응답 동작 변경 가능한 제어 인터페이스
    - 호출 통계 및 사용 패턴 추적 기능
    - 파일 위치: `src/agentic_framework/llm/providers/mock_config.py`
    - _Requirements: 4.1 (Mock 제어), 6.2 (통계 수집)_

- [ ] 10. 실제 LLM 제공자 연동 (OpenAI)

  **목적**: OpenAI API와의 실제 연동을 구현하여 프로덕션 환경에서 사용 가능한 LLM 기능 제공

  **왜 필요한가**: Mock 제공자로는 실제 AI 기능을 사용할 수 없음. 가장 널리 사용되는 OpenAI API를 먼저 구현하여 실용적인 에이전트 시스템 구축

  **세부 작업**:

  - [ ] 10.1 OpenAI Python SDK 클라이언트 구현

    - OpenAI API 클라이언트 초기화 및 설정
    - Chat Completions API 호출 로직
    - 스트리밍 응답 지원 (실시간 텍스트 생성)
    - 파일 위치: `src/agentic_framework/llm/providers/openai.py`
    - _Requirements: 4.1 (OpenAI 연동), 4.2 (실시간 응답)_

  - [ ] 10.2 API 키 관리 및 인증 처리

    - 환경변수에서 API 키 자동 로딩
    - API 키 유효성 검증 및 권한 확인
    - 여러 API 키 로테이션 지원 (rate limit 회피)
    - 파일 위치: `src/agentic_framework/llm/providers/openai_auth.py`
    - _Requirements: 4.3 (인증 관리), 7.2 (보안)_

  - [ ] 10.3 재시도 로직 및 에러 처리
    - tenacity 라이브러리를 활용한 지능적 재시도
    - Rate limit, 서버 에러, 네트워크 에러별 다른 재시도 전략
    - 비용 추적 및 사용량 모니터링
    - 파일 위치: `src/agentic_framework/llm/providers/openai_retry.py`
    - _Requirements: 4.3 (재시도), 6.2 (비용 추적)_

## Phase 5: 에이전트와 도구 통합

- [ ] 11. 에이전트에 도구 사용 기능 추가

  **목적**: 에이전트가 LLM의 응답을 바탕으로 적절한 도구를 선택하고 실행할 수 있는 통합 시스템 구축

  **왜 필요한가**: 단순히 텍스트만 생성하는 에이전트는 실용성이 제한적임. 실제 작업을 수행하려면 외부 도구와 연동하여 데이터 조회, 계산, 파일 처리 등을 할 수 있어야 함

  **프로그래밍 관점에서의 의미**:

  - **Chain of Responsibility Pattern**: 도구 선택 과정을 체인으로 구성하여 복잡한 의사결정 로직을 단순화
  - **Mediator Pattern**: 에이전트와 도구 간의 복잡한 상호작용을 중재자를 통해 관리하여 결합도 감소
  - **Composite Pattern**: 여러 도구를 조합한 복합 작업을 단일 도구처럼 취급할 수 있는 구조
  - **Error Recovery Patterns**: 도구 실행 실패 시 graceful degradation과 fallback 메커니즘 구현
  - **Separation of Concerns**: 도구 선택 로직, 실행 로직, 결과 처리 로직을 명확히 분리하여 각각의 책임 명확화

  **세부 작업**:

  - [ ] 11.1 도구 호출 메커니즘 구현

    - 에이전트가 사용 가능한 도구 목록 관리
    - LLM 응답에서 도구 호출 의도 파싱 (function calling 패턴)
    - 도구 파라미터 추출 및 검증 로직
    - 파일 위치: `src/agentic_framework/core/tool_integration.py`
    - _Requirements: 1.3 (도구 연동), 2.4 (도구 호출)_

  - [ ] 11.2 도구 실행 결과 처리

    - 도구 실행 결과를 에이전트 응답에 통합
    - 도구 실행 실패 시 대체 방안 제시
    - 여러 도구를 순차적으로 호출하는 체인 실행 지원
    - 파일 위치: `src/agentic_framework/core/tool_results.py`
    - _Requirements: 1.3 (결과 통합), 2.4 (체인 실행)_

  - [ ] 11.3 도구 호출 에러 처리 및 복구
    - 도구 실행 실패 시 에이전트 상태 관리
    - 사용자에게 에러 상황 설명 및 대안 제시
    - 도구 실행 로그 및 디버깅 정보 수집
    - 파일 위치: `src/agentic_framework/core/tool_error_handling.py`
    - _Requirements: 1.3 (에러 처리), 6.1 (로깅)_

- [ ] 12. LLM과 도구를 사용하는 에이전트 구현

  **목적**: LLM의 추론 능력과 도구의 실행 능력을 결합한 완전한 기능의 에이전트 구현

  **왜 필요한가**: 이전 단계에서 구현한 LLM 연동과 도구 시스템을 실제로 결합하여 사용자 요청을 이해하고 적절한 도구를 사용해 작업을 완료하는 실용적인 에이전트 구현

  **세부 작업**:

  - [ ] 12.1 LLM 기반 사용자 입력 처리

    - 사용자 요청 분석 및 의도 파악
    - 필요한 도구 식별 및 실행 계획 수립
    - 컨텍스트 기반 대화 연속성 유지
    - 파일 위치: `src/agentic_framework/agents/llm_agent.py`
    - _Requirements: 1.3 (LLM 통합), 4.4 (의도 파악)_

  - [ ] 12.2 도구 호출 필요성 판단 로직

    - LLM 응답에서 도구 사용 필요성 자동 감지
    - 사용자 요청 유형별 도구 추천 시스템
    - 도구 사용 전 사용자 확인 요청 메커니즘
    - 파일 위치: `src/agentic_framework/agents/tool_decision.py`
    - _Requirements: 1.3 (도구 선택), 2.4 (사용자 확인)_

  - [ ] 12.3 LLM-도구 실행 루프 구현
    - LLM 응답 → 도구 실행 → 결과 반영 → 다음 LLM 호출의 순환 구조
    - 무한 루프 방지 및 최대 실행 횟수 제한
    - 각 단계별 중간 결과 저장 및 복구 지원
    - 파일 위치: `src/agentic_framework/agents/execution_loop.py`
    - _Requirements: 1.3 (실행 루프), 4.4 (순환 처리)_

## Phase 6: 기본 컨텍스트 관리

- [ ] 13. 간단한 메모리 저장소 구현

  **목적**: 대화 기록과 에이전트 상태를 메모리에 저장하고 관리하는 기본적인 저장소 시스템 구축

  **왜 필요한가**: 에이전트가 이전 대화를 기억하고 연속적인 대화를 유지하려면 대화 기록을 저장할 메모리 시스템이 필요함. 초기에는 간단한 인메모리 저장소로 시작하여 기본 기능 검증

  **프로그래밍 관점에서의 의미**:

  - **Repository Pattern**: 데이터 접근 로직을 캡슐화하여 비즈니스 로직과 데이터 저장 방식을 분리
  - **Memory Management**: 메모리 사용량을 모니터링하고 제한하여 메모리 누수 및 OOM 방지
  - **Data Isolation**: 세션별 데이터 격리를 통해 멀티테넌트 환경에서의 보안과 안정성 확보
  - **CRUD Operations**: 기본적인 데이터 조작 연산을 일관된 인터페이스로 제공하여 사용성 향상
  - **Prototype Pattern**: 향후 다양한 저장소 구현체(Redis, Database 등)로 확장 가능한 기반 마련

  **세부 작업**:

  - [ ] 13.1 인메모리 대화 기록 저장소

    - 세션별 대화 기록 저장 구조 (딕셔너리 기반)
    - 메시지 추가, 조회, 삭제 기본 CRUD 연산
    - 메모리 사용량 모니터링 및 제한 설정
    - 파일 위치: `src/agentic_framework/memory/in_memory_store.py`
    - _Requirements: 3.1 (메모리 저장), 3.2 (대화 기록)_

  - [ ] 13.2 세션별 컨텍스트 분리

    - 사용자별, 세션별 독립적인 컨텍스트 관리
    - 세션 생성, 종료, 정리 생명주기 관리
    - 세션 간 데이터 격리 및 보안 보장
    - 파일 위치: `src/agentic_framework/memory/session_manager.py`
    - _Requirements: 3.1 (세션 관리), 3.2 (컨텍스트 격리)_

  - [ ] 13.3 기본적인 컨텍스트 조회 기능
    - 최근 N개 메시지 조회
    - 키워드 기반 메시지 검색
    - 시간 범위별 대화 기록 필터링
    - 파일 위치: `src/agentic_framework/memory/query.py`
    - _Requirements: 3.2 (컨텍스트 조회), 3.3 (검색 기능)_

- [ ] 14. 컨텍스트 매니저 기본 구현

  **목적**: 대화 기록의 효율적인 관리와 LLM 토큰 제한에 맞는 컨텍스트 최적화 시스템 구축

  **왜 필요한가**: LLM은 토큰 제한이 있어 모든 대화 기록을 포함할 수 없음. 중요한 정보는 유지하면서 불필요한 정보는 제거하는 지능적인 컨텍스트 관리가 필요함

  **세부 작업**:

  - [ ] 14.1 대화 기록 저장 및 조회 시스템

    - 구조화된 대화 기록 저장 (사용자 메시지, 에이전트 응답, 도구 호출 결과)
    - 대화 기록 메타데이터 관리 (타임스탬프, 중요도, 카테고리)
    - 빠른 조회를 위한 인덱싱 시스템
    - 파일 위치: `src/agentic_framework/memory/context_manager.py`
    - _Requirements: 3.1 (대화 저장), 3.2 (메타데이터)_

  - [ ] 14.2 컨텍스트 크기 제한 관리

    - 토큰 수 기반 컨텍스트 크기 계산
    - 토큰 제한 초과 시 오래된 메시지 자동 제거
    - 중요한 메시지 보존 우선순위 시스템
    - 파일 위치: `src/agentic_framework/memory/size_manager.py`
    - _Requirements: 3.3 (크기 제한), 4.1 (토큰 관리)_

  - [ ] 14.3 오래된 메시지 자동 정리
    - 시간 기반 메시지 만료 정책
    - 사용 빈도 기반 메시지 중요도 계산
    - 정리된 메시지의 요약 정보 보존
    - 파일 위치: `src/agentic_framework/memory/cleanup.py`
    - _Requirements: 3.3 (자동 정리), 3.1 (요약 보존)_

## Phase 7: 다중 에이전트 기초

- [ ] 15. 에이전트 레지스트리 구현

  **목적**: 여러 에이전트를 중앙에서 관리하고 각 에이전트의 상태를 모니터링할 수 있는 레지스트리 시스템 구축

  **왜 필요한가**: 복잡한 작업을 처리하려면 여러 전문화된 에이전트가 협업해야 함. 각 에이전트를 개별적으로 관리하면 복잡성이 증가하므로 중앙화된 관리 시스템이 필요함

  **프로그래밍 관점에서의 의미**:

  - **Service Locator Pattern**: 에이전트 인스턴스들을 중앙에서 관리하되 의존성 주입의 장점도 활용
  - **Health Check Pattern**: 각 에이전트의 상태를 주기적으로 확인하여 시스템 안정성 보장
  - **Load Balancing**: 동일한 역할의 여러 에이전트 중 가장 적절한 인스턴스 선택 로직
  - **Microservices Architecture**: 각 에이전트를 독립적인 서비스로 취급하여 확장성과 장애 격리 달성
  - **Event-Driven Architecture**: 에이전트 상태 변경을 이벤트로 전파하여 느슨한 결합 유지

  **세부 작업**:

  - [ ] 15.1 에이전트 등록 및 관리 시스템

    - 에이전트 등록, 해제, 업데이트 기능
    - 에이전트 고유 ID 생성 및 중복 방지
    - 에이전트 메타데이터 관리 (이름, 역할, 능력, 상태)
    - 파일 위치: `src/agentic_framework/orchestration/registry.py`
    - _Requirements: 1.1 (에이전트 관리), 1.4 (다중 에이전트)_

  - [ ] 15.2 에이전트 ID 기반 조회 시스템

    - ID, 이름, 역할별 에이전트 검색 기능
    - 에이전트 능력 기반 필터링 (특정 도구 사용 가능한 에이전트 찾기)
    - 에이전트 가용성 확인 (현재 작업 중인지, 응답 가능한지)
    - 파일 위치: `src/agentic_framework/orchestration/discovery.py`
    - _Requirements: 1.4 (에이전트 검색), 1.2 (가용성 확인)_

  - [ ] 15.3 에이전트 상태 모니터링
    - 실시간 에이전트 상태 추적 (활성, 비활성, 오류, 과부하)
    - 에이전트 성능 메트릭 수집 (응답 시간, 성공률, 처리량)
    - 에이전트 건강 상태 체크 및 자동 복구
    - 파일 위치: `src/agentic_framework/orchestration/monitoring.py`
    - _Requirements: 1.2 (상태 모니터링), 6.1 (성능 추적)_

- [ ] 16. 기본 에이전트 오케스트레이터 구현

  **목적**: 여러 에이전트의 실행 순서를 조정하고 에이전트 간 메시지 전달을 관리하는 오케스트레이션 시스템 구축

  **왜 필요한가**: 복잡한 작업은 여러 에이전트가 순차적 또는 병렬적으로 협업해야 함. 에이전트 간 의존성과 실행 순서를 관리하고 결과를 통합하는 중앙 조정자가 필요함

  **세부 작업**:

  - [ ] 16.1 에이전트 실행 순서 관리

    - 에이전트 간 의존성 그래프 구성 (A 완료 후 B 실행)
    - 순차 실행, 병렬 실행, 조건부 실행 패턴 지원
    - 실행 계획 검증 및 순환 의존성 감지
    - 파일 위치: `src/agentic_framework/orchestration/scheduler.py`
    - _Requirements: 1.4 (실행 순서), 5.2 (의존성 관리)_

    **학습 포인트**:

    - **Directed Acyclic Graph (DAG)**: 의존성을 그래프로 모델링하여 복잡한 실행 순서를 체계적으로 관리
    - **Topological Sort**: 의존성 그래프를 기반으로 올바른 실행 순서를 자동으로 계산하는 알고리즘 활용

  - [ ] 16.2 에이전트 간 메시지 전달 시스템

    - 에이전트 간 비동기 메시지 큐 시스템
    - 메시지 라우팅 및 브로드캐스트 기능
    - 메시지 우선순위 및 타임아웃 처리
    - 파일 위치: `src/agentic_framework/orchestration/messaging.py`
    - _Requirements: 1.1 (메시지 전달), 1.4 (에이전트 통신)_

  - [ ] 16.3 에이전트 실행 결과 수집 및 통합
    - 각 에이전트의 실행 결과 수집 및 저장
    - 부분 실패 시 롤백 및 재시도 로직
    - 최종 결과 통합 및 사용자에게 보고
    - 파일 위치: `src/agentic_framework/orchestration/result_collector.py`
    - _Requirements: 1.2 (결과 수집), 1.4 (결과 통합)_

## Phase 8: 기본 워크플로우 시스템

- [ ] 17. 간단한 워크플로우 정의 구조 구현

  **목적**: 복잡한 비즈니스 프로세스를 단계별로 정의하고 실행할 수 있는 선언적 워크플로우 시스템 구축

  **왜 필요한가**: 실제 업무는 단일 에이전트로 해결하기 어려운 복잡한 다단계 프로세스임. 이를 코드로 하드코딩하면 유지보수가 어려우므로 설정 파일로 정의할 수 있는 워크플로우 시스템이 필요함

  **프로그래밍 관점에서의 의미**:

  - **Declarative Programming**: 절차적 코드 대신 선언적 설정으로 워크플로우를 정의하여 가독성과 유지보수성 향상
  - **Domain-Specific Language (DSL)**: 워크플로우 도메인에 특화된 언어로 비개발자도 이해할 수 있는 표현
  - **Interpreter Pattern**: 워크플로우 정의를 해석하고 실행하는 인터프리터 구현
  - **Configuration as Code**: 워크플로우를 코드처럼 버전 관리하고 리뷰할 수 있는 체계
  - **Validation by Design**: 워크플로우 정의 시점에 구조적 오류를 사전 검증하여 런타임 에러 방지

  **세부 작업**:

  - [ ] 17.1 순차 실행 워크플로우 정의

    - YAML/JSON 기반 워크플로우 정의 스키마
    - 단계별 에이전트 매핑 및 입출력 정의
    - 단계 간 데이터 전달 메커니즘
    - 파일 위치: `src/agentic_framework/workflow/definition.py`
    - _Requirements: 5.1 (워크플로우 정의), 5.2 (단계 정의)_

  - [ ] 17.2 워크플로우 단계별 에이전트 매핑

    - 각 워크플로우 단계에 적절한 에이전트 할당
    - 에이전트 능력과 단계 요구사항 매칭
    - 에이전트 가용성 확인 및 대체 에이전트 선택
    - 파일 위치: `src/agentic_framework/workflow/agent_mapping.py`
    - _Requirements: 5.1 (에이전트 매핑), 1.4 (에이전트 선택)_

  - [ ] 17.3 기본적인 워크플로우 검증 로직
    - 워크플로우 정의 문법 검증
    - 참조된 에이전트 및 도구 존재 확인
    - 데이터 흐름 일관성 검사 (출력이 다음 단계 입력과 호환되는지)
    - 파일 위치: `src/agentic_framework/workflow/validation.py`
    - _Requirements: 5.2 (검증), 5.4 (일관성 검사)_

- [ ] 18. 워크플로우 실행 엔진 기본 구현

  **목적**: 정의된 워크플로우를 실제로 실행하고 각 단계의 결과를 관리하는 실행 엔진 구현

  **왜 필요한가**: 워크플로우 정의만으로는 실제 작업이 수행되지 않음. 정의된 워크플로우를 해석하고 각 단계를 순서대로 실행하며 에러 처리와 상태 관리를 담당하는 실행 엔진이 필요함

  **세부 작업**:

  - [ ] 18.1 순차적 단계 실행 엔진

    - 워크플로우 단계를 순서대로 실행하는 메인 루프
    - 각 단계별 실행 상태 추적 (대기, 실행 중, 완료, 실패)
    - 단계별 실행 시간 측정 및 성능 모니터링
    - 파일 위치: `src/agentic_framework/workflow/executor.py`
    - _Requirements: 5.1 (워크플로우 실행), 5.2 (단계 실행)_

  - [ ] 18.2 단계별 결과 전달 메커니즘

    - 이전 단계 출력을 다음 단계 입력으로 전달
    - 데이터 타입 변환 및 형식 맞춤
    - 중간 결과 저장 및 디버깅 지원
    - 파일 위치: `src/agentic_framework/workflow/data_flow.py`
    - _Requirements: 5.2 (데이터 전달), 5.4 (결과 관리)_

  - [ ] 18.3 실행 실패 시 중단 처리
    - 단계 실행 실패 감지 및 워크플로우 중단
    - 실패 원인 분석 및 사용자에게 상세 정보 제공
    - 부분 완료된 작업의 정리 및 리소스 해제
    - 파일 위치: `src/agentic_framework/workflow/error_handling.py`
    - _Requirements: 5.4 (에러 처리), 6.1 (실패 분석)_

## Phase 9: 모니터링 및 로깅 기초

- [ ] 19. 기본 로깅 시스템 구현

  **목적**: 시스템 전체의 동작을 추적하고 문제 발생 시 디버깅할 수 있는 구조화된 로깅 시스템 구축

  **왜 필요한가**: 복잡한 에이전트 시스템에서는 여러 컴포넌트가 비동기적으로 동작하므로 문제 발생 시 원인을 파악하기 어려움. 체계적인 로깅 없이는 프로덕션 환경에서 안정적인 운영이 불가능함

  **프로그래밍 관점에서의 의미**:

  - **Structured Logging**: JSON 형태의 구조화된 로그로 기계 판독성과 검색 효율성 향상
  - **Cross-Cutting Concerns**: 로깅을 횡단 관심사로 처리하여 비즈니스 로직과 분리
  - **Contextual Information**: 요청 ID, 세션 ID 등 컨텍스트 정보를 자동으로 포함하여 분산 시스템에서의 추적성 확보
  - **Log Levels**: 적절한 로그 레벨 분류로 운영 환경에서의 성능 영향 최소화
  - **Observability**: 로깅을 모니터링, 메트릭과 함께 시스템 관찰 가능성의 핵심 요소로 설계

  **세부 작업**:

  - [ ] 19.1 구조화된 로그 메시지 생성

    - JSON 형태의 구조화된 로그 포맷 정의
    - 컨텍스트 정보 자동 포함 (에이전트 ID, 세션 ID, 요청 ID)
    - 로그 메시지 표준화 및 일관성 보장
    - 파일 위치: `src/agentic_framework/logging/structured_logger.py`
    - _Requirements: 6.1 (구조화 로깅), 6.3 (표준화)_

  - [ ] 19.2 로그 레벨별 필터링 시스템

    - DEBUG, INFO, WARNING, ERROR, CRITICAL 레벨 지원
    - 컴포넌트별 로그 레벨 개별 설정
    - 런타임 로그 레벨 동적 변경 기능
    - 파일 위치: `src/agentic_framework/logging/level_manager.py`
    - _Requirements: 6.3 (로그 레벨), 7.1 (동적 설정)_

  - [ ] 19.3 파일 및 콘솔 출력 지원
    - 로그 로테이션 및 압축 기능
    - 콘솔 출력 시 색상 및 포맷팅 지원
    - 원격 로그 수집 시스템 연동 준비 (syslog, ELK 스택)
    - 파일 위치: `src/agentic_framework/logging/output_handlers.py`
    - _Requirements: 6.3 (출력 관리), 6.1 (로그 수집)_

- [ ] 20. 실행 추적 기능 구현

  **목적**: 에이전트와 도구의 실행 성능을 측정하고 시스템 최적화를 위한 메트릭을 수집하는 추적 시스템 구축

  **왜 필요한가**: 성능 병목 지점을 찾고 시스템을 최적화하려면 실행 시간, 리소스 사용량, 성공률 등의 정량적 데이터가 필요함. 이런 데이터 없이는 시스템 개선이 어려움

  **세부 작업**:

  - [ ] 20.1 에이전트 실행 시간 측정

    - 에이전트 시작부터 완료까지 전체 실행 시간 추적
    - 단계별 세부 실행 시간 분석 (LLM 호출, 도구 실행, 데이터 처리)
    - 실행 시간 통계 및 히스토그램 생성
    - 파일 위치: `src/agentic_framework/monitoring/execution_tracker.py`
    - _Requirements: 6.1 (실행 추적), 6.2 (성능 측정)_

  - [ ] 20.2 도구 호출 횟수 및 성공률 추적

    - 도구별 호출 빈도 및 사용 패턴 분석
    - 성공/실패 비율 및 에러 유형별 분류
    - 도구 성능 벤치마크 및 비교 분석
    - 파일 위치: `src/agentic_framework/monitoring/tool_metrics.py`
    - _Requirements: 6.2 (도구 메트릭), 2.3 (성공률 추적)_

  - [ ] 20.3 기본적인 성능 메트릭 수집
    - 메모리 사용량, CPU 사용률, 네트워크 I/O 모니터링
    - 동시 실행 에이전트 수 및 큐 대기 시간 추적
    - 시스템 리소스 임계값 알림 기능
    - 파일 위치: `src/agentic_framework/monitoring/system_metrics.py`
    - _Requirements: 6.2 (시스템 메트릭), 6.1 (리소스 모니터링)_

## Phase 10: 설정 및 배포 지원

- [ ] 21. 설정 관리 시스템 구현

  **목적**: 다양한 환경(개발, 테스트, 프로덕션)에서 일관되게 동작할 수 있는 유연한 설정 관리 시스템 구축

  **왜 필요한가**: 하드코딩된 설정으로는 환경별 배포가 어렵고 보안 정보 관리가 위험함. 환경변수, 설정 파일, 기본값을 체계적으로 관리하는 시스템이 필요함

  **프로그래밍 관점에서의 의미**:

  - **12-Factor App Methodology**: 설정을 환경변수로 외부화하여 코드와 설정의 완전한 분리
  - **Configuration Hierarchy**: 기본값 < 설정파일 < 환경변수 순의 우선순위로 유연한 설정 오버라이드
  - **Type Safety in Configuration**: Pydantic을 활용한 설정 검증으로 런타임 에러 사전 방지
  - **Secrets Management**: 민감한 정보(API 키, 패스워드)의 안전한 관리와 접근 제어
  - **Environment Parity**: 개발, 스테이징, 프로덕션 환경 간 일관성 유지를 위한 설정 표준화

  **세부 작업**:

  - [ ] 21.1 환경변수 기반 설정 로딩

    - python-dotenv를 활용한 .env 파일 지원
    - 환경별 설정 파일 자동 선택 (.env.dev, .env.prod)
    - 환경변수 우선순위 및 오버라이드 규칙 정의
    - 파일 위치: `src/agentic_framework/config/env_loader.py`
    - _Requirements: 7.1 (환경 설정), 7.2 (환경별 배포)_

  - [ ] 21.2 설정 파일 (JSON/YAML) 지원

    - 복잡한 설정을 위한 구조화된 설정 파일 지원
    - 설정 파일 템플릿 및 예제 제공
    - 설정 파일 병합 및 상속 기능 (base.yaml + prod.yaml)
    - 파일 위치: `src/agentic_framework/config/file_loader.py`
    - _Requirements: 7.1 (설정 파일), 7.2 (설정 관리)_

  - [ ] 21.3 Pydantic 기반 설정 검증 및 기본값 처리
    - 설정 스키마 정의 및 타입 검증
    - 필수 설정 누락 시 명확한 에러 메시지
    - 기본값 제공 및 설정 문서 자동 생성
    - 파일 위치: `src/agentic_framework/config/validator.py`
    - _Requirements: 7.2 (설정 검증), 7.1 (기본값)_

- [ ] 22. 예제 애플리케이션 작성

  **목적**: 프레임워크의 모든 기능을 실제로 사용하는 완전한 예제를 통해 사용법 검증 및 문서화

  **왜 필요한가**: 개별 컴포넌트 테스트만으로는 전체 시스템의 통합 동작을 확인하기 어려움. 실제 사용 시나리오를 구현한 예제로 프레임워크의 완성도를 검증하고 사용자에게 참고 자료 제공

  **프로그래밍 관점에서의 의미**:

  - **Integration Testing**: 개별 컴포넌트들이 실제로 함께 동작하는지 검증하는 end-to-end 테스트
  - **Documentation by Example**: 코드 자체가 문서 역할을 하는 실행 가능한 문서화
  - **Best Practices Demonstration**: 프레임워크의 올바른 사용법과 권장 패턴을 구체적으로 보여주는 참고 자료
  - **User Experience Validation**: 실제 사용자 관점에서 API의 사용성과 직관성 검증
  - **Regression Prevention**: 향후 프레임워크 변경 시 기존 기능이 깨지지 않았는지 확인하는 회귀 테스트 역할

  **세부 작업**:

  - [ ] 22.1 간단한 챗봇 예제 구현

    - 사용자 질문에 답변하는 기본 챗봇
    - LLM 연동 및 대화 기록 관리 시연
    - 간단한 도구 사용 (계산기, 날씨 조회 등) 포함
    - 파일 위치: `examples/simple_chatbot.py`
    - _Requirements: 모든 기본 기능 통합 검증_

  - [ ] 22.2 다중 에이전트 협업 예제

    - 여러 전문 에이전트가 협업하는 시나리오 (연구 → 분석 → 보고서 작성)
    - 에이전트 간 메시지 전달 및 워크플로우 실행 시연
    - 각 에이전트의 역할 분담 및 결과 통합 과정 보여주기
    - 파일 위치: `examples/multi_agent_collaboration.py`
    - _Requirements: 1.4 (다중 에이전트), 5.1 (워크플로우)_

  - [ ] 22.3 도구를 활용한 작업 자동화 예제
    - 파일 처리, 데이터 분석, 보고서 생성 등 실용적인 자동화 작업
    - 여러 도구를 연계한 복잡한 작업 흐름 구현
    - 에러 처리 및 복구 시나리오 포함
    - 파일 위치: `examples/automation_workflow.py`
    - _Requirements: 2.4 (도구 연계), 5.4 (에러 처리)_
