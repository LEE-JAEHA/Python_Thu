import random
lotto = list()

while len(lotto)!=7:
    new_number = random.randrange(1,46)
    if new_number not in lotto:
        lotto.append(new_number)
    # lotto.append(random.randrange(1,46))

# print("""
# 랜덤 로또 발생기 입니다.
# 당첨번호 : {0} {1} {2} {3} {4} {5}
# 2등 보너스볼 : {6}
# """.format(lotto[0]))
print("랜덤 로또 발생기입니다.")
print("당첨 번호 : ",end="")
for index,value in enumerate(lotto):
    if index == len(lotto)-1:
        print("\n2등 보너스볼 : {0}".format(value))
    else:
        print(value,end = " ")








#
#
#
#
#
#
#
#
#
#
#
#
#
#
# print("로또 번호 출력입니다")
# lotto_numbers  =list()
#
# while len(lotto_numbers) < 7:
#     new_number = random.randrange(1,46)
#     if new_number not in lotto_numbers:
#         lotto_numbers.append(new_number)
#
# print("랜덤 로또 발생기 입니다")
# print("당첨 번호 : ",end="")
# for idx,value in enumerate(lotto_numbers):
#     if idx == len(lotto_numbers)-1:
#         print("\n2등 보너스볼 : {0}".format(value))
#     else:
#         print(value,end=" ")