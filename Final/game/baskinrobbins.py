import random
def br_counter(count,br):
    for i in range(count):
        br = br + 1
        print("{0}".format(br))
        if br == 31:
            break
    return br


def baskin():
    print("베스킨 라빈스 31 게임입니다.")
    while True:
        order = input("누가 먼저 시작하나요? (0 : 후공 / 1 : 선공) : ")
        if order in ['0','1']:
            order = int(order)
            break
        else:
            print("잘못된 입력입니다.")

    BR = 0
    turn = 1

    while BR < 31:
        if turn % 2 == order:
            print("사용자 차례")
            while True:
                count = int(input("몇 개를 말할까요? : "))
                if count ==1 or count ==2 or count == 3:
                    break
                else:
                    print("잘못된 입력입니다. (1~3 사이의 수를 입력해주세요)")
            # for i in range(count):
            #     BR = BR +1
            #     print("사용자 : {0}".format(BR))
            #     if BR == 31:
            #         print("사용자 졌습니다.")
            #         break
            BR = br_counter(count,BR)

        else:
            print("컴퓨터 차례")
            count = random.randrange(1,4)
            for i in range(count):
                BR += 1
                print("컴퓨터 : {0}".format(BR))
                if BR == 31:
                    print("컴퓨터가 졌습니다.")
                    break
        turn = turn + 1

    if turn % 2 == order:
        print("사용자가 이겼습니다.")
    else:
        print("사용자가 졌습니다.")

