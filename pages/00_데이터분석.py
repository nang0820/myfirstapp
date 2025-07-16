import streamlit as st
import pandas as pd
import altair as alt
import os

# 제목
st.title("국가별 MBTI 유형 Top 3 시각화")

# 기본 파일 경로
default_file_path = "countriesMBTI_16types.csv"

# 파일 업로드
uploaded_file = st.file_uploader("MBTI 데이터 CSV 파일을 업로드하거나 건너뛰세요.", type="csv")

# 파일 선택 로직
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.info("업로드된 파일을 사용하고 있습니다.")
elif os.path.exists(default_file_path):
    df = pd.read_csv(default_file_path)
    st.info("기본 데이터를 사용하고 있습니다.")
else:
    st.error("CSV 파일을 업로드하거나 디렉토리에 'countriesMBTI_16types.csv'가 있어야 합니다.")
    st.stop()

# 국가 선택
countries = df['Country'].unique()
selected_country = st.selectbox("국가를 선택하세요:", countries)

# 선택 국가 데이터 추출 및 Top 3
country_data = df[df['Country'] == selected_country].iloc[0]
mbti_scores = country_data.drop('Country')
top3 = mbti_scores.sort_values(ascending=False).head(3).reset_index()
top3.columns = ['MBTI Type', 'Proportion']

# Altair 시각화
chart = alt.Chart(top3).mark_bar().encode(
    x=alt.X('MBTI Type', sort='-y'),
    y=alt.Y('Proportion', title='비율'),
    color=alt.Color('MBTI Type', legend=None),
    tooltip=['MBTI Type', alt.Tooltip('Proportion', format='.2%')]
).properties(
    width=500,
    height=400,
    title=f"{selected_country}의 MBTI 상위 3유형"
)

st.altair_chart(chart, use_container_width=True)
