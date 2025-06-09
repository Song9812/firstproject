import streamlit as st

st.set_page_config(page_title="MBTI 대화 가이드", layout="centered")

st.title("💬 MBTI 대화 가이드 & 예시 추천기")
st.write("MBTI를 선택하면 해당 유형과 대화하기 좋은 주제, 말투, 예시를 확인할 수 있어요!")

# 모든 MBTI 유형
mbti_list = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

# 성격 요약
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

# 대화 주제 추천
mbti_topics = {
    "INTJ": [("미래 기술", "미래를 설계하는 데 관심이 많기 때문입니다."),
             ("전략 게임", "복잡한 사고를 자극하는 활동을 선호해서입니다."),
             ("자기계발", "목표 지향적인 성격과 잘 맞기 때문입니다."),
             ("사회 구조 변화", "큰 그림을 보는 능력과 관련된 주제입니다."),
             ("철학적 대화", "깊고 의미 있는 주제를 좋아하기 때문입니다.")],
    "INFP": [("감동적인 영화", "감성적이고 이야기 중심의 대화를 좋아합니다."),
             ("자기 꿈 이야기", "이상과 가치를 나누는 데 관심이 많습니다."),
             ("어릴 적 추억", "감정에 연결된 기억을 소중히 여깁니다."),
             ("사랑과 관계", "깊이 있는 감정 교류를 선호합니다."),
             ("예술과 창작", "상상력과 창의력을 표현할 수 있습니다.")],
    # 나머지 유형은 위 이전 답변에서 복사해서 붙여넣기 가능
    # ...
}

# 대화 팁
mbti_tips = {
    "INTJ": "논리적이고 간결하게 정리된 말투로 접근하면 신뢰를 얻을 수 있어요.",
    "INFP": "따뜻하고 진정성 있는 말로 다가가면 깊은 대화를 나누기 좋아요.",
    # 나머지 유형 추가 가능
    # ...
}

# 추천 말투 예시
mbti_phrases = {
    "INTJ": "“이런 주제에 대해 어떻게 생각하세요? 전략적인 관점이 궁금해서요.”",
    "INFP": "“그때 느꼈던 감정이나 생각을 나눠줄 수 있어요? 듣고 싶어요.”",
    # 나머지 유형 추가 가능
    # ...
}

# 대화 예시 생성기
def generate_conversation(mbti):
    if mbti == "INTJ":
        return [
            "🙋‍♂️: 요즘 AI 기술이 사회에 어떤 영향을 줄지 생각해본 적 있어?",
            "🧠 INTJ: 그거 꽤 흥미로운 주제네. 특히 노동 시장의 변화가 가장 큰 변수라고 봐."
        ]
    elif mbti == "INFP":
        return [
            "🙋‍♂️: 어릴 때 가장 기억에 남는 순간이 있어?",
            "🌸 INFP: 음... 초등학교 때 친구랑 비 오는 날 우산 없이 걷던 기억이 아직도 따뜻해."
        ]
    else:
        return [
            "🙋‍♂️: 흥미로운 대화를 시작해보세요!",
            "🙂: 상대방의 성격에 맞게 감정 또는 논리를 고려해 접근하면 좋아요."
        ]

# 상태 저장
if "selected_mbti" not in st.session_state:
    st.session_state.selected_mbti = None

# 버튼으로 MBTI 선택
cols = st.columns(4)
for i, mbti in enumerate(mbti_list):
    if cols[i % 4].button(mbti):
        st.session_state.selected_mbti = mbti

# 결과 출력
if st.session_state.selected_mbti:
    mbti = st.session_state.selected_mbti
    st.markdown(f"## 🧠 {mbti} 성격 요약")
    st.info(mbti_traits.get(mbti, "정보 없음"))

    st.markdown("### 🗣️ 대화에 어울리는 주제 & 이유")
    topics = mbti_topics.get(mbti, [])
    for i, (topic, reason) in enumerate(topics, 1):
        st.markdown(f"**{i}. {topic}**  \n→ {reason}")

    st.markdown("### 💬 대화할 때 이런 말투를 써보세요")
    st.success(mbti_tips.get(mbti, "말투 정보 없음"))

    st.markdown("**📝 예시 표현:**")
    st.write(mbti_phrases.get(mbti, "예시 문장 없음"))

    st.markdown("### 🎭 대화 예시")
    convo = generate_conversation(mbti)
    for line in convo:
        st.markdown(line)

