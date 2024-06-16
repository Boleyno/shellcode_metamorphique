#!/usr/bin/env python3
from func_instru import *

def partie0():

    # PARTIE : PREPARATION DES REGISTRES
    """
    xor rax, rax
	xor rbx, rbx
	xor rcx, rcx
	xor rdx, rdx
	xor rdi, rdi
	xor rsi, rsi
    """

    # Liste des registres qui seront initialsiés à 0 au début du programme
    reg = [
        'rbx',
        'rcx',
        'rdx',
        'rdi',
        'rsi'
    ]
    
    # Pour que le shellcode soit fonctionnel il faut commencer par xor rax, rax ou équivalent :
    resultat = [randomxor('rax')]

    for index in reg:
        resultat.append(randomxor(index))
    
    # Concatenation
    resultat_concat = ''.join(resultat)

    return resultat_concat  
