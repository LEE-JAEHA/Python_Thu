print("해적통 게임 프로그램입니다!")

# 상태 초기화
status = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18"]


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
           status[15], status[16], status[17],))