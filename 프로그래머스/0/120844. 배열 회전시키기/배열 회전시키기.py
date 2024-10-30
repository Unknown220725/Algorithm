def solution(numbers, direction):    
    # x번째 위치에 y 삽입 / 맨마지막 원소 리턴후 삭제
    # insert() / pop()
    
    if direction == "right":
        numbers.insert(0,numbers.pop())
        return numbers

    elif direction == "left": 
        numbers.append(numbers[0])
        numbers.remove(numbers[0])
        return numbers
        
    
