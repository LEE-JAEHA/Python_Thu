from calculators.pay_calculator import pay_calculator
from calculators.grade_calculator import grade_calculate
from  calculators.obesity_calcultor import obesity
from calculators.normal_calculator import normal_calculate
from game.alligator_game import alligator_game
from game.pirate_game import pirate_game
from game.baseball_game import baseball_game
from game.baskinrobbins import baskin

if __name__ == "__main__":
    while True:
        print("""

----------------------------------
    어떤 프로그램을 실행하시겠습니까?
    1. 급여 계산기
    2. 학점 계산기
    3. 비만도 계산기
    4. 일반 사칙 연산 계산기
    5. 악어 이빨 게임
    6. 해적통 게임
    7. 야구 게임
    8. 베스킨 라빈스 게임
    9. 종료
----------------------------------
        """)
        choice = int(input("번호 입력 : "))
        if choice == 1:
            pay_calculator()
        elif choice == 2:
            grade_calculate()
        elif choice ==3:
            obesity()
        elif choice == 4:
            normal_calculate()
        elif choice == 5:
            alligator_game()
        elif choice == 6:
            pirate_game()
        elif choice == 7:
            baseball_game()
        elif choice == 8:
            baskin()
        elif choice == 9:
            print("종료!")
            break
        else:
            print("잘못된 입력입니다. 1~9 사이의 수를 입력해주세요.")


