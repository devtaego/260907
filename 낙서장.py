import random


# ========================================
# 데이터를 저장할 리스트
# ========================================

# 업앤다운 게임 결과
# 리스트 안에 딕셔너리를 저장
players = []

# 예시
# [
#     {"name": "철수", "시도횟수": 5},
#     {"name": "영희", "시도횟수": 3}
# ]


# 로또 번호 과거 이력
# 리스트 안에 리스트를 저장 → 2차원 리스트
lotto_history = []

# 예시
# [
#     [1, 5, 10, 20, 30, 40],
#     [2, 7, 15, 22, 35, 44]
# ]


# ========================================
# 전체 프로그램 실행
# ========================================

while True:

    print()
    print("==========================")
    print("       게임 프로그램")
    print("==========================")
    print("1. 모드 선택")
    print("2. 결과 보기")
    print("3. 프로그램 종료")

    main_menu = input("메뉴를 선택하세요 : ")


    # ====================================
    # 1. 모드 선택
    # ====================================

    if main_menu == "1":

        print()
        print("[ 모드 선택 ]")
        print("1. 업앤다운 게임")
        print("2. 로또 번호 추출")

        mode = input("모드를 선택하세요 : ")


        # =================================
        # 1-1. 업앤다운 게임
        # =================================

        if mode == "1":

            print()
            print("[ 난이도 선택 ]")
            print("1. 쉬움   : 1 ~ 50")
            print("2. 중간   : 1 ~ 100")
            print("3. 어려움 : 1 ~ 200")

            level = input("난이도를 선택하세요 : ")


            # 난이도에 따라 최대 숫자 결정
            if level == "1":
                max_number = 50

            elif level == "2":
                max_number = 100

            elif level == "3":
                max_number = 200

            else:
                print("잘못된 난이도입니다.")
                continue


            # ---------------------------------
            # 사용자 이름 입력
            # ---------------------------------

            name = input("이름을 입력하세요 : ")


            # ---------------------------------
            # 정답 생성
            # ---------------------------------

            answer = random.randint(1, max_number)

            count = 0


            print()
            print("업앤다운 게임을 시작합니다.")
            print("1부터", max_number, "사이의 숫자를 맞혀보세요.")


            # ---------------------------------
            # 게임 반복
            # ---------------------------------

            while True:

                number = int(input("숫자 입력 : "))

                # 시도횟수 증가
                count += 1


                if number > answer:
                    print("DOWN!")


                elif number < answer:
                    print("UP!")


                else:
                    print()
                    print("정답입니다!")
                    print("시도횟수 :", count)
                    break


            # ---------------------------------
            # 사용자 결과를 딕셔너리로 생성
            # ---------------------------------

            player = {
                "name": name,
                "시도횟수": count
            }


            # 리스트 안에 딕셔너리 저장
            players.append(player)

            print("게임 결과가 저장되었습니다.")


        # =================================
        # 1-2. 로또 번호 추출
        # =================================

        elif mode == "2":

            lotto = []


            # 숫자 6개가 들어갈 때까지 반복
            while len(lotto) < 6:

                number = random.randint(1, 45)


                # 중복 번호가 아닐 경우만 추가
                if number not in lotto:
                    lotto.append(number)


            # ---------------------------------
            # 직접 정렬
            # ---------------------------------

            for i in range(len(lotto) - 1):

                for j in range(len(lotto) - 1 - i):

                    if lotto[j] > lotto[j + 1]:

                        temp = lotto[j]
                        lotto[j] = lotto[j + 1]
                        lotto[j + 1] = temp


            print()
            print("추첨된 로또 번호")
            print(lotto)


            # ---------------------------------
            # 2차원 리스트에 저장
            # ---------------------------------

            lotto_history.append(lotto)

            print("로또 번호가 과거 이력에 저장되었습니다.")


        else:
            print("잘못된 모드입니다.")


    # ====================================
    # 2. 결과 보기
    # ====================================

    elif main_menu == "2":

        print()
        print("[ 결과 보기 ]")
        print("1. 업앤다운 랭킹")
        print("2. 로또 번호 과거 이력")

        result_menu = input("메뉴를 선택하세요 : ")


        # =================================
        # 2-1. 업앤다운 랭킹
        # =================================

        if result_menu == "1":

            if len(players) == 0:

                print("아직 게임 기록이 없습니다.")


            else:

                # =================================
                # 원본 데이터가 변경되지 않도록
                # 새로운 리스트 생성
                # =================================

                ranking = []


                for player in players:
                    ranking.append(player)


                # =================================
                # 시도횟수를 기준으로 직접 정렬
                # 오름차순
                #
                # 2회
                # 3회
                # 5회
                # ...
                # =================================

                for i in range(len(ranking) - 1):

                    for j in range(len(ranking) - 1 - i):

                        # 딕셔너리에서
                        # 시도횟수 값만 가져와서 비교
                        current_count = ranking[j]["시도횟수"]
                        next_count = ranking[j + 1]["시도횟수"]


                        # 앞의 시도횟수가 더 크다면
                        if current_count > next_count:

                            # 위치 교환
                            temp = ranking[j]
                            ranking[j] = ranking[j + 1]
                            ranking[j + 1] = temp


                # =================================
                # TOP 3 출력
                # =================================

                print()
                print("==========================")
                print("      업앤다운 TOP 3")
                print("==========================")


                # 사람이 3명보다 적을 수도 있으므로
                # 출력할 사람 수 결정
                if len(ranking) >= 3:
                    ranking_count = 3

                else:
                    ranking_count = len(ranking)


                for i in range(ranking_count):

                    # 리스트에서 딕셔너리 꺼내기
                    player = ranking[i]


                    # 딕셔너리에서 각각의 값 꺼내기
                    name = player["name"]
                    count = player["시도횟수"]


                    print(
                        i + 1,
                        "등 :",
                        name,
                        "/",
                        count,
                        "회"
                    )


        # =================================
        # 2-2. 로또 과거 이력
        # =================================

        elif result_menu == "2":

            if len(lotto_history) == 0:

                print("아직 로또 추첨 기록이 없습니다.")


            else:

                print()
                print("==========================")
                print("      로또 과거 이력")
                print("==========================")


                # ---------------------------------
                # 2차원 리스트를 인덱스로 접근
                # ---------------------------------

                for i in range(len(lotto_history)):

                    print(
                        i + 1,
                        "회차 :",
                        lotto_history[i]
                    )


                print()
                history_number = int(
                    input("확인할 회차를 입력하세요 : ")
                )


                # 사용자는 1회차부터 입력하지만
                # 리스트 인덱스는 0부터 시작
                index = history_number - 1


                if index >= 0 and index < len(lotto_history):

                    print()
                    print(
                        history_number,
                        "회차 번호 :",
                        lotto_history[index]
                    )


                    # 번호 하나씩 인덱스로 출력
                    print("1번째 번호 :", lotto_history[index][0])
                    print("2번째 번호 :", lotto_history[index][1])
                    print("3번째 번호 :", lotto_history[index][2])
                    print("4번째 번호 :", lotto_history[index][3])
                    print("5번째 번호 :", lotto_history[index][4])
                    print("6번째 번호 :", lotto_history[index][5])


                else:
                    print("존재하지 않는 회차입니다.")


        else:
            print("잘못된 메뉴입니다.")


    # ====================================
    # 3. 프로그램 종료
    # ====================================

    elif main_menu == "3":

        print()
        print("프로그램을 종료합니다.")
        break


    else:
        print("잘못된 메뉴입니다.")