def solution(my_string):
    answer = ''
    dict1 = {}

# 요소가 딕셔너리에 있다면 += 1, 없다면 = 1
    for num in my_string:
        if num in dict1: # dict.get(num)로 대체가능
            dict1[num] += 1
        else:
            dict1[num] = 1
    
    for index, (key, elem) in enumerate(dict1.items()):
        answer+=key
    
    return answer