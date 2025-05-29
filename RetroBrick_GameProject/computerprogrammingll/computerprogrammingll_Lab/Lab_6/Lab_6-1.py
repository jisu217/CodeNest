# 다음 문자열 sentence에서 각 알파벳 문자들의 빈도수를 구하는 프로그램 작성
# 공백 문자, 탭 문자, 줄바꿈 문자, 마침표나 따옴표, 콤마 같은 특수 문자의 개수도 각각 센다
# 화면에 출력할 수 없는 공백 문자는 SPACE, 탭 문자는 TAB, 줄바꿈 문자는 NEWLINE으로 출력하고 개수 출력

sentences = """lorem ipsum dolor sit amet,
consectetuer adipiscing elit.
maecenas porttitor congue massa.
fusce posuere, magna sed pulvinar ultricies, purus
lectus malesuada libero, sit
amet commodo magna eros quis urna.
nunc viverra imperdiet enim.
"""

# 빈 셔너리 생성
d = {}

for s in sentences:
    if s in d: # 각 글자들이 딕셔너리에 있는지 확인
        d[s] += 1 #1 증가
    else:
        d[s] = 1 #1로 초기화

for k, v in d. items ():

   # 임시로 key값을 다르게 출력
   if k == ' ':
        k = "SPACE"
   elif k == '\t' :
       K = "TAR"
   elif k == '\n' :
       K = "NEWLINE"
   print(f"{k}:{v}") # 결과 출력
