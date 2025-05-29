# 게임 설정 파일

# 파일 읽기
con = open(".//res//config.txt","r")
conFile = con.readlines() # 파일 전체의 내용을 리스트로 만듦
con. close()

# 사용자 입력 현재 상태도 보여줌
HP_warning = input("HP영곡표시(0~100)\t협재상태:"+conFile[0]+":")
HP_warning = input("HP영곡표시(0~100)\t협재상태:"+conFile[1]+":")
autoChat = input("1.수동\n2,천천히\n3,빠르게\n대화자동진행\t현재상태:"+conFile[2]+":")
autoBattle = input("자동 이동, 전투(ON:1/OFF:0)\t현재상태:"+conFile[3]+":")
autoQuest = input("다음 퀘스트 자동진행(ON:1/OFF:0)\t현재상태:"+conFile[4]+":")
showlnfo = input("캐릭터 터치하여 정보보기(ON:1/OFF:0)\t현재상태:"+conFile[5]+":")

#파일 쓰기
con = open(".//res//config.txt","w")
con.write( "HP_warning="+HP_warning+"\n")
con.write( "HP_warning="+HP_warning+"\n")
con.write( "autoChat="+autoChat+"\n")
con.write( "autoBattle="+autoBattle+"\n")
con.write( "autoQuest="+autoQuest+"\n")
con.write( "showlnfo="+showlnfo+"\n")
con.close()