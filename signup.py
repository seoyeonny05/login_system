# idpass.txt를 읽음
lines = open("../idpass.txt", "r").readlines()
idlist = []
for i in range(len(lines)):
    # idpass.txt에 있는 아이디리스트에 저장
    if i % 3 == 0:
        idlist.append(lines[i].strip())

signed = False
# 아이디 중복시 무한 반복
while not signed:
    id = input("새로 만들 아이디를 입력하시오:")
    password1 = input("새로 만들 1차 비밀번호를 입력하시오:")
    # 이미 존재하는 아이디일 경우
    if id in idlist:
        print(f"{id} 는 중복된 아이디 입니다.")
    # 존재 하지 않는 아이디를 입력헸을 경우
    else:
        password2 = input("새로 만들 2차 비밀번호를 입력하시오:")
        f = open("../idpass.txt", "a")
        f.write(f"\n{id}\n{password1}\n{password2}")
        f.close()
        signed = True
