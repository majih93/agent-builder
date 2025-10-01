# 가상환경 사용 가이드

## 빠른 시작

### 1. 가상환경 설정 (최초 1회)

```bash
./setup_venv.sh
```

### 2. 가상환경 활성화

```bash
source venv/bin/activate
# 또는
./activate_venv.sh
```

### 3. 가상환경 비활성화

```bash
deactivate
```

## 개발 워크플로우

1. **프로젝트 시작할 때**

   ```bash
   source venv/bin/activate
   ```

2. **개발 작업**

   ```bash
   # 테스트 실행
   pytest

   # 코드 포맷팅
   black src/ tests/
   isort src/ tests/

   # 타입 체크
   mypy src/
   ```

3. **작업 완료 후**
   ```bash
   deactivate
   ```

## 의존성 관리

- **새 패키지 설치**: `pip install package-name`
- **개발 의존성 재설치**: `pip install -e ".[dev]"`
- **requirements 업데이트**: `pip freeze > requirements.txt`

## 문제 해결

### 가상환경이 활성화되지 않을 때

```bash
# 가상환경 삭제 후 재생성
rm -rf venv
./setup_venv.sh
```

### Python 버전 확인

```bash
python --version  # 가상환경의 Python
which python      # Python 경로 확인
```
