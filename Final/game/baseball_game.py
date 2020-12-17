import random

def baseball_game():
    print("아구 게임 프로그램 입니다")


    answer = list()

    while len(answer)!=4:
        new_number = random.randrange(0,10)
        if new_number not in answer:
            answer.append(new_number)

    # print(answer)
    ##################################################
    strike = 0
    count =0
    while strike != 4 :
        count = count + 1
        your_answer = input("정답을 입력하세요  :  ")
        strike = 0
        ball = 0
        for index,value in enumerate(your_answer):
            if int(value) == answer[index]:
                strike = strike + 1
            elif int(value) in answer:
                ball = ball + 1

        if strike ==0 and ball == 0:
            print("out")
        else:
            print("{0} 스트라이크 {1} 볼입니다.".format(strike,ball))

    ######################################################
    print("{0}번 만에 끝내셨습니다.".format(count))
    print("정답은 : ",end="")
    for i in answer:
        print(i,end="")
    print()



