# -*- coding: utf-8 -*-

def caesar(plain, key=3):
    ''' 평문 plain과 암호화 키 key를 받아 카이사르 암호문을 돌려준다.
    
    >>> caesar('nevertrustbrutus', 13)
    'ariregehfgoehghf'    '''

    alphabets = "abcdefghijklmnopqrstuvwxyz"
    cipher = ""
    for char in plain:
        number = ( alphabets.find(char) + key ) % 26
        letter = alphabets[number]                
        cipher += letter
    return cipher
    
def trithem(plain):
    ''' 평문 plain을 받아 트리테미우스 암호문을 돌려준다.
    
    >>> trithem('nevertrustbrutus')
    'nfxhvyxbaclcggih'    '''
    
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    cipher = ""
    for i, char in enumerate(plain):
        number = ( alphabets.find(char) + i ) % 26
        letter = alphabets[number]
        cipher += letter
    return cipher
    
def vigenere(plain, key):
    ''' 평문 plain과 암호화 키 key를 받아 비즈네르 암호문을 돌려준다.
    
    >>> vigenere('nevertrustbrutus', 'python')
    'ccolfggslapejrnz'    '''
    
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    cipher = ""
    for i, char in enumerate(plain):
        number = ( alphabets.find(char) + alphabets.find(key[i%len(key)]) ) % 26
        letter = alphabets[number]
        cipher += letter
    return cipher

def polybius(plain):
    ''' 평문 plain을 받아 폴뤼비오스 암호문을 돌려준다.
    
    >>> polybius('julius')
    '13 40 21 13 40 33'    '''
    
    alphabets = "abcdefghiklmnopqrstuvwxyz"
    cipher = ""
    newplain= ""
    for char in plain:
        if char == "j":
            newplain += "i"
        else:
            newplain += char
    for char1 in newplain:
        coordinate = ((alphabets.find(char1))//5)*10+(alphabets.find(char1))%5  
        cipher += str(coordinate).zfill(2) + " "
    return cipher[:-1]