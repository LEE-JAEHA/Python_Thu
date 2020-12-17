def pay_calculator():
    print("급여계산기")

    print("급여 계산기 프로그램입니다")
    pay = int(input("시급을 입력해주세요 : "))
    time_of_day = int(input("일일근무시간 : "))
    day_of_month= int(input("한달 근무 일수  : "))

    practice = input("""
    수습을 적용하나요?
    1. 적용
    2. 미적용
    """)





    practice=int(practice)
    profit = pay *time_of_day * day_of_month
    if practice == 1:
        practice_price = profit//10
    else:
        practice_price=0
    profit = profit - practice_price

    tax = input("""
    세금을 적용하나요??
    1. 미적용
    2. 4대 보험료 공제
    3. 소득세 공제
    4. 모두 적용
    """)

    if tax =='1':
        tax_price =0
    elif tax =='2':
        tax_price = profit * 841//1000
    elif tax =='3':
        tax_price = profit*33//1000
    elif tax =='4':
        tax_price= profit * 841//1000 + profit*33//1000


    profit = profit - tax_price

    print("예상 월급은?? : {0}".format(profit))


