def solution(cpr):
    answer = []
    basic_order = ["check", "call", "pressure", "respiration", "repeat"]
    for action in basic_order:
        for i in range (5):
            if action == basic_order[i]:
                answer.append(i+1)

    print(answer)
    return answer

