# -*- coding: utf-8 -*-

#시작할 숫자, 마지막 숫자 받는다.
start=int(input("시작할 숫자: "))
end=int(input("마지막 숫자: "))

# 입력된 범위내에서 계산한다.
for i in range(start,end+1):
   
    # output을 만든다.
    output = ""
    
    # i를 str으로 변환해 준다.
    j=str(i)
    
    # 값이 3,6,9 중 하나인 경우 *을 추가하게 한다. 아니면 넘어간다.
    for num in j:
        if num == "3" or num == "6" or num == "9":
                output += "*"
        else:
                pass
    # 만약 *이 한 번도 안 나왔다면 숫자를 그대로 출력하게 한다.
    if output == "":
        output = i
    
    # 결과를 한 줄로 출력한다.
    print(output, end=" ")