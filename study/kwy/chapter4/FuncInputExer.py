# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 15:54:27 2019

@author: wykim
"""
## 사용자 입력
#number = input("숫자를 입력하세요: ")

#print(number)

##print 자세히 알기
a = 123
print(a)

a="Python"
print(a)

a=[1,2,3]
print(a)

#한 줄에 결과값 출력하기
for i in range(10):
    print(i,end=' ')
    
#exercise
 
    
def Display():
    print("\n연산할 기호를 입력하세요")
    print("1.+")
    print("2.-")
    print("3.*")
    print("4./")    
    



while(1):
    Display()
    choice = (input())
    num1 = int(input())
    num2 = int(input())
    if choice == '+':
        print("덧셈 선택")
        print(num1+num2)
        break
    elif choice == "-":
        print("뺄셈 선택")
        print(num1-num2)
        break
    elif choice == "*":
        print("곱셈 선택")
        print(num1*num2)
        break
    elif choice == "/":
        if num2 == 0:
            print("제수가 0이므로 나눗셈을 할 수 없습니다 다시 입력해주세요")
            continue
        print("나눗셈 선택")
        print(num1/num2)
        break
    else:
        print("사칙연산 이외의 기호를 입력하셨습니다! 다시 입력해주세요")
        continue
