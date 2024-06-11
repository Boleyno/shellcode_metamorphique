#!/usr/bin/env python3
import random
from func_instu import *

def partie0():

    reg = [
        'rbx',
        'rcx',
        'rdx',
        'rdi',
        'rsi'
    ]

    
    # pour que le shellcode soit fonctionnel il faut commencer par xor rax, rax ou équivalent :
    resultat = [randomxor('rax')]

    for index in reg:
        resultat.append(randomxor(index))
    
    # Concatenation
    resultat_concat = ''.join(resultat)
    print("Partie 0 = ", resultat_concat)

    return resultat_concat  
