# -*- coding: utf-8 -*-

# 강좌: 컴퓨터의 개념 및 실습
# 날짜: 2018/03/23
# 작성자: 이건희
# 설명: [숙제02심화] 1. 카이사르 암호문


# 암호화 키를 입력 받는다. int 함수를 쓰지 않으면 뒤에서 Type error 발생한다.
key = int(input("암호화 키: "))

# 평문을 입력 받는다.
plaintext = input("평문: ")

# 알파벳을 나열한 텍스트가 자주 쓰이기 때문에 미리 지정해둔다.
alphabets = "abcdefghijklmnopqrstuvwxyz"

# find 함수로 알파벳을 0~25의 수로 변환해 key를 더하고 26으로 나눈 나머지를 구한다.
first_number = ( alphabets.find(plaintext[0]) + key ) % 26
second_number = ( alphabets.find(plaintext[1]) + key ) % 26
third_number = ( alphabets.find(plaintext[2]) + key ) % 26
fourth_number = ( alphabets.find(plaintext[3]) + key ) % 26

# 0~25의 수를 알파벳으로 변환한다.
first_letter = alphabets[first_number]
second_letter = alphabets[second_number]
third_letter = alphabets[third_number]
fourth_letter = alphabets[fourth_number]

# 네 개의 알파벳을 연결해 암호문을 만들고 출력한다.
cyphertext = first_letter+second_letter+third_letter+fourth_letter
print("카이사르 암호문:",cyphertext)