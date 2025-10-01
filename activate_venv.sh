#!/bin/bash

# 가상환경 활성화 스크립트
if [ -d "venv" ]; then
    echo "🔧 가상환경을 활성화합니다..."
    source venv/bin/activate
    echo "✅ 가상환경이 활성화되었습니다!"
    echo "현재 Python: $(which python)"
    echo "현재 pip: $(which pip)"
else
    echo "❌ 가상환경이 없습니다. 먼저 ./setup_venv.sh를 실행해주세요."
fi