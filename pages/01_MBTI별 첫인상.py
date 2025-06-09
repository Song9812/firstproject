import streamlit as st

st.set_page_config(page_title="✨ MBTI 첫인상 이미지", layout="centered")

st.title("✨ MBTI별 첫인상 이미지 서비스")
st.write("아래 버튼에서 본인의 MBTI를 선택하면, MBTI별 첫인상 이미지를 보여드립니다!")

mbti_list = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

# MBTI별 이미지 URL (예시 URL이므로 실제 이미지 URL로 교체하세요)
mbti_image_urls = {
    "INTJ": "https://i.imgur.com/0aP4kHq.png",
    "INTP": "https://i.imgur.com/tQmMEph.png",
    "ENTJ": "https://i.imgur.com/NmY6Q6T.png",
    "ENTP": "https://i.imgur.com/gEXR8kE.png",
    "INFJ": "https://i.imgur.com/EGQZpma.png",
    "INFP": "https://i.imgur.com/LZxREuk.png",
    "ENFJ": "https://i.imgur.com/0X0m2Ti.png",
    "ENFP": "https://i.imgur.com/rX7ZLkP.png",
    "ISTJ": "https://i.imgur.com/4ZQ2hO1.png",
    "ISFJ": "https://i.imgur.com/WYRcqAp.png",
    "ESTJ": "https://i.imgur.com/dQG1xqE.png",
    "ESFJ": "https://i.imgur.com/Xy2xlbL.png",
    "ISTP": "https://i.imgur.com/j4kKxUY.png",
    "ISFP": "https://i.imgur.com/f3c7xEb.png",
    "ESTP": "https://i.imgur.com/4K7Tl1K.png",
    "ESFP": "https://i.imgur.com/MgqDHXv.png",
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
        st.write("아래는 이 MBTI의 첫인상을 표현한 이미지입니다.")
        img_url = mbti_image_urls.get(selected_mbti)
        if img_url:
            st.image(img_url, caption=f"{selected_mbti} 첫인상", use_column_width=True)
        else:
            st.write("이미지 URL이 없습니다.")

if __name__ == "__main__":
    main()
