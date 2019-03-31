# -*- coding: utf-8 -*-

# 1부터 100까지 수에 대해서 계산한다.
for i in range(1,101):
    
    # 일의 자리가 3,6,9 중 하나인 경우를 본다.
    if i % 10 in range(3, 10, 3):
        if i // 30 == 0:
            print("*", end=" ")
        
        # 십의 자리도 3,6,9 중 하나면 **, 아니면 *을 출력한다.
        elif i % 30 in range(0,10):
            print("**", end=" ")
        else:
            print("*", end=" ")
   
    # 일의 자리가 3,6,9 중 하나가 아니면 십의 자리만 확인 한다.
    else:
        if i % 30 in range(0,10) and  i // 30 != 0:
            print("*", end=" ")
        else:
            print(i, end=" ")