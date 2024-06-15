#!/usr/bin/env python3
from func_instru import *

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

    return resultat_concat  
