#!/bin/bash

# 가상환경 설정 스크립트
echo "🚀 가상환경 설정을 시작합니다..."

# 가상환경 생성
if [ ! -d "venv" ]; then
    echo "📦 가상환경을 생성합니다..."
    python3 -m venv venv
else
    echo "✅ 가상환경이 이미 존재합니다."
fi

# 가상환경 활성화
echo "🔧 가상환경을 활성화합니다..."
source venv/bin/activate

# pip 업그레이드
echo "⬆️  pip을 업그레이드합니다..."
pip install --upgrade pip

# 의존성 설치
echo "📚 의존성을 설치합니다..."
pip install -e ".[dev]"

echo "✨ 설정 완료!"
echo ""
echo "가상환경을 활성화하려면:"
echo "  source venv/bin/activate"
echo ""
echo "가상환경을 비활성화하려면:"
echo "  deactivate"