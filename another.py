import random


LOTTO_SIZE = 6
LOTTO_MAX = 45
DIFFICULTIES = {"1": 50, "2": 100, "3": 200}


def print_main_menu():
    print("\n==================시작===================")
    print("1번 : 게임 선택")
    print("2번 : 로또 번호 이력 / 랭킹 보기")
    print("3번 : 종료\n")


def draw_lotto(numbers=None):
    numbers = [] if numbers is None else list(numbers)
    remaining = LOTTO_SIZE - len(numbers)
    available = [number for number in range(1, LOTTO_MAX + 1) if number not in numbers]
    numbers.extend(random.sample(available, remaining))
    return sorted(numbers)


def create_manual_lotto():
    numbers = []
    while len(numbers) < LOTTO_SIZE:
        number = int(input("\n1~45 중 번호를 입력해주세요 : "))
        print("0 입력 시 남은 숫자는 자동 선택")

        if number == 0:
            return draw_lotto(numbers)
        if not 1 <= number <= LOTTO_MAX:
            print("1~45 중에서 번호를 입력하세요.")
        elif number in numbers:
            print("이미 선택된 번호입니다.")
        else:
            numbers.append(number)

    return sorted(numbers)


def play_lotto(history, round_number):
    print("\n===============================================")
    print("로또 번호 추출을 선택했습니다.")
    print("자동 : 1")
    print("수동 : 2")
    method = input("방식 선택 : ")

    if method == "1":
        numbers = draw_lotto()
    elif method == "2":
        numbers = create_manual_lotto()
    else:
        print("잘못된 방식입니다.")
        return round_number

    history.append(numbers)
    print(f"{round_number}회차 로또 번호 : {numbers}")
    return round_number + 1


def play_up_down(players):
    print("\n===============================================")
    print("업앤다운 게임을 진행합니다.\n")
    print("1. 쉬움  //  2. 보통  //  3. 어려움")
    level = input("난이도를 선택하세요. : ")
    max_number = DIFFICULTIES.get(level)
    if max_number is None:
        print("잘못된 난이도입니다.")
        return

    name = input("닉네임을 입력하세요 : ")
    answer = random.randint(1, max_number)
    attempts = 0
    print(f"\n업앤다운 게임을 시작합니다.\n1부터 {max_number} 사이의 숫자를 맞혀보세요.")

    while True:
        number = int(input("숫자 입력 : "))
        attempts += 1
        if number > answer:
            print("DOWN!")
        elif number < answer:
            print("UP!")
        else:
            print(f"\n정답입니다!\n시도횟수 : {attempts}")
            players.append({"name": name, "시도횟수": attempts})
            print("게임 결과가 저장되었습니다.")
            return


def show_history(history):
    print("\n===============================================")
    print("최근 5회 로또 이력")
    if not history:
        print("내역 없음")
        return
    print(f"최근 5회 내역 : {history[-5:]}")


def show_ranking(players):
    print("\n===============================================")
    if not players:
        print("아직 게임 기록이 없습니다.")
        return

    print("업앤다운 TOP 3")
    ranking = sorted(players, key=lambda player: player["시도횟수"])
    for rank, player in enumerate(ranking[:3], start=1):
        print(f"{rank}등 : {player['name']} / {player['시도횟수']}회")


def main():
    lotto_history = []
    players = []
    round_number = 1

    while True:
        print_main_menu()
        menu = input("메뉴 선택 : ")

        if menu == "1":
            print("\n로또 번호 추출 : 1 / 업앤다운 게임 : 2")
            game = input("선택 : ")
            if game == "1":
                round_number = play_lotto(lotto_history, round_number)
            elif game == "2":
                play_up_down(players)
        elif menu == "2":
            print("\n로또 이력 보기 : 1 / 업앤다운 랭킹 보기 : 2")
            record_menu = input("메뉴 선택 : ")
            if record_menu == "1":
                show_history(lotto_history)
            elif record_menu == "2":
                show_ranking(players)
        elif menu == "3":
            print("\n종료\n")
            return
        else:
            print("잘못된 메뉴입니다.")


main()