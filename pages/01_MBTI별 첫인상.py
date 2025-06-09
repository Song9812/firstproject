import streamlit as st

st.set_page_config(page_title="✨ MBTI 첫인상 이미지 느낌", layout="centered")

st.title("✨ MBTI별 첫인상 느낌 표현")
st.write("MBTI 버튼을 눌러 해당 유형의 첫인상을 이모지와 간단한 텍스트로 확인해보세요!")

mbti_list = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

mbti_first_impression = {
    "INTJ": "🧠🔍 전략가, 깊고 냉철한 사고",
    "INTP": "🤔💡 탐구자, 호기심 가득한 이론가",
    "ENTJ": "🚀🎯 리더, 목표 지향적이고 강한 추진력",
    "ENTP": "⚡💬 토론가, 창의적이고 즉흥적인 아이디어 뱅크",
    "INFJ": "🌌💖 이상주의자, 깊은 공감과 통찰력",
    "INFP": "🌿🎨 몽상가, 감성적이고 창의적인 영혼",
    "ENFJ": "🌟🤝 소통가, 따뜻하고 사람 중심적",
    "ENFP": "🔥🌈 열정가, 자유로운 영혼과 호기심",
    "ISTJ": "📋🏛️ 관리자, 체계적이고 신뢰할 수 있는 존재",
    "ISFJ": "🛡️💝 수호자, 헌신적이고 따뜻한 마음",
    "ESTJ": "⚙️📊 집행자, 현실적이고 조직적인 리더",
    "ESFJ": "🎉🤗 사교가, 친절하고 협력적인 사람",
    "ISTP": "🔧🕵️‍♂️ 장인, 실용적이고 침착한 문제 해결사",
    "ISFP": "🎸🌸 예술가, 감성적이고 조용한 아름다움",
    "ESTP": "🏎️🎯 활동가, 즉흥적이고 에너지 넘치는 행동파",
    "ESFP": "🎤🎊 연예인, 즐겁고 사교적인 분위기 메이커",
}

def mbti_button_grid(mbtis):
    st.write("본인의 MBTI를 선택해주세요!👇")
    cols = st.columns(4)
    selected = None
    for i, mbti in enumerate(mbtis):
        if cols[i % 4].button(mbti):
            selected = mbti
    return selected

def main():
    selected_mbti = mbti_button_grid(mbti_list)
    if selected_mbti:
        st.markdown(f"### 🎯 선택한 MBTI: **{selected_mbti}**")
        st.markdown(f"### 첫인상 이미지 느낌")
        st.markdown(f"#### {mbti_first_impression[selected_mbti]}")

if __name__ == "__main__":
    main()
