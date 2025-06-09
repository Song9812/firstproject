import streamlit as st

st.set_page_config(page_title="MBTI VS놀이 추천기", layout="centered")

st.title("⚖️ MBTI별 어울리는 VS놀이 주제")
st.write("MBTI를 선택하면 그 성격 유형에 어울리는 다양한 VS놀이 주제를 확인할 수 있어요! 🎲")

mbti_list = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

mbti_vs_list = {
    "INTJ": [
        "📊 논리적으로 설득하기 vs 🧠 직관적으로 판단하기",
        "🤖 AI 찬성 vs 🚫 AI 반대",
        "📚 계획 세우기 vs 🌀 즉흥 행동",
        "🧩 복잡한 문제 풀기 vs 🎯 간단한 결과 얻기",
        "🎮 전략 게임 vs 🕹️ 액션 게임"
    ],
    "INTP": [
        "🧪 실험 설계 vs 🔍 이론 정리",
        "🧠 질문하는 게 재밌다 vs 🗣️ 답하는 게 재밌다",
        "🧭 새로운 아이디어 만들기 vs 🧱 기존 지식 정리하기",
        "💡 엉뚱한 상상 vs 📏 현실 기반 아이디어",
        "📖 책으로 배우기 vs 🎥 영상으로 배우기"
    ],
    "ENTJ": [
        "🧑‍💼 리더 역할 vs 🧠 전략가 역할",
        "🚀 빠른 실행 vs 🧮 완벽한 준비",
        "📈 경쟁 있는 환경 vs 🌿 조화로운 환경",
        "💼 현실적인 목표 vs 🌈 이상적인 목표",
        "👥 협업 프로젝트 vs 🧍 단독 진행"
    ],
    "ENTP": [
        "🎭 즉흥 연기 vs 🗣️ 즉흥 토론",
        "🧠 생각 많기 vs 🗯️ 말 많기",
        "🌍 현실 여행 vs 🚀 우주여행 상상",
        "📱 새로운 앱 만들기 vs 🧩 기존 기술 해체하기",
        "😂 유머 대결 vs 😎 센스 대결"
    ],
    "INFJ": [
        "🧭 운명 믿기 vs 🧱 현실 만들기",
        "📖 소설 읽기 vs 🎬 감동 영화 보기",
        "🧘 명상 vs 🎨 그림 그리기",
        "🧑‍🤝‍🧑 깊은 인간관계 vs 🌐 다양한 네트워크",
        "🎁 마음 담긴 편지 vs 🎉 직접 준비한 이벤트"
    ],
    "INFP": [
        "❤️ 이상적 사랑 vs 💬 현실적 사랑",
        "🎨 창작 하기 vs 📚 감상 하기",
        "🌌 우주 이야기 vs 🧚 동화 이야기",
        "😢 눈물 나는 영화 vs 😂 웃긴 영화",
        "🎶 가사에 집중 vs 🎵 멜로디에 집중"
    ],
    "ENFJ": [
        "💖 진심 표현하기 vs 🤹 센스 있게 대처하기",
        "🌱 성장을 위한 대화 vs 🎁 감동 주는 대화",
        "👥 단체 활동 vs 🧑‍🤝‍🧑 1:1 깊은 대화",
        "📣 발표 준비 vs 🧏 경청 훈련",
        "🌈 긍정 조언하기 vs 🧱 현실 조언하기"
    ],
    "ENFP": [
        "🔥 하고 싶은 일 vs 🧠 잘하는 일",
        "✈️ 즉흥 여행 vs 📆 계획 여행",
        "🎨 창의성 발휘 vs 🧭 자유 탐험",
        "🧩 퍼즐 맞추기 vs 🧚 이야기 짓기",
        "🎤 프레젠테이션 vs 🎭 연극하기"
    ],
    "ISTJ": [
        "🗓 루틴 있는 삶 vs 🌊 자유로운 삶",
        "📑 매뉴얼 따르기 vs 🧪 실험해 보기",
        "📂 문서 정리 vs 🗃 자료 수집",
        "📈 통계 기반 분석 vs 🧠 직관적 판단",
        "🏠 집 꾸미기 vs 🧹 집 정리하기"
    ],
    "ISFJ": [
        "📔 일기 쓰기 vs 📷 사진 찍기",
        "💌 손편지 vs 🎁 직접 만든 선물",
        "👨‍👩‍👧 가족과 시간 보내기 vs 👯 친구와 수다",
        "🥣 직접 요리하기 vs 🍽️ 외식하기",
        "📆 계획한 하루 vs 🎲 예측불가 하루"
    ],
    "ESTJ": [
        "📊 결과 중심 vs 🛤️ 과정 중심",
        "👨‍⚖️ 규칙 따르기 vs 🎨 유연한 상황 대처",
        "📈 경쟁하기 vs 🧘 협력하기",
        "🧱 현실적인 이야기 vs 🌈 감성적인 이야기",
        "🏢 회사 이야기 vs 🏠 개인 생활 이야기"
    ],
    "ESFJ": [
        "👫 단체 활동 vs 🧍 1:1 대화",
        "🎂 깜짝 이벤트 vs 🎁 정성 선물",
        "💬 문자로 대화 vs 📞 전화 통화",
        "📸 사진 많이 찍기 vs 🎥 영상으로 기록",
        "👗 스타일링 하기 vs 🎨 꾸미기 게임"
    ],
    "ISTP": [
        "🧠 논리로 설득하기 vs 💬 감성으로 공감하기",
        "🔧 고치기 vs 🧱 만들기",
        "🧮 수학 퍼즐 vs 🧩 추리 게임",
        "🏍 스피드 즐기기 vs 🚴 안정감 추구",
        "📏 측정하기 vs ✏️ 추정하기"
    ],
    "ISFP": [
        "🍃 자연 산책 vs 🖼 갤러리 관람",
        "🎵 음악 듣기 vs 🎨 그림 그리기",
        "📸 감성 사진 찍기 vs 🪴 식물 키우기",
        "🌌 밤 산책 vs ☀️ 아침 산책",
        "🎁 감성 선물 주기 vs 💬 짧은 편지 쓰기"
    ],
    "ESTP": [
        "🎢 놀이공원 가기 vs 🏕 캠핑 가기",
        "🎯 목표 중심 여행 vs 🎲 즉흥 여행",
        "🤣 유머 대결 vs 🎭 역할극",
        "🕺 댄스타임 vs 🎮 게임타임",
        "🏃 액티비티 vs 🧘 휴식"
    ],
    "ESFP": [
        "🎤 노래방 가기 vs 🎶 콘서트 가기",
        "📷 인생샷 찍기 vs 🎥 브이로그 찍기",
        "🍰 디저트 만들기 vs 🍱 요리하기",
        "🎁 선물 포장하기 vs 🎀 이벤트 꾸미기",
        "🎉 파티 준비하기 vs 💃 무대 서보기"
    ]
}

if "selected_mbti" not in st.session_state:
    st.session_state.selected_mbti = None

cols = st.columns(4)
for i, mbti in enumerate(mbti_list):
    if cols[i % 4].button(mbti):
        st.session_state.selected_mbti = mbti

if st.session_state.selected_mbti:
    mbti = st.session_state.selected_mbti
    st.markdown(f"## 🎭 {mbti} 어울리는 VS놀이 주제 예시")
    for vs in mbti_vs_list[mbti]:
        st.markdown(f"- {vs}")
