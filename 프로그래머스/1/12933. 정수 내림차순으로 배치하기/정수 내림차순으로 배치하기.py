def solution(n):
    answer = 0
    test = []

    for x in str(n):
        test.append(int(x))
    
    test.sort(reverse=True)
    answer = int(''.join(map(str, test)))
    
    return answer

