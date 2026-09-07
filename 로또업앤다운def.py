
import random

# 로또 이력
eryuk = []

# 업앤다운 랭킹
ranking = []

print("메뉴를 선택해주세요!")

def num_select() :
    number = int(input())


while True:
    print("1. UP & DOWN / 2. 로또 / 3. 게임종료")
    menunum = int(input())
    print()

    # 1. UP & DOWN

    if menunum == 1:

        print("1. UP & DOWN 게임 / 2. 랭킹 / 3. 메인 메뉴")
        updownmenu = int(input())
        print()


        # 1. UP & DOWN 게임

        if updownmenu == 1:

            print("****** 숫자 UP & DOWN 게임에 오신걸 환영합니다! ******")
            print()

            def difficulty_select():
                print("1. 쉬움 - 횟수 제한 없음")
                print("2. 중간 - 10회 제한")
                print("3. 어려움 - 5회 제한")
                print("난이도를 선택해주세요!")

                difficulty = int(input())

                if difficulty == 1:
                    return 0

                elif difficulty == 2:
                    return 10

                elif difficulty == 3:
                    return 5

                else:
                    print("올바르지 않은 난이도입니다!")
                    print()


            print()

            print("닉네임을 입력해주세요!")
            nickname = input()

            randomnum = random.randint(1, 100)

            print(randomnum)

            attempt = 0
            success = False

            print()
            print("1부터 100 사이의 숫자를 입력해주세요!")

            while True:

                # 제한 횟수를 모두 사용했는지 확인
                if difficulty_select() != 0 and attempt >= difficulty_select():
                    print("시도 횟수를 모두 사용했습니다!")
                    print(f"정답은 {randomnum}이었습니다.")
                    break

                guessnum = int(input())

                attempt += 1

                if guessnum < randomnum:
                    print("더 큰 수를 입력하세요!")

                elif guessnum > randomnum:
                    print("더 작은 수를 입력하세요!")

                elif guessnum == randomnum:
                    print("정답입니다!")
                    print(f"{attempt}번 만에 정답을 맞췄습니다!")

                    success = True

                    # 랭킹에 아무도 없을 경우
                    if len(ranking) == 0:
                        ranking.append([nickname, attempt])

                    else:
                        found = False

                        # 기존 닉네임 검색
                        for i in range(len(ranking)):

                            if ranking[i][0] == nickname:
                                found = True

                                # 기존 기록보다 좋은 기록이면 갱신
                                if attempt < ranking[i][1]:
                                    ranking[i][1] = attempt

                        # 기존 닉네임이 없으면 새로 추가
                        if found == False:
                            ranking.append([nickname, attempt])

                    break

            print()


        # UP & DOWN 랭킹

        elif updownmenu == 2:

            if len(ranking) == 0:
                print("랭킹 기록이 존재하지 않습니다!")
                print()
                continue

            # 시도수 >> 이름 순으로 정렬
            for i in range(len(ranking)):

                for j in range(i + 1, len(ranking)):

                    if ranking[i][1] > ranking[j][1]:
                        ranking[i], ranking[j] = ranking[j], ranking[i]

                    elif ranking[i][1] == ranking[j][1]:

                        if ranking[i][0] > ranking[j][0]:
                            ranking[i], ranking[j] = ranking[j], ranking[i]

            print("****** UP & DOWN 랭킹 ******")
            print()

            for i in range(len(ranking)):
                print(f"{i + 1}위 : {ranking[i][0]} - {ranking[i][1]}회")

            print()


        # 메인 메뉴

        elif updownmenu == 3:

            print("메인 메뉴로 이동합니다!")
            print()
            continue

        else:
            print("올바르지 않은 번호입니다!")
            print()



    # 2. 로또

    elif menunum == 2:

        print("1. 로또 번호 추출 / 2. 로또 이력 보기 / 3. 메인 메뉴")
        lottomenu = int(input())
        print()


        # 로또 번호 추출

        if lottomenu == 1:

            print("****** 로또 번호 추출기에 오신걸 환영합니다! ******")

            while True:

                print()
                print("1. 자동 추출 / 2. 수동 추출 (반자동 가능) / 3. 메뉴로 돌아가기")

                lottonum = int(input())


                def lotto_pop():

                    while len(lotto) < 6:
                        x = random.randint(1, 45)

                        if x not in lotto:
                            lotto.append(x)

                    lotto.sort()

                # 자동 추출
                if lottonum == 1:

                    lotto = []
                    lotto_pop()

                    print("추천 번호는 ", end="")

                    for i in range(6):
                        print(lotto[i], end=" ")

                    print("입니다!")
                    print()

                    eryuk.append(lotto)

                # 수동 / 반자동 추출
                elif lottonum == 2:

                    lotto = []

                    while len(lotto) < 6:

                        print()
                        print("원하시는 번호를 입력해주세요!")
                        print("(모두 자동으로 입력하고 싶으시면 0을 눌러주세요!)")

                        wantnum = int(input())

                        if wantnum >= 1 and wantnum <= 45:

                            if wantnum not in lotto:

                                lotto.append(wantnum)

                                print(
                                    f"지금까지 {len(lotto)}개 입력하셨습니다! "
                                    "다음 번호를 입력해주세요!"
                                )

                            elif wantnum in lotto:

                                print("이미 입력한 숫자입니다! 다른 숫자를 입력해주세요!")

                            lotto.sort()
                            print(lotto)

                        elif wantnum == 0:

                            while len(lotto) < 6:

                                x = random.randint(1, 45)

                                if x not in lotto:
                                    lotto.append(x)

                            lotto.sort()

                            print(lotto)

                        else:

                            print("올바르지 않은 숫자입니다! 다시 입력하세요!")
                            continue

                        if len(lotto) == 6:
                            eryuk.append(lotto)

                # 로또 메뉴에서 나가기
                elif lottonum == 3:
                    break

                else:
                    print("올바르지 않은 메뉴입니다!")


        # 로또 이력

        elif lottomenu == 2:

            if len(eryuk) == 0:

                print("로또 번호 이력이 존재하지 않습니다!")
                print()
                continue

            print("****** 로또 번호 이력 ******")
            print()

            for i, v in enumerate(eryuk):

                print(f"{i + 1}회차 번호 : ", end="")

                for j in range(6):
                    print(eryuk[i][j], end=" ")

                print()

            print()


        # 메인 메뉴

        elif lottomenu == 3:

            print("메인 메뉴로 이동합니다!")
            print()
            continue

        else:
            print("올바르지 않은 번호입니다!")
            print()



    # 게임 종료

    elif menunum == 3:

        print("게임을 종료합니다.")
        break



    # 잘못된 번호 입력시

    else:

        print("올바르지 않은 번호입니다!")
        print()
        continue

