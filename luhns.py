# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 05:23:37 2021

@author: gocan
"""

# Luhn Algorithm

def luhn_checksum(card_num):
    def digits_of(n):
        return [int(d) for d in str(n)]
    digits = digits_of(card_num)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = 0
    checksum += sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d*2))
        return checksum % 10
                                   
print('Valid!') if luhn_checksum("5163610076726361")==0 else print('Invalid!')      
