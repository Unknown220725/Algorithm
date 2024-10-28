def solution(quiz):
    answer = []
    box = []
    for x in quiz:
        box = x.split("=")

        if eval(box[0]) == int(box[1]):
            answer.append("O")
        else:
            answer.append("X")
        
        
    return answer