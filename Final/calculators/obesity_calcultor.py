def obesity():
    print("비만도 계산기 프로그램입니다.")
    print("""
    성별이 어떻게 되십니까?
    1. 남자
    2. 여자
    """)
    sex = input("성별 입력 (1/2) : ")

    h = int(input("신장을 입력해주세요 : "))
    w = int(input("체중을 입력해주세요 : "))
    age = int(input("나이를 입력해주세요 : "))

    bmi = w / ( (h/100) * (h/100))

    print("당신의 BMI 수치는 {0} 입니다.".format(bmi))

    if bmi < 20:
        print("저체중입니다.")
    elif bmi <24:
        print("정상입니다.")
    elif bmi < 29:
        print("과체중입니다.")
    else:
        print("비만입니다.")
