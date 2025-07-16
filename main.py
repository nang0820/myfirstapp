import streamlit as st
import random

# --- 이모지 리스트 ---
emoji_list = ["🎬", "✨", "🌟", "🍿", "🎞️", "💫", "🎥", "📺", "😸", "🌸"]

# --- MBTI별 애니 추천 리스트 ---
mbti_anime_dict = {
    "INTJ": ["데스노트", "코드기어스", "사이코패스"],
    "INTP": ["슈타인즈 게이트", "모브사이코 100", "하이큐!!"],
    "ENTJ": ["진격의 거인", "헌터x헌터", "도쿄구울"],
    "ENTP": ["원피스", "노 게임 노 라이프", "은혼"],
    "INFJ": ["너의 이름은", "비올렛 에버가든", "이누야샤"],
    "INFP": ["클라나드", "4월은 너의 거짓말", "날씨의 아이"],
    "ENFJ": ["강철의 연금술사", "나의 히어로 아카데미아", "페어리 테일"],
    "ENFP": ["스파이 패밀리", "오란고교 호스트부", "카케구루이"],
    "ISTJ": ["명탐정 코난", "강철의 연금술사", "유희왕"],
    "ISFJ": ["너에게 닿기를", "마루코는 아홉살", "슬램덩크"],
    "ESTJ": ["하이큐!!", "쿠로코의 농구", "블리치"],
    "ESFJ": ["사랑은 비가 갠 뒤처럼", "나츠메 우인장", "하야테처럼!"],
    "ISTP": ["토라도라!", "아인", "소드 아트 온라인"],
    "ISFP": ["요르문간드", "일상", "하나야마타"],
    "ESTP": ["건담 시리즈", "도쿄 리벤저스", "베르세르크"],
    "ESFP": ["러브라이브!", "케이온!", "아이돌마스터"]
}

# --- 앱 기본 설정 ---
st.set_page_config(page_title="MBTI 애니 추천기", page_icon="🌸")
st.title("🌸 MBTI 애니메이션 추천기")
st.write("당신의 MBTI를 선택하면, 잘 맞을 것 같은 애니메이션을 추천해드릴게요!")

# --- MBTI 선택 위젯 ---
mbti_types = list(mbti_anime_dict.keys())
selected_mbti = st.selectbox("당신의 MBTI를 선택해주세요 👇", [""] + mbti_types)

# --- 추천 결과 출력 ---
if selected_mbti:
    st.markdown(f"### 🌟 {selected_mbti} 유형이 좋아할 만한 애니 추천:")

    for anime in mbti_anime_dict[selected_mbti]:
        emoji = random.choice(emoji_list)
        st.markdown(f"- {emoji} {anime}")

    st.balloons()  # 🎈 풍선 효과
    st.success("좋은 감상 되세요! 🎉")
else:
    st.info("먼저 MBTI를 선택해주세요 😊")
