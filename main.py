import streamlit as st

st.set_page_config(page_title="💬 MBTI 대화 주제 추천기", layout="centered")

st.title("💬 MBTI 대화 주제 추천기")
st.write("MBTI를 선택하면 해당 유형과 대화하기 좋은 주제와 추천 이유를 서술형으로 알려드려요!")

mbti_list = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

mbti_traits = {
    "INTJ": "🧠 전략적이고 분석적인 성향으로 깊은 대화와 아이디어 공유를 선호합니다.",
    "INTP": "🔍 논리적이고 호기심 많은 성격으로, 새로운 이론과 개념을 탐구하는 것을 좋아합니다.",
    "ENTJ": "🚀 리더십이 강하고 목표 지향적이며, 효율성과 계획에 관심이 많습니다.",
    "ENTP": "💡 창의적이고 토론을 즐기며, 다양한 아이디어에 열려 있는 편입니다.",
    "INFJ": "🌱 이상주의적이며 공감 능력이 뛰어나고, 의미 있는 관계와 대화를 선호합니다.",
    "INFP": "🎨 감성적이고 상상력이 풍부하며, 자신의 가치와 감정을 표현하는 것을 좋아합니다.",
    "ENFJ": "🤝 사람 중심적이며 타인의 감정에 민감하고, 진심 어린 교감을 중요시합니다.",
    "ENFP": "🔥 열정적이고 자유로운 사고를 지닌 사람으로, 새로운 것에 대한 호기심이 많습니다.",
    "ISTJ": "📋 책임감 있고 실용적인 사고를 지닌 성격으로, 체계적인 대화를 선호합니다.",
    "ISFJ": "🌷 조용하지만 따뜻하고 헌신적인 성향으로, 배려 깊은 대화를 좋아합니다.",
    "ESTJ": "🏢 단호하고 현실적인 성격으로, 명확하고 논리적인 대화를 선호합니다.",
    "ESFJ": "🎉 사교적이며 배려심이 강하고, 감정적 연결과 조화를 중요하게 여깁니다.",
    "ISTP": "🔧 객관적이고 침착하며, 분석적 사고와 실용적 주제를 선호합니다.",
    "ISFP": "🍃 감성적이고 조용한 성향이며, 예술적이거나 자연과 관련된 대화를 좋아합니다.",
    "ESTP": "⚡ 즉흥적이고 에너제틱한 성격으로, 액티브하고 생생한 대화를 즐깁니다.",
    "ESFP": "🎈 유쾌하고 외향적인 성격으로, 즐겁고 감각적인 대화를 좋아합니다."
}

