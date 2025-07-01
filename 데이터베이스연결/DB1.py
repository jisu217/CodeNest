import sqlite3
import pandas as pd
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Malgun Gothic'  # Windows 한글 폰트
plt.rcParams['axes.unicode_minus'] = False     # 마이너스 부호 깨짐 방지

# DB 파일과 테이블명
DB_PATH = "서울시지하철복잡도.db"
TABLE_NAME = "서울교통공사_지하철혼잡도정보_20250331"

# DB에서 데이터 불러오기
conn = sqlite3.connect(DB_PATH)
df = pd.read_sql_query(f"SELECT * FROM {TABLE_NAME}", conn)
conn.close()

# 시간대 컬럼 추출
time_columns = [col for col in df.columns if "시" in col]

# GUI 시작
root = tk.Tk()
root.title("🚇 서울시 지하철 혼잡도 시각화 (DB 기반)")
root.geometry("1000x700")

# 필터 프레임
frame = tk.Frame(root)
frame.pack(pady=20)

tk.Label(frame, text="호선 선택:").grid(row=0, column=0, padx=5)
tk.Label(frame, text="출발역 선택:").grid(row=0, column=2, padx=5)

# 콤보박스: 호선
lines = sorted(df['호선'].unique())
selected_line = tk.StringVar()
line_cb = ttk.Combobox(frame, textvariable=selected_line, values=lines, state="readonly")
line_cb.grid(row=0, column=1)

# 콤보박스: 출발역
selected_station = tk.StringVar()
station_cb = ttk.Combobox(frame, textvariable=selected_station, state="readonly")
station_cb.grid(row=0, column=3)

# 호선 선택 시 출발역 필터링
def update_stations(event):
    stations = sorted(df[df['호선'] == selected_line.get()]['출발역'].unique())
    station_cb['values'] = stations
    if stations:
        station_cb.set(stations[0])
line_cb.bind("<<ComboboxSelected>>", update_stations)

# 그래프 출력
def plot_data():
    line = selected_line.get()
    station = selected_station.get()
    subset = df[(df['호선'] == line) & (df['출발역'] == station)]

    if subset.empty:
        return

    fig, ax = plt.subplots(figsize=(10, 4))
    for direction in subset['상하구분'].unique():
        row = subset[subset['상하구분'] == direction]
        ax.plot(time_columns, row.iloc[0][time_columns], label=direction)

    ax.set_title(f"{line} - {station} 시간대별 혼잡도")
    ax.set_ylabel("혼잡도 (%)")
    ax.set_xlabel("시간대")
    ax.legend()
    ax.grid(True)
    plt.xticks(rotation=45)

    # 이전 그래프 제거
    for widget in canvas_frame.winfo_children():
        widget.destroy()
    canvas = FigureCanvasTkAgg(fig, master=canvas_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

# 실행 버튼
tk.Button(root, text="혼잡도 그래프 보기", command=plot_data, bg="lightblue", font=("Arial", 12)).pack(pady=10)

# 그래프 출력 영역
canvas_frame = tk.Frame(root)
canvas_frame.pack(fill=tk.BOTH, expand=True)

# GUI 실행
root.mainloop()
