def solution(my_string):
    answer = 0

    import re

    text = my_string
    numbers = re.findall(r'\d+', text)
    result = ''.join(numbers)
    
    for x in result:
        print(x)
        answer += int(x)
    # print(result)  # 출력 결과: 123
    
    return answer