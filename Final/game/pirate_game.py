import random
def print_pirate(status):
    print('''
             ---------
            |+++++++++|
            ___________
            |  O   @  |
            |    o    |
             ---===---
               |   |
        ---------------------
        | {0} | {1} | {2} | {3} |
      --------------------------
      | {4} | {5} | {6} | {7} | {8} |
      --------------------------
      | {9} | {10} | {11} | {12} | {13} |   
      --------------------------
        | {14} | {15} | {16} | {17} |
        ---------------------
    '''.format(status[0], status[1], status[2], status[3], status[4],
               status[5], status[6], status[7], status[8], status[9],
               status[10], status[11], status[12], status[13], status[14],
               status[15], status[16], status[17], ))


def pirate_game():
    print("해적통 게임 프로그램입니다!")

    # 상태 초기화
    status = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18"]

    bomb = random.randrange(1,19)
    # print("벌칙 수 : {0}".format(bomb))
    check = list()
    while True:
        my_number = int(input("어디에 꽂을 건가요? : "))
        if my_number <0 or my_number >18:
            print("잘못 입력하였습니다. 다시 입력해주세요!!")
            # continue # continue를 만나게 되면 반복문 맨처음으로 돌아감
        if my_number in check:
            print("이미 꽂은 부분입니다. 다시 입력해주세요")
            continue
        elif my_number == bomb:
            print("걸렸습니다.")
            status[my_number - 1] = "X"
            break
        elif my_number != bomb :
            check.append(my_number)
            status[my_number-1]="X"
            print("휴 통과")
            print_pirate(status)



