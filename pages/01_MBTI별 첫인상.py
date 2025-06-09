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

# MBTI별 이미지 URL (인물 일러스트)
mbti_image_urls = {
    "INTJ": "https://www.urbanbrush.net/wp-content/uploads/2022/09/mbti-intj-%EC%9D%BC%EB%9F%AC%EC%8A%A4%ED%8A%B8-ai-%EB%8B%A4%EC%9A%B4%EB%A1%9C%EB%93%9C-download-mbti-intj-vector-500x500.jpg",
    "INTP": "https://www.urbanbrush.net/wp-content/uploads/2022/09/mbti-intp-%EC%9D%BC%EB%9F%AC%EC%8A%A4%ED%8A%B8-ai-%EB%8B%A4%EC%9A%B4%EB%A1%9C%EB%93%9C-download-mbti-intp-vector-500x500.jpg",
    "ENTJ": "https://www.urbanbrush.net/wp-content/uploads/2022/09/mbti-entj-%EC%9D%BC%EB%9F%AC%EC%8A%A4%ED%8A%B8-ai-%EB%8B%A4%EC%9A%B4%EB%A1%9C%EB%93%9C-download-mbti-entj-vector-500x500.jpg",
    "ENTP": "https://www.urbanbrush.net/wp-content/uploads/2022/09/mbti-entp-%EC%9D%BC%EB%9F%AC%EC%8A%A4%ED%8A%B8-ai-%EB%8B%A4%EC%9A%B4%EB%A1%9C%EB%93%9C-download-mbti-entp-vector-500x500.jpg",
    "INFJ": "https://www.urbanbrush.net/wp-content/uploads/2022/09/mbti-infj-%EC%9D%BC%EB%9F%AC%EC%8A%A4%ED%8A%B8-ai-%EB%8B%A4%EC%9A%B4%EB%A1%9C%EB%93%9C-download-mbti-infj-vector-500x500.jpg",
    "INFP": "https://www.urbanbrush.net/wp-content/uploads/2022/09/mbti-infp-%EC%9D%BC%EB%9F%AC%EC%8A%A4%ED%8A%B8-ai-%EB%8B%A4%EC%9A%B4%EB%A1%9C%EB%93%9C-download-mbti-infp-vector-500x500.jpg",
    "ENFJ": "https://www.urbanbrush.net/wp-content/uploads/2022/09/mbti-enfj-%EC%9D%BC%EB%9F%AC%EC%8A%A4%ED%8A%B8-ai-%EB%8B%A4%EC%9A%B4%EB%A1%9C%EB%93%9C-download-mbti-enfj-vector-500x500.jpg",
    "ENFP": "https://www.urbanbrush.net/wp-content/uploads/2022/09/mbti-enfp-%EC%9D%BC%EB%9F%AC%EC%8A%A4%ED%8A%B8-ai-%EB%8B%A4%EC%9A%B4%EB%A1%9C%EB%93%9C-download-mbti-enfp-vector-500x500.jpg",
    "ISTJ": "https://www.urbanbrush.net/wp-content/uploads/2022/09/mbti-istj-%EC%9D%BC%EB%9F%AC%EC%8A%A4%ED%8A%B8-ai-%EB%8B%A4%EC%9A%B4%EB%A1%9C%EB%93%9C-download-mbti-istj-vector-500x500.jpg",
    "ISFJ": "https://www.urbanbrush.net/wp-content/uploads/2022/09/mbti-isfj-%EC%9D%BC%EB%9F%AC%EC%8A%A4%ED%8A%B8-ai-%EB%8B%A4%EC%9A%B4%EB%A1%9C%EB%93%9C-download-mbti-isfj-vector-500x500.jpg",
    "ESTJ": "https://www.urbanbrush.net/wp-content/uploads/2022/09/mbti-estj-%EC%9D%BC%EB%9F%AC%EC%8A%A4%ED%8A%B8-ai-%EB%8B%A4%EC%9A%B4%EB%A1%9C%EB%93%9C-download-mbti-estj-vector-500x500.jpg",
    "ESFJ": "https://www.urbanbrush.net/wp-content/uploads/2022/09/mbti-esfj-%EC%9D%BC%EB%9F%AC%EC%8A%A4%ED%8A%B8-ai-%EB%8B%A4%EC%9A%B4%EB%A1%9C%EB%93%9C-download-mbti-esfj-vector-500x500.jpg",
    "ISTP": "https://www.urbanbrush.net/wp-content/uploads/2022/09/mbti-istp-%EC%9D%BC%EB%9F%AC%EC%8A%A4%ED%8A%B8-ai-%EB%8B%A4%EC%9A%B4%EB%A1%9C%EB%93%9C-download-mbti-istp-vector-500x500.jpg",
    "ISFP": "https://www.urbanbrush.net/wp-content/uploads/2022/09/mbti-isfp-%EC%9D%BC%EB%9F%AC%EC%8A%A4%ED%8A%B8-ai-%EB%8B%A4%EC%9A%B4%EB%A1%9C%EB%93%9C-download-mbti-isfp-vector-500x500.jpg",
    "ESTP": "https://www.urbanbrush.net/wp-content/uploads/2022/09/mbti-estp-%EC%9D%BC%EB%9F%AC%EC%8A%A4%ED%8A%B8-ai-%EB%8B%A4%EC%9A%B4%EB%A1%9C%EB%93%9C-download-mbti-estp-vector-500x500.jpg",
    "ESFP": "https://www.urbanbrush.net/wp-content/uploads/2022/09/mbti-esfp-%EC%9D%BC%EB%9F%AC%EC%8A%A4%ED%8A%B8-ai-%EB%8B%A4%EC%9A%B4%EB%A1%9C%EB%93%9C-download-mbti-esfp-vector-500x500.jpg",
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
        st.image(mbti_image_urls[selected_mbti], caption=f"{selected_mbti} 이미지", use_column_width=True)

if __name__ == "__main__":
    main()
