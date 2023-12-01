import sys
n = (int)(input()) # test case

first_term = 0
second_term = 1

for i in range(n):
    temp = first_term + second_term 
    first_term = second_term
    second_term = temp
    if(i+1==n):
        print(first_term)