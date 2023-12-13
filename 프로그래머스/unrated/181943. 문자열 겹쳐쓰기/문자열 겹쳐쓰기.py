def solution(my_string, overwrite_string, s):     
    return my_string[:s] + overwrite_string + my_string[s+len(overwrite_string):]

    #replce 문자열 전체를 변환시킴
    #return my_string.replace(my_string[s:s+len(overwrite_string)],overwrite_string)  