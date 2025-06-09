import streamlit as st

st.set_page_config(page_title="MBTI 대화 가이드", layout="centered")

st.title("💬 MBTI 대화 가이드 & 예시 추천기")
st.write("MBTI를 선택하고, 대화 스타일을 고르면 해당 유형과 대화하기 좋은 주제, 말투, 예시를 확인할 수 있어요!")

mbti_list = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

styles = {
    "공식적인 말투": "~합니다", 
    "친근한 말투": "~해요"
}

mbti_traits = {
    "INTJ": "전략적이고 분석적인 성향으로 깊은 대화와 아이디어 공유를 선호합니다.",
    "INTP": "논리적이고 호기심 많은 성격으로, 새로운 이론과 개념을 탐구하는 것을 좋아합니다.",
    "ENTJ": "리더십이 강하고 목표 지향적이며, 효율성과 계획에 관심이 많습니다.",
    "ENTP": "창의적이고 토론을 즐기며, 다양한 아이디어에 열려 있는 편입니다.",
    "INFJ": "이상주의적이며 공감 능력이 뛰어나고, 의미 있는 관계와 대화를 선호합니다.",
    "INFP": "감성적이고 상상력이 풍부하며, 자신의 가치와 감정을 표현하는 것을 좋아합니다.",
    "ENFJ": "사람 중심적이며 타인의 감정에 민감하고, 진심 어린 교감을 중요시합니다.",
    "ENFP": "열정적이고 자유로운 사고를 지닌 사람으로, 새로운 것에 대한 호기심이 많습니다.",
    "ISTJ": "책임감 있고 실용적인 사고를 지닌 성격으로, 체계적인 대화를 선호합니다.",
    "ISFJ": "조용하지만 따뜻하고 헌신적인 성향으로, 배려 깊은 대화를 좋아합니다.",
    "ESTJ": "단호하고 현실적인 성격으로, 명확하고 논리적인 대화를 선호합니다.",
    "ESFJ": "사교적이며 배려심이 강하고, 감정적 연결과 조화를 중요하게 여깁니다.",
    "ISTP": "객관적이고 침착하며, 분석적 사고와 실용적 주제를 선호합니다.",
    "ISFP": "감성적이고 조용한 성향이며, 예술적이거나 자연과 관련된 대화를 좋아합니다.",
    "ESTP": "즉흥적이고 에너제틱한 성격으로, 액티브하고 생생한 대화를 즐깁니다.",
    "ESFP": "유쾌하고 외향적인 성격으로, 즐겁고 감각적인 대화를 좋아합니다."
}

mbti_topics = {
    "INTJ": ["미래 기술", "전략 게임", "자기계발", "사회 구조 변화", "철학적 대화"],
    "INTP": ["과학적 발견", "이론적 질문", "패턴 분석", "시스템 설계", "논리 퀴즈"],
    "ENTJ": ["비즈니스 아이디어", "목표 설정", "리더십 이론", "생산성 방법", "정치 토론"],
    "ENTP": ["창의적 발상", "유쾌한 토론", "가상 시나리오", "즉흥 연기", "미래 상상"],
    "INFJ": ["인생 의미", "심리학 이야기", "도움 줄 수 있는 일", "사회 정의", "감정 공유"],
    "INFP": ["감동적인 영화", "자기 꿈 이야기", "어릴 적 추억", "사랑과 관계", "예술과 창작"],
    "ENFJ": ["사람과 사람 사이 이야기", "심리적인 연결", "긍정적인 변화", "격려와 응원", "공감 이야기"],
    "ENFP": ["여행 이야기", "새로운 취미", "인생 도전기", "다양한 문화", "창의적 상상"],
    "ISTJ": ["일상 루틴", "효율적인 방법", "일 처리 방식", "전통 가치", "계획 세우기"],
    "ISFJ": ["가족 이야기", "추억 이야기", "도움이 되었던 경험", "정리정돈 방법", "감사한 일"],
    "ESTJ": ["사회 규칙", "현실적인 해결책", "조직 이야기", "일하는 방식", "결정 내리는 법"],
    "ESFJ": ["친구 관계", "감정 나누기", "행사 준비", "배려 경험", "공동체 이야기"],
    "ISTP": ["기계나 도구", "논리적 문제", "재미있는 실험", "실용적인 팁", "분석 토론"],
    "ISFP": ["자연 이야기", "감성적 음악", "예술 창작", "개인 공간", "감정 표현"],
    "ESTP": ["스포츠 경기", "즉흥 활동", "현장 체험", "기억에 남는 사건", "유머 이야기"],
    "ESFP": ["공연 경험", "맛집 추천", "즐거운 추억", "웃긴 이야기", "음악과 춤"]
}

