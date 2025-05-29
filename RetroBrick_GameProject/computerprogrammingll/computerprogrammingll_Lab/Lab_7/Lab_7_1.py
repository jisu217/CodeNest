# 파일 이름을 입력받아 이름과 확장자 구분하여 출력
# 파일 이름에 "."가 두 개 이상 있을 수 있음 (최소 한 개는 있음)
# 확장자는 몇 글자인지 정해져 있지 않음

ok = True

while ok :
    # 사용자 입력
    filename = input("파일명:")

    # 확장자 검사
    # 조건식 순서 중요
    if filename.count('.') < 1 or len(filename[filename.rfind('.')+1:]) <= 0 : # filename.rfind('.'):문자열 filename에서 가장 마지막 .의 위치를 찾기
        print("확장자가 없습니다.")

    else : # 다 통과하면 반복문 종료
        ok = False
idx = filename.rindex('.')
print(f"\n파일명:{filename[:idx]}")
print(f"확장자:{filename[idx+1:]}")