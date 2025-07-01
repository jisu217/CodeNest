import streamlit as st
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

# ✅ 한글 폰트 설정
import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic'  # Windows
matplotlib.rcParams['axes.unicode_minus'] = False

# DB 설정
DB_PATH = "서울시지하철복잡도.db"
TABLE_NAME = "서울교통공사_지하철혼잡도정보_20250331"

# DB에서 데이터 불러오기
@st.cache_data
def load_data():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query(f"SELECT * FROM {TABLE_NAME}", conn)
    conn.close()
    return df

df = load_data()
time_columns = [col for col in df.columns if "시" in col]

# 🎯 Streamlit 앱 시작
st.set_page_config(layout="wide")
st.title("🚇 서울시 지하철 시간대별 혼잡도 분석")

# 🔎 필터 선택
col1, col2 = st.columns(2)

with col1:
    selected_line = st.selectbox("호선을 선택하세요", sorted(df['호선'].unique()))

with col2:
    filtered_stations = df[df['호선'] == selected_line]['출발역'].unique()
    selected_station = st.selectbox("출발역을 선택하세요", sorted(filtered_stations))

# 데이터 필터링
subset = df[(df['호선'] == selected_line) & (df['출발역'] == selected_station)]

# 📈 그래프 출력
if not subset.empty:
    fig, ax = plt.subplots(figsize=(12, 5))
    for direction in subset['상하구분'].unique():
        row = subset[subset['상하구분'] == direction]
        ax.plot(time_columns, row.iloc[0][time_columns], label=f"{direction}")

    ax.set_title(f"{selected_line} {selected_station} 혼잡도 (상/하행)")
    ax.set_xlabel("시간대")
    ax.set_ylabel("혼잡도 (%)")
    ax.legend()
    ax.grid(True)
    plt.xticks(rotation=45)
    st.pyplot(fig)
else:
    st.warning("선택한 조건에 맞는 데이터가 없습니다.")