mbti_tips = {
    "INTJ": "논리적이고 간결하게 요점만 말하는 방식이 좋습니다.",
    "INTP": "지적인 주제를 함께 탐구하는 듯한 말투가 효과적입니다.",
    "ENTJ": "직접적이고 목표 중심적인 화법을 좋아합니다.",
    "ENTP": "재미있고 유쾌하게, 다양한 아이디어를 던지며 접근하세요.",
    "INFJ": "진심이 담긴 말투로 조심스럽게 접근하면 신뢰를 얻습니다.",
    "INFP": "감성적이고 부드러운 말투가 잘 통합니다.",
    "ENFJ": "다정하고 따뜻하게 관심을 표현하는 것이 좋습니다.",
    "ENFP": "에너지 넘치고 열정적으로 이야기하면 연결됩니다.",
    "ISTJ": "정확하고 신중한 말투를 사용하면 신뢰를 줍니다.",
    "ISFJ": "배려 깊고 예의 바른 표현이 효과적입니다.",
    "ESTJ": "논리적이고 실질적인 말투를 선호합니다.",
    "ESFJ": "공감과 배려가 담긴 화법이 잘 맞습니다.",
    "ISTP": "과장 없는 사실 기반 말투가 신뢰를 줍니다.",
    "ISFP": "조용하고 섬세한 표현이 잘 어울립니다.",
    "ESTP": "직관적이고 에너지 넘치는 말투로 접근하세요.",
    "ESFP": "유쾌하고 감각적인 표현이 호감을 줍니다."
}

def generate_phrase(mbti, style):
    if style == "공식적인 말투":
        return f"{mbti} 유형에게는 '{mbti_tips[mbti]}' 말투로 접근하는 것이 좋습니다."
    else:
        return f"{mbti}에게는 편하게 다가가며 '{mbti_tips[mbti].replace('습니다', '해요')}' 말투가 좋아요."

def generate_conversation_example(mbti, style):
    intro = "🙋‍♂️: 요즘 관심 있는 주제가 뭐예요?"
    reply = f"🙂 ({mbti}): 저는 '{mbti_topics[mbti][0]}' 같은 주제가 재미있더라고요!"
    if style == "공식적인 말투":
        return [intro, reply.replace("요", "니다")]
    return [intro, reply]

if "selected_mbti" not in st.session_state:
    st.session_state.selected_mbti = None

cols = st.columns(4)
for i, mbti in enumerate(mbti_list):
    if cols[i % 4].button(mbti):
        st.session_state.selected_mbti = mbti

style = st.selectbox("🗨️ 대화 스타일을 선택하세요", list(styles.keys()))

if st.session_state.selected_mbti:
    mbti = st.session_state.selected_mbti
    st.markdown(f"## 🧠 {mbti} 성격 요약")
    st.info(mbti_traits[mbti])

    st.markdown("### 🗣️ 대화에 어울리는 주제")
    for topic in mbti_topics[mbti]:
        st.markdown(f"- {topic}")

    st.markdown("### 💬 대화 팁")
    st.success(generate_phrase(mbti, style))

    st.markdown("### 🎭 대화 예시")
    convo = generate_conversation_example(mbti, style)
    for line in convo:
        st.markdown(line)
