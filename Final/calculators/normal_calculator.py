def calculate(choice, first, second):
    if choice == 1:
        print("결과값 : {0}".format(first + second))
    elif choice == 2:
        print("결과값 : {0}".format(first - second))
    elif choice == 3:
        print("결과값 : {0}".format(first * second))
    elif choice == 4:
        print("결과값 : {0}".format(first // second))
    elif choice == 5:
        print("결과값 : {0}".format(first / second))
    elif choice == 6:
        print("결과값 : {0}".format(first % second))

def normal_calculate():
    while True:
        a = int(input("계산할 첫번째 값을 입력해주세요 : "))
        b = int(input("계산할 두번쨰 값을 입력해주세요 : "))

        print("""
            원하는 연산을 선택하세요.
            1. 더하기
            2. 빼기
            3. 곱하기
            4. 정수 나누기
            5. 실수 나누기
            6. 나머지 구하기
            7. 계산 종료
        """)
        choice = int(input("어떤 번호를 선택하시겠습니까? : "))
        if choice < 0 or choice > 7:
            print("잘못된 입력입니다. 다시 입력해주세요")
        elif choice == 7:
            print("종료하겠습니다.")
            break
        else:
            calculate(choice, a, b)


