str = "오늘은 날씨가 흐림"


words = str.split()  # ["오늘은", "날씨가", "흐림"]

position = words.index("흐림")
words[position] = "맑음"  # ["오늘은", "날씨가", "맑음"]

new_str = " ".join(words)  # "오늘은 날씨가 맑음"

print(new_str)  # "오늘은 날씨가 맑음"
