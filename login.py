def start_login():
    lines = open("idpass.txt", "r").read().splitlines()

    try_number = 5
    login = True

    # 로그인 여부
    while login:
        login_text = input("로그인 하시겠습니까?")

        # 로그인 여부 묻기에 yes 시, 아이디및 비밀번호를 묻는 단계
        if login_text == "yes":
            id_text = input("아이디를 입력하시오:")
            pass1 = input("비밀번호를 입력하시오:")

            # 아이디 입력 코드
            if lines[0] == id_text:

                # 1차 비밀번호 입력 코드
                if lines[1] == pass1:
                    pass2 = input("1차 합격\n2차 비밀번호를 입력하시오:")

                    # 1차 비밀번호 입력 후 2차 비밀번호로그인 입력 코드 ( 2차 비밀번호 로그인시 그 즉시 중지 )
                    if lines[2] == pass2:
                        print("로그인 되었습니다")
                        break
                    else:
                        print("2차 비밀번호 틀렸습니다")

                # 비밀번호 입력 실패시 횟수가 줄어드는 코드
                else:
                    try_number = try_number - 1
                    print(f"1차 비밀번호를 틀렸습니다.\n남은 횟수 {try_number} 남았습니다")

            # 로그인 실패시
            else:
                print("그런 아이디 없습니다")

        # 로그인시 no로 대답하면 bye라고 인사하는 코드
        elif login_text == "no":
            login = False
            print("bye")

        # 로그인 보기를 주는 코드
        else:
            print("yes no 로만 대답하세요")

        # 로그인 할당량을 초과를 나타내는 코드
        if try_number == 0:
            login = False
            print("당신은 침입자 입니다.")


def haha():
    print("haha")