mbti_topics_with_reasons = {
    "INTJ": [
        ("미래 기술이 어떻게 발전할지 함께 이야기해봐요 🔮", "전략적 사고를 좋아하므로 미래에 대한 전망을 이야기하면 흥미로워합니다."),
        ("자기계발을 위해 어떤 방법을 쓰는지 공유해요 📈", "목표 지향적인 성격으로 자기 성장에 대한 이야기를 선호합니다."),
        ("사회 구조가 어떻게 변화할지 의견을 나눠봐요 🏛️", "시스템에 대한 개선을 고민하는 성향이 있어 의견 나누기를 좋아합니다."),
        ("철학적 질문이나 윤리 문제에 대해 깊이 생각해봐요 📚", "깊이 있는 사고를 즐기므로 철학이나 윤리적 주제를 선호합니다."),
        ("전략 게임이나 복잡한 계획에 대해 이야기해요 🎲", "복잡한 규칙과 계획이 필요한 활동을 좋아합니다.")
    ],
    "INTP": [
        ("최근 과학적 발견에 대해 궁금한 점을 이야기해요 🔬", "호기심이 많고 분석적이라 새로운 발견에 관심이 많습니다."),
        ("이론적인 질문이나 추상적 개념에 대해 토론해봐요 ❓", "추상적인 개념이나 가설을 다루는 대화를 즐깁니다."),
        ("시스템 설계나 복잡한 구조를 분석해보아요 🧩", "복잡한 구조나 원리를 분석하는 것을 좋아합니다."),
        ("정보 속에서 패턴을 찾아내는 방법에 대해 이야기해요 🔎", "정보 속에서 규칙을 찾는 것을 즐깁니다."),
        ("논리 퀴즈나 문제 풀이를 함께 해봐요 🧠", "재미있게 사고력을 시험할 수 있는 주제입니다.")
    ],
    "ENTJ": [
        ("비즈니스 아이디어를 나누며 의견을 교환해요 💼", "사업과 성과에 대한 이야기를 즐깁니다."),
        ("목표를 설정하고 계획하는 방법에 대해 이야기해봐요 🎯", "계획을 세우고 추진하는 것을 좋아합니다."),
        ("리더십 스타일과 조직 관리에 대해 토론해요 👔", "조직을 이끄는 방식에 대한 대화에 관심이 많습니다."),
        ("생산성을 높이는 팁을 공유해봐요 ⚙️", "효율을 중시하는 성향이 있습니다."),
        ("정치나 사회 변화에 대한 의견을 나눠요 🏛️", "의사결정 구조와 시스템 변화에 관심이 많습니다.")
    ],
    "ENTP": [
        ("창의적인 아이디어를 자유롭게 나누어봐요 💡", "새로운 아이디어를 자유롭게 나누는 것을 즐깁니다."),
        ("즉흥 연기나 재미있는 상황극을 함께 해봐요 🎭", "상상력과 유머가 필요한 활동에 강합니다."),
        ("가상 시나리오를 만들어 미래를 상상해봐요 🛸", "가정을 기반으로 한 대화를 좋아합니다."),
        ("미래에 대해 신선한 아이디어를 공유해요 🚀", "상상력과 비전을 공유하는 것을 좋아합니다."),
        ("유쾌한 토론으로 생각을 확장해봐요 🗣️", "토론을 통해 생각을 확장하기를 즐깁니다.")
    ],
    "INFJ": [
        ("인생의 의미에 대해 깊이 이야기해봐요 🌌", "깊은 감성과 철학적 주제에 끌립니다."),
        ("심리학이나 사람의 내면에 대해 탐구해요 🧘‍♂️", "사람의 내면에 관심이 많습니다."),
        ("타인을 돕는 일에 대해 생각을 나눠봐요 💖", "타인을 위한 행동에서 가치와 의미를 찾습니다."),
        ("사회 정의와 문제 해결에 대해 이야기해요 ⚖️", "세상의 문제를 진지하게 생각하고 해결책을 고민합니다."),
        ("감정을 솔직하게 공유하는 시간을 가져봐요 💬", "공감하는 대화를 좋아합니다.")
    ],
    "INFP": [
        ("감동적인 영화나 책에 대해 이야기해봐요 🎬", "감정을 자극하는 콘텐츠를 좋아합니다."),
        ("자신의 꿈과 이상에 대해 솔직히 나누어봐요 🌈", "개인의 가치와 이상을 이야기하는 것을 좋아합니다."),
        ("어릴 적 추억을 떠올리며 감성적인 대화를 나눠요 🧸", "감성적인 기억을 소중히 여깁니다."),
        ("사랑과 관계에 대해 진솔하게 이야기해요 ❤️", "사람 간의 진실한 관계에 집중합니다."),
        ("예술과 창작 활동에 대해 경험을 나누어봐요 🎨", "자신만의 감성을 표현하는 활동을 좋아합니다.")
    ],
    "ENFJ": [
        ("사람과의 관계나 성장 이야기를 나눠봐요 🤗", "타인과의 관계, 성장 이야기에 관심이 많습니다."),
        ("공감과 격려가 담긴 대화를 해봐요 🌟", "진심이 담긴 감정 표현을 중요하게 여깁니다."),
        ("심리적 연결과 소통에 대해 이야기해요 💞", "감정적 소통에서 의미를 찾습니다."),
        ("긍정적인 변화를 만드는 방법을 토론해요 ✨", "타인을 위한 조언과 응원을 아끼지 않습니다."),
        ("사회적 책임과 봉사에 대해 생각해봐요 🌍", "세상에 긍정적인 영향을 주는 것을 중요하게 생각합니다.")
    ],
    "ENFP": [
        ("여행에서의 새로운 경험을 나눠봐요 🧳", "새로운 경험과 자극을 좋아합니다."),
        ("새로운 취미나 관심사에 대해 이야기해요 🎸", "다양한 관심사를 공유하는 것을 즐깁니다."),
        ("인생에서 도전했던 순간들을 공유해봐요 🧗‍♂️", "자유롭고 도전적인 삶을 지향합니다."),
        ("다양한 문화를 경험한 이야기를 나눠요 🌏", "다름과 다양성에 관심이 많습니다."),
        ("창의적인 상상과 아이디어를 자유롭게 펼쳐봐요 🎉", "상상력을 발휘할 수 있는 주제를 좋아합니다.")
    ],
    "ISTJ": [
        ("일상의 루틴과 규칙에 대해 이야기해봐요 ⏰", "규칙적이고 안정적인 것을 선호합니다."),
        ("효과적인 계획 세우기 방법을 공유해요 📝", "사전에 준비하고 조직하는 것을 좋아합니다."),
        ("일 처리 방식과 노하우를 나눠봐요 🛠️", "효율적이고 현실적인 접근을 선호합니다."),
        ("전통과 가치에 대해 의견을 나누어봐요 🏡", "오랜 가치나 규범을 중요하게 생각합니다."),
        ("정리정돈 노하우를 함께 공유해요 🧹", "체계적인 시스템을 선호합니다.")
    ],
    "ISFJ": [
        ("가족과 소중한 기억을 나눠봐요 👨‍👩‍👧‍👦", "가까운 사람들과의 관계를 소중히 여깁니다."),
        ("도움이 되었던 경험을 공유해봐요 🙌", "봉사나 배려에 관심이 많습니다."),
        ("추억과 감성을 자극하는 이야기를 나눠요 🕯️", "정서적인 연결을 느끼는 주제를 선호합니다."),
        ("감사한 일들에 대해 이야기해봐요 🌸", "따뜻한 감정 표현을 좋아합니다."),
        ("정리와 실생활 팁을 함께 나누어봐요 🧺", "정리정돈과 실생활 팁을 공유하는 것을 좋아합니다.")
    ],
    "ESTJ": [
        ("사회 규칙과 질서에 대해 이야기해봐요 📏", "체계와 규율을 중시합니다."),
        ("효과적인 일하는 방식을 공유해요 🏢", "현실적이고 실용적인 대화를 선호합니다."),
        ("조직과 시스템에 대해 토론해봐요 🏛️", "구조적인 시스템에 관심이 많습니다."),
        ("결정 내리는 법과 판단 기준을 나눠봐요 ⚖️", "논리적 판단을 중시합니다."),
        ("현실적인 조언과 팁을 공유해봐요 🗣️", "실질적인 도움을 주는 것을 좋아합니다.")
    ],
    "ESFJ": [
        ("친구와의 관계와 소통에 대해 이야기해봐요 👫", "인간관계와 조화에 관심이 많습니다."),
        ("감정을 솔직하게 나누는 시간을 가져봐요 💕", "감정을 공유하는 대화를 선호합니다."),
        ("행사나 모임 준비 경험을 공유해봐요 🎈", "타인을 위한 활동을 좋아합니다."),
        ("배려와 다정함에 대해 이야기해요 🤗", "다정함과 친절을 중요시합니다."),
        ("공동체와 협력 경험을 나눠봐요 🏘️", "협력과 관계 형성에 관심이 많습니다.")
    ],
    "ISTP": [
        ("기계나 도구에 대해 관심사를 나눠봐요 ⚙️", "실용적인 것에 관심이 많습니다."),
        ("문제 해결 경험을 공유해봐요 🧩", "논리적이고 즉각적인 해결을 선호합니다."),
        ("액티비티와 스포츠에 대해 이야기해봐요 🏄‍♂️", "행동과 경험 중심의 대화를 좋아합니다."),
        ("기술이나 트렌드에 대해 탐구해봐요 💻", "최신 기술에 관심이 많습니다."),
        ("직접 체험한 일들을 재미있게 나누어봐요 🎯", "경험 중심의 이야기를 즐깁니다.")
    ],
    "ISFP": [
        ("자연이나 예술에 대해 감성을 나눠봐요 🌿", "감성적이고 자연을 좋아합니다."),
        ("감동적인 음악이나 그림에 대해 이야기해요 🎶", "예술적 표현을 즐깁니다."),
        ("내면의 감정과 생각을 솔직히 나누어봐요 💭", "내면 표현에 관심이 많습니다."),
        ("소소한 일상 속 행복을 공유해요 ☕", "작은 행복과 감정을 소중히 여깁니다."),
        ("편안한 분위기에서 조용한 대화를 나눠봐요 🕯️", "조용하고 평화로운 환경을 좋아합니다.")
    ],
    "ESTP": [
        ("액티브한 모험이나 스포츠 이야기를 나눠봐요 🏎️", "즉흥적이고 활동적인 주제를 좋아합니다."),
        ("도전적인 경험을 공유해봐요 🧗‍♂️", "도전과 스릴을 즐깁니다."),
        ("재미있는 상황극이나 유머를 함께 나눠요 😂", "유머와 재미있는 대화를 선호합니다."),
        ("트렌디한 주제나 핫이슈에 대해 이야기해요 🔥", "최신 이슈에 관심이 많습니다."),
        ("현장 경험을 중심으로 대화해봐요 🎯", "직접 경험한 이야기를 좋아합니다.")
    ],
    "ESFP": [
        ("즐거운 파티나 행사 경험을 나눠봐요 🎉", "즐겁고 활기찬 분위기를 좋아합니다."),
        ("유쾌한 이야기와 농담을 함께 나눠요 😄", "유머 감각이 뛰어납니다."),
        ("새로운 사람들과의 만남을 이야기해봐요 🤗", "사교적인 대화를 선호합니다."),
        ("감각적인 취미나 활동에 대해 이야기해요 🎨", "감각적이고 예술적인 것을 좋아합니다."),
        ("현장의 생생한 경험을 공유해봐요 🎤", "직접 경험한 것을 이야기하는 것을 즐깁니다.")
    ],
}

def show_mbti_buttons():
    st.write("아래 버튼 중에서 본인의 MBTI를 눌러주세요!👇")
    cols = st.columns(4)
    selected_mbti = None
    for i, mbti in enumerate(mbti_list):
        if cols[i % 4].button(mbti):
            selected_mbti = mbti
    return selected_mbti

def main():
    selected = show_mbti_buttons()
    if selected:
        st.markdown(f"### ✨ 당신의 MBTI는 **{selected}** 입니다!")
        st.write(mbti_traits[selected])
        st.markdown("#### 🗣️ 추천 대화 주제와 이유")
        for topic, reason in mbti_topics_with_reasons[selected]:
            st.write(f"• {topic} — {reason}")

if __name__ == "__main__":
    main()
