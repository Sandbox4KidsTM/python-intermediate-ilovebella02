# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 10:41:39 2018

@author: SBX-001
"""

pal = "RaceCar"
not_pal = "Hello"

def is_palendrome(word):
    word = word.lower()
    i = 0
    rev_word = reversed(word)
    for letter in rev_word:
        if letter != word[i]:
            return False
        i += 1
        return True

def is_pal(word):
    word = word.lower()
    rev_word = word[::-1]
    return rev_word == word

print(is_palendrome(pal) == True)
print(is_palendrome(not_pal) == False)

print(is_pal(pal) == True)
print(is_pal(not_pal) ==  False)