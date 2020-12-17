def grade_calculate():
    grade_point=0
    print("학점 계산기 프로그램입니다.")
    subject = input("과목명을 입력해주세요 : ")
    credit = input("학점(1,2,3학점)을 입력해주세요 : ")
    grade = input("성적을 입력해주세요 (A+,B0,C-,F...) : ")#3학점 2학점 1학점 같은

    calculating_way = int(input("""
    학점 계산 방식을 선택해주세요.
    1. 4.5 만점
    2. 4.3 만점
    """))

    if calculating_way == 1:
        print("4.5만점입니다.")
        if grade == 'A+':
            grade_point = 4.5
        elif grade =='A0':
            grade_point = 4.0
        elif grade =='B+':
            grade_point = 3.5
        elif grade =='B0':
            grade_point = 3.0
        elif grade =='C+':
            grade_point = 2.5
        elif grade =='C0':
            grade_point = 2.0
        elif grade =='D+':
            grade_point = 1.5
        elif grade =='D0':
            grade_point = 1.0
        elif grade =='F':
            grade_point = 0
        else:
            print("input 에러입니다.정확한 값을 넣어주세요")

    elif calculating_way ==2:
        print("4.3만점입니다.")
        if grade == 'A+':
            grade_point = 4.3
        elif grade =='A0':
            grade_point = 4.0
        elif grade =='A-':
            grade_point = 3.7
        elif grade =='B+':
            grade_point = 3.3
        elif grade =='B0+':
            grade_point = 3.0
        elif grade =='B-':
            grade_point = 2.7
        elif grade =='C+':
            grade_point = 2.3
        elif grade =='C0':
            grade_point = 2.0
        elif grade =='C-':
            grade_point = 1.7
        elif grade == 'F':
            grade_point = 0.0
        else:
            print("input 에러입니다.정확한 값을 넣어주세요")
    else:
        print("1이나 2를 입력해주세요. 프로그램 종료")


    print("""
    과목명 : {0}
    성적 : {1}
    변환학점 : {2}
    취득학점 : {3}
    """.format(subject,grade,grade_point,credit))













    #
    # calculating_way= input("""
    # 학점 계산 방식을 선택해주세요
    # 1. 4.5 만점
    # 2. 4.3 만점
    # """)
    #
    # grade_point = 0
    #
    # if calculating_way == '1':
    #     pass
    # elif calculating_way == '2':
    #     pass
    # else:
    #     print("1이나 2를 입력해주세요. 프로그램 종료")
    #
    # if calculating_way == '1':
    #     if grade =='A+':
    #         grade_point = 4.5
    #     elif grade =='A0':
    #         grade_point = 4.0
    #     elif grade =='B+':
    #         grade_point = 3.5
    #     elif grade == 'B0':
    #         grade_point = 3.0
    #     elif grade =='C+':
    #         grade_point = 2.0
    #
    #
    # print("""
    # 과목명 : {0}
    # 성적  : {1}
    # 변환학점 : {2}
    # 취득학점 : {3}
    # """.format(subject,grade,grade_point,credit))