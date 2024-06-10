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

    # choix d'un chiffre aléatoire
    x = random.randint(0, 5)
    
    # pour que le shellcode soit fonctionnel il faut commencer par xor rax, rax ou équivalent :
    resultat = [randomxor('rax')]

    if x > 0:
        choix = random.sample(range(len(reg)), min(x, len(reg)))
        for index in choix:
            resultat.append(randomxor(reg[index]))
    
    # Concatenation
    resultat_concat = ''.join(resultat)

    return resultat_concat  
