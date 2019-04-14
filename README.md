# assignments


1.	카이사르 암호문
A.	문제 해결 방법
이 프로그램은 다음과 같은 과정을 거쳐야 합니다. 첫째, 암호화 키를 입력 받습니다. 둘째, 암호문으로 변환할 평문을 입력 받습니다. 셋째, find 함수로 알파벳을 0~25의 수로 변환하고 키를 더한 뒤 26으로 나눈 나머지를 구합니다. 넷째, 0~25의 수를 알파벳으로 변환합니다. 다섯째, 네 개의 알파벳을 연결해 암호문을 만들고 출력합니다.
이 코딩의 핵심은 알파벳이라는 문자를 0~25의 수로 바꿔서 연산하고 연산을 마친 뒤에는 0~25의 숫자를 알파벳이라는 문자로 바꾸어 출력하는 것입니다. 알파벳을 숫자로 바꿀 때는 find 함수를 사용하고 숫자를 알파벳으로 바꿀 때는 index 함수를 사용합니다.
B.	코드 설명
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
C.	테스트 실행 결과
 
암호화 키로 24 대신 24에서 26을 뺀 -2를 입력해도 같은 결과가 출력됩니다. 이는 key가 int 함수로 정수의 범위를 포괄하고 있기 때문입니다.
평문에 eggs 대신 EGGS를 입력하면 다른 값이 나옵니다. 이는 처음 알파벳을 나열한 텍스트(alphabets)를 지정할 때 소문자로만 이루어진 "abcdefghijklmnopqrstuvwxyz"을 입력했기 때문입니다.

2.	트리테미우스 암호문
A.	문제 해결 방법
이 프로그램은 다음과 같은 과정을 거쳐야 합니다. 첫째, 암호문으로 변환할 평문을 입력 받습니다. 둘째, find 함수로 알파벳을 0~25의 수로 변환하고 첫 번째 알파벳에 해당하는 수에는 0을, 두 번째 알파벳에 해당하는 수에는 1을 더하는 방식으로 더한 뒤 26으로 나눈 나머지를 구합니다. 셋째, 0~25의 수를 알파벳으로 변환합니다. 넷째, 네 개의 알파벳을 연결해 암호문을 만들고 출력합니다.
이 코딩의 핵심은 알파벳이라는 문자를 0~25의 수로 바꿔서 연산하고 연산을 마친 뒤에는 0~25의 숫자를 알파벳이라는 문자로 바꾸어 출력하는 것입니다. 알파벳을 숫자로 바꿀 때는 find 함수를 사용하고 숫자를 알파벳으로 바꿀 때는 index 함수를 사용합니다.
B.	코드 설명
# 평문을 입력 받는다.
plaintext = input("평문: ")
	
# 알파벳을 나열한 텍스트가 자주 쓰이기 때문에 미리 지정해둔다.
alphabets = "abcdefghijklmnopqrstuvwxyz"
	
# find 함수로 알파벳을 0~25의 수로 변환해 첫 번째 알파벳에 해당하는 수에는 0을, 두 번째 알파벳에 해당하는 수에는 1을 더하는 방식으로 더한 뒤 26으로 나눈 나머지를 구한다.
first_number = alphabets.find(plaintext[0])
second_number = ( alphabets.find(plaintext[1]) + 1 ) % 26
third_number = ( alphabets.find(plaintext[2]) + 2 ) % 26
fourth_number = ( alphabets.find(plaintext[3]) + 3 ) % 26
	
# 0~25의 수를 알파벳으로 변환한다.
first_letter = alphabets[first_number]
second_letter = alphabets[second_number]
third_letter = alphabets[third_number]
fourth_letter = alphabets[fourth_number]
	
# 네 개의 알파벳을 연결해 암호문을 만들고 출력한다.
cyphertext = first_letter+second_letter+third_letter+fourth_letter
print("트리테미우스 암호문:",cyphertext)
C.	테스트 실행 결과
 
