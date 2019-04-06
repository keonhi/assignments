# -*- coding: utf-8 -*-

# 암호화 키를 입력 받는다.
raw = input("암호화 키: ")
if raw.isdigit():
    key=int(raw)
    
    # 평문을 입력 받는다.
    plaintext = input("평문: ")

    # 알파벳을 나열한 텍스트가 자주 쓰이기 때문에 미리 지정해둔다.
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    cyphertext = ""
    for char in plaintext:
        
        # find 함수로 알파벳을 0~25의 수로 변환해 key를 더하고 26으로 나눈 나머지를 구한다.
        number = ( alphabets.find(char) + key ) % 26
    
        # 0~25의 수를 알파벳으로 변환한다.
        letter = alphabets[number]                
        cyphertext += letter
        
    print("카이사르 암호문:", cyphertext)

else:
    print("숫자를 입력하세요.")