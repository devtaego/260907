# 사용자정의 함수

scores = [80, 90, 75, 88, 92]

total = 0

for score in scores :
    total += score

average = total / len(scores)


## 1. 일일히 입력하기


print(f"평균 점수: {average:.1f}점")

scores1 = [80, 90, 75, 88, 92]
scores2 = [60, 70, 85, 90, 100]

total = 0
for score in scores1:
    total += score
average = total / len(scores1)
print(f"1반 평균: {average:.1f}점")

total = 0
for score in scores2:
    total += score
average = total / len(scores2)
print(f"2반 평균: {average:.1f}점")


## 2. def 사용하기


def get_average(scores):
    total = 0

    for score in scores:
        total += score

    average = total / len(scores)

    return average


scores1 = [80, 90, 75, 88, 92]
scores2 = [60, 70, 85, 90, 100]

avg1 = get_average(scores1)
avg2 = get_average(scores2)

print(f"1반 평균: {avg1:.1f}점")
print(f"2반 평균: {avg2:.1f}점")


##


def say_hello() :
    print("안녕하세요!")


##

def print_menu():
    print("1. 전체 학생 보기")
    print("2. 평균 점수 보기")
    print("3. 합격자 보기")
    print("0. 종료")


print_menu()


##


def say_hello(name):
    print(f"{name}님, 안녕하세요.")


say_hello("민수")
say_hello("지수")


def print_pass_students(scores, pass_socre = 60):
    for score in scores:
        if score >= pass_socre :
            print(score, end =" ")

scores = [50,60,70,80,90]
print_pass_students(scores,80)


###


students = [
    {"name": "민수", "score": 85},
    {"name": "지수", "score": 92},
    {"name": "영희", "score": 55},
    {"name": "철수", "score": 73}
]


# 평균 점수 함수
def get_average_score(students):
    total = 0

    for student in students:
        total += student["score"]

    return total / len(students)


# 합격자 이름 반환 함수
def get_pass_students(students, pass_score=60):
    passed = []

    for student in students:
        if student["score"] >= pass_score:
            passed.append(student["name"])

    return passed


# 등급 추가 함수
def add_grade(students):
    for student in students:
        if student["score"] >= 90:
            student["grade"] = "A"
        elif student["score"] >= 80:
            student["grade"] = "B"
        elif student["score"] >= 60:
            student["grade"] = "C"
        else:
            student["grade"] = "F"

    return students


# 전체 사용
students = [
    {"name": "민수", "score": 85},
    {"name": "지수", "score": 92},
    {"name": "영희", "score": 55},
    {"name": "철수", "score": 73}
]

average = get_average_score(students)
passed = get_pass_students(students)
students = add_grade(students)

print(f"평균 점수: {average:.1f}점")
print(f"합격자: {passed}")
print(students)


##


scores = [80, 90, 70]

def add_score(data):
    data.append(100)


add_score(scores)

print(scores)


###

student = {
    "name": "민수",
    "score": 85
}

def add_result(data):
    data["result"] = "합격"

# student["result"] = "합격"

print(student)


###

print()
#global은 되도록 사용하지 말 것.
score = 80

def change_score():
    global score
    score = 90
    print("함수 안 score:", score)

change_score()
print("함수 밖 score:", score)