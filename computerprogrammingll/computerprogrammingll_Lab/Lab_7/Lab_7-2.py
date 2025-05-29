# 영화 리뷰 텍스트 중 일부를 전처리 과정
# 대문자 -> 소문자로 변환
# 태그, 특수문자 및 숫자 제거
# 불용어 중 'a', 'an', 'the' 제거

line = "One of the other reviewers has mentioned that after watching just 1 Oz episode you'll be hooked. \
They are right, as this is exactly what happened with me.<br /><br />The first thing that struck \
me about Oz was its brutality and unflinching scenes of violence, which set in right from the \
word GO. Trust me, this is not a show for the faint hearted or timid. This show pulls no punches \
with regards to drugs, sex or violence. Its is hardcore, in the classic use of the word.<br /><br \
/>It is called OZ as that is the nickname given to the Oswald Maximum Security State Penitentary. \
It focuses mainly on Emerald City, an experimental section of the prison where all the cells have \
glass fronts and face inwards, so privacy is not high on the agenda. Em City is home to \
many..Aryans, Muslims, gangstas, Latinos, Christians, Italians, Irish and more....so scuffles, \
death stares, dodgy dealings and shady agreements are never far away.<br /><br />I would say the \
main appeal of the show is due to the fact that it goes where other shows wouldn't dare. Forget \
pretty pictures painted for mainstream audiences, forget charm, forget romance...OZ doesn't mess \
around. The first episode I ever saw struck me as so nasty it was surreal, I couldn't say I was \
ready for it, but as I watched more, I developed a taste for Oz, and got accustomed to the high \
levels of graphic violence. Not just violence, but injustice (crooked guards who'll be sold out \
for a nickel, inmates who'll kill on order and get away with it, well mannered, middle class \
inmates being turned into prison bitches due to their lack of street skills or prison experience) \
Watching Oz, you may become comfortable with what is uncomfortable viewing....thats if you can \
get in touch with your darker side."
print(f"전처리 전 글자수:{len(line)}")

# 1) 대문자 -> 소문자로 변환
line = line.lower()

# 2) 태그, 특수문자 및 숫자 제거
clean_text = ""  # 전처리된 텍스트를 저장할 빈 문자열
inside_tag = False  # HTML 태그 내부 여부를 체크하기 위한 변수
# 한 글자씩 검사
for char in line:

    if char == '<':  # 태그의 시작을 찾으면
        inside_tag = True  # inside_tag를 True로 설정
    elif char == '>':  # 태그의 끝을 찾으면
        inside_tag = False  # inside_tag를 False로 설정
    elif not inside_tag and (char.isalpha() or char.isspace()):  # 태그 외부에서 알파벳인 경우
        clean_text += char  # clean_text에 해당 문자 추가

# 3) 불용어 제거
stopWords = ['a', 'an', 'the']  # 불용어 리스트
line = clean_text  # clean_text를 line에 저장 (지금은 clean_text가 태그와 숫자를 제거한 상태)
clean_text = ""  # 다시 clean_text를 초기화
# 띄어쓰기로 분리 후 한 단어씩 검사
for word in line.split():
    if not word in stopWords:  # 불용어가 아닐 경우
        clean_text += word + " "  # clean_text에 단어 추가

# 결과
# 전처리 후 글자 수를 출력
print(f"전처리 후 글자수:{len(clean_text)}")
print(clean_text)  # 최종 전처리된 텍스트 출력