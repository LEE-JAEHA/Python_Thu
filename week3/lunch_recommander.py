import random


print("점심 추천기 프로그램입니다.")

menus = list()
menus.append("갈비탕")
menus.append("떡볶이")
menus.append("오뎅")
menus.append("감자탕")
menus.append("김치찌개")
menus.append("제육볶음")
menus.append("김치볶음밥")
prices = [10000,7000,5000,8000,8000,7000,5000]


print("메뉴판")
print("="*20)
for index,value in enumerate(menus):
    print("{0:<10}{1:>10}{won}".format(value,prices[index],won="원"))
print("="*20)


choice = random.randrange(0,len(menus))
print("오늘의 메뉴 선택 : {0}".format(menus[choice]))
print("메뉴의 가격 : {0}".format(prices[choice]))










# import random
#
# print("점심 추천기 프로그램입니다.")
#
# menus =list()
# menus.append("갈비탕")
# menus.append("떡볶이")
# menus.append("오뎅")
# menus.append("감자탕")
# menus.append("김치찌개")
# menus.append("제육볶음")
# menus.append("김치볶읍밥")
# prices = [10000,7000,5000,8000,8000,7000,5000]
# # print("""
# # 메뉴판
# # =====================
# # {0:<10}{1:>10}{won}
# # {2:<10}{3:>10}{won}
# # {4:<10}{5:>10}{won}
# # {6:<10}{7:>10}{won}
# # {8:<10}{9:>10}{won}
# # {10:<10}{11:>10}{won}
# # {12:<10}{13:>10}{won}
# # =====================
# # """.format(menus[0],prices[0],menus[1],prices[1],menus[2],prices[2],menus[3],prices[3],
# # menus[4],prices[4],menus[5],prices[5],menus[6],prices[6],won="원"))
#
# print("메뉴판")
# print("================")
# for idx,value in enumerate(menus):
#     print("{0:<10}  {1:>10}{won}".format(value,prices[idx],won="원"))
#
#
#
#
# print("================")
#
#
#
#
#
#
#
#
# choice = random.randrange(0,len(menus))
# print("오늘의 메뉴 선택 : {0}".format(  menus[choice] )  )
# print("메뉴의 가격     : {0}".format( prices[choice] ) )
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
#
#
#
#
#
#
#
# # import random
# #
# # print("점심 추천입니다")
# # menus = list()
# # menus.append("갈비탕")
# # menus.append("떡볶이")
# # menus.append("오뎅")
# # menus.append("감자탕")
# # menus.append("김치찌개")
# # menus.append("제육볶음")
# # menus.append("김치볶읍밥")
# # prices = [10000,7000,5000,8000,8000,7000,5000]
# #
# # print("메뉴판")
# # print("==============")
# # for index,value in enumerate(menus):
# #     print("{0:<10}{1:>10}{won}".format(value,prices[index],won="원"))
# # print("==============")
# #
# #
# #
# # choice = random.randrange(0,len(menus))
# #
# # print("오늘의 메뉴 선택 : {0}".format(menus[choice]))
# # print("메뉴의 가격 : {0}".format(prices[choice]))
