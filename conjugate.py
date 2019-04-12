# -*- coding: utf-8 -*-

import re
def get_pattern(string):  
    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"
    
    if string.endswith("e") :
        if string[-2] in consonants:
            stem = string[:-1]
            particle = re.compile('{}(ed|ing)'.format(stem))
        elif string[-2] == "i":
            stem = string[:-2]
            particle = re.compile('{}(ied|ying)'.format(stem))
        elif string[-2] in "eoa":
            stem = string
            particle = re.compile('{}(d|ing)'.format(stem))
        elif string[-2] == "u":
            stem = string[:-1]
            particle = re.compile('{}(ed|ing)'.format(stem))
            
    elif string.endswith("y") and string[-2] in consonants:
        stem = string[:-1]
        particle = re.compile('{}(ied|ying)'.format(stem))
        
    elif string[-1] in consonants and string[-2] in vowels \
    and string[-3] in consonants and string[-1] != "y":
        stem = string + string[-1]
        particle = re.compile('{}(ed|ing)'.format(stem))
    
    else :
        particle = re.compile('{}(ed|ing)'.format(string))
        
    print(particle)


if __name__ == '__main__':
    words = [ "dance", "dye", "play", "apply", "annoy", "help", "step", "lie",\
    "agree", "tiptoe", "pursue"]
    for word in words:
        print("{}의 변형 패턴: {}".format(word, get_pattern(word).pattern))


from timeit import timeit

test = """
for i in range(100):
    if __name__ == '__main__':
        words = [ "dance", "dye", "play", "apply", "annoy", "help", "step", "lie",\
        "agree", "tiptoe", "pursue"]
        for word in words:
            print("{}의 변형 패턴: {}".format(word, get_pattern(word).pattern))"""

print(timeit(stmt=test))