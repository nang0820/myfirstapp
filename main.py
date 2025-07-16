import streamlit as st

# --- 애니 정보: 제목, 이미지 URL, 설명 ---
anime_info = {
    "데스노트": {
        "img": "https://upload.wikimedia.org/wikipedia/en/6/6f/Death_Note_Vol_1.jpg",
        "desc": "죽은 자의 이름을 적으면 죽게 되는 노트를 가진 천재 고등학생의 이야기."
    },
    "코드기어스": {
        "img": "https://upload.wikimedia.org/wikipedia/en/3/3b/Code_Geass_DVD.jpg",
        "desc": "천재 소년이 가면을 쓰고 제국에 반기를 드는 전략 서사물."
    },
    "사이코패스": {
        "img": "https://upload.wikimedia.org/wikipedia/en/7/76/Psycho-Pass_key_visual.jpg",
        "desc": "사람의 정신 상태를 수치화해 범죄를 예측하는 미래 사회의 딜레마."
    },
    "슈타인즈 게이트": {
        "img": "https://upload.wikimedia.org/wikipedia/en/5/57/SteinsGate.jpg",
        "desc": "시간을 조작하게 된 청년들의 이야기, SF와 감동의 조화."
    },
    "모브사이코 100": {
        "img": "https://upload.wikimedia.org/wikipedia/en/2/2e/Mob_Psycho_100_key_visual.jpg",
        "desc": "엄청난 초능력을 가진 평범한 소년의 성장기."
    },
    "하이큐!!": {
        "img": "https://upload.wikimedia.org/wikipedia/en/2/2e/Haikyu_season1_cover.png",
        "desc": "배구에 모든 것을 건 소년들의 열정과 성장 이야기."
    },
    "진격의 거인": {
        "img": "https://upload.wikimedia.org/wikipedia/en/f/f5/Attack_on_Titan_S1_DVD.jpg",
        "desc": "거인과 인간의 전쟁, 숨겨진 진실을 파헤치는 이야기."
    },
    "너의 이름은": {
        "img": "https://upload.wikimedia.org/wikipedia/en/0/0b/Your_Name_poster.png",
        "desc": "서로 몸이 바뀐 두 소년소녀의 운명적 만남과 시간 여행 로맨스."
    },
    "클라나드": {
        "img": "https://upload.wikimedia.org/wikipedia/en/b/b7/Clannad_game_cover.jpg",
        "desc": "삶과 가족, 사랑에 대한 감성적인 이야기."
    },
    "스파이 패밀리": {
        "img": "https://upload.wikimedia.org/wikipedia/en/0/0b/Spy_x_Family_manga_volume_1.jpg",
        "desc": "정체를 숨긴 스파이 가족의 코믹한 일상."
    },
    "명탐정 코난": {
        "img": "https://upload.wikimedia.org/wikipedia/en/8/84/Detective_Conan_vol_1.jpg",
        "desc": "어린이의 모습이 된 천재 고등학생 탐정의 미스터리 해결기."
    },
    "나의 히어로 아카데미아": {
        "img": "https://upload.wikimedia.org/wikipedia/en/9/9d/My_Hero_Academia_Volume_1.png",
        "desc": "개성을 가진 사회에서 영웅을 꿈꾸는 소년의 성장기."
    }
    # 필요 시 더 추가 가능
}

# --- MBTI별 애니메이션 추천 데이터 ---
mbti_anime_dict = {
    "INTJ": ["데스노트", "코드기어스", "사이코패스"],
    "INTP": ["슈타인즈 게이트", "모브사이코 100", "하이큐!!"],
    "ENTJ": ["진격의 거인", "하이큐!!", "명탐정 코난"],
    "INFJ": ["너의 이름은", "클라나드", "사이코패스"],
    "ENFP": ["스파이 패밀리", "슈타인즈 게이트", "나의 히어로 아카데미아"]
    # 다른 유형도 원하면 계속 추가할 수 있음
}

# --- 앱 설정 ---
st.set_page_config(page_title="MBTI 애니 추천기", page_icon="🌸")
st.title("🌸 MBTI 애니메이션 추천기")
st.write("당신의 MBTI를 선택하면, 잘 맞을 것 같은 애니메이션을 추천해드릴게요!")

# --- MBTI 선택 ---
mbti_types = list(mbti_anime_dict.keys())
selected_mbti = st.selectbox("당신의 MBTI를 선택해주세요 👇", [""] + mbti_types)

# --- 추천 결과 출력 ---
if selected_mbti:
    st.markdown(f"### 🌟 {selected_mbti} 유형이 좋아할 만한 애니메이션 추천:")

    for anime in mbti_anime_dict[selected_mbti]:
        info = anime_info.get(anime)
        if info:
            st.image(info["img"], width=200)
            st.markdown(f"**{anime}**  
            {info['desc']}")
            st.markdown("---")
        else:
            st.markdown(f"**{anime}** - 이미지/설명 없음")
    
    st.success("좋은 감상 되세요! ✨")
else:
    st.info("먼저 MBTI를 선택해주세요 :)")
