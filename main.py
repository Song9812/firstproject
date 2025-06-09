import streamlit as st

# MBTI 별 추천 영화 데이터
mbti_movies = {
    "INTJ": ["인셉션", "매트릭스", "셜록 홈즈"],
    "INTP": ["인터스텔라", "이터널 선샤인", "굿 윌 헌팅"],
    "ENTJ": ["소셜 네트워크", "울프 오브 월 스트리트", "킹스 스피치"],
    "ENTP": ["아이언맨", "빅쇼트", "캐치 미 이프 유 캔"],
    "INFJ": ["월터의 상상은 현실이 된다", "포레스트 검프", "그린북"],
    "INFP": ["업", "어바웃 타임", "라라랜드"],
    "ENFJ": ["죽은 시인의 사회", "러브 액츄얼리", "인사이드 아웃"],
    "ENFP": ["500일의 썸머", "위대한 쇼맨", "라이온 킹"],
    "ISTJ": ["셜록 홈즈", "다크 나이트", "헌터 킬러"],
    "ISFJ": ["원더", "패딩턴", "작은 아씨들"],
    "ESTJ": ["미션 임파서블", "터미네이터 2", "아폴로 13"],
    "ESFJ": ["맘마미아!", "러브 액츄얼리", "헬프"],
    "ISTP": ["본 아이덴티티", "존 윅", "매드 맥스"],
    "ISFP": ["월E", "캐롤", "콜 미 바이 유어 네임"],
    "ESTP": ["베이비 드라이버", "분노의 질주", "킹스맨"],
    "ESFP": ["위대한 개츠비", "셰프", "라라랜드"]
}

# Streamlit 앱 제목
st.title("🎬 MBTI 기반 명작 영화 추천기")

# 사용자 입력 받기
user_mbti = st.text_input("당신의 MBTI를 입력해주세요 (예: INFP)").upper()

# 유효성 검사 및 추천
if user_mbti:
    if user_mbti in mbti_movies:
        st.subheader(f"✨ {user_mbti} 추천 명작 영화:")
        for movie in mbti_movies[user_mbti]:
            st.write(f"- {movie}")
    else:
        st.warning("유효한 MBTI 16가지 중 하나를 입력해주세요. (예: INTJ, ENFP 등)")
