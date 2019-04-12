# -*- coding: utf-8 -*-

import re
def get_pattern(string):  
    
    rule_e = re.compile(r'e\b')
    rule_ce = re.compile(r'[^aeiou]e\b')
    rule_ie = re.compile(r'ie\b')
    rule_eoae = re.compile(r'[eoa]\e')
    rule_ue = re.compile(r'ue\b')
    rule_cy = re.compile(r'[^aeiou]y\b')
    rule_cvc = re.compile(r'[^aeiou][aeiou][^aeiouy]\b')
    
    if rule_e.search(string) :
        if rule_ce.search(string): 
            stem = string[:-1]
            particle = re.compile('{}(ed|ing)'.format(stem))
        elif rule_ie.search(string):
            stem = string[:-2]
            particle = re.compile('{}(ied|ying)'.format(stem))
        elif rule_eoae.search(string):
            stem = string
            particle = re.compile('{}(d|ing)'.format(stem))
        elif rule_ue.search(string):
            stem = string[:-1]
            particle = re.compile('{}(ed|ing)'.format(stem))
            
    elif rule_cy.search(string):
        stem = string[:-1]
        particle = re.compile('{}(ied|ying)'.format(stem))
        
    elif rule_cvc.search(string):
        stem = string + string[-1]
        particle = re.compile('{}(ed|ing)'.format(stem))

    else:
        particle = re.compile('{}(ed|ing)'.format(string))
        
    return particle
        

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