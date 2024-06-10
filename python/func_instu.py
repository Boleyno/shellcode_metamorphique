#!/usr/bin/env python3
import random

def randomxor(reg):
    
    if reg == 'al':
        op = '\\x30\\xc0'

    elif reg == 'rax':
        op_liste = [
            '\\x48\\x31\\xc0', # xor rax, rax
            '\\x48\\x29\\xc0', # sub rax, rax
            '\\x48\\x21\\xc0', # and rax, rax
            '\\x48\\x31\\xc0\\x48\\x6b\\xc0\\x00', # imul rax, rax
            '\\xb8\\x01\\x00\\x00\\x00\\x48\\x29\\xc0', # mov rax, 1 - sub rax, rax
            '\\xb8\\x01\\x00\\x00\\x00\\x48\\x21\\xc0', # mov rax, 1 - and rax, rax
            '\\xb8\\x01\\x00\\x00\\x00\\x48\\x31\\xc0' # mov rax, 1 - xor rax, rax
        ]

        x = random.randint(0, len(op_liste) - 1)
        op = op_liste[x]
        print(f'OP = {op}')

    elif reg == 'rbx':
        op = '\\x48\\x31\\xdb' # xor rbx, rbx

    elif reg == 'rcx':
        op = '\\x48\\x31\\xc9' # xor rcx, rcx
    
    elif reg == 'rdx':
        op = '\\x48\\x31\\xd2' # xor rdx, rdx
    
    elif reg == 'rdi':
        op = '\\x48\\x31\\xff' # xor rdi, rdi

    elif reg == 'rsi':
        op = '\\x48\\x31\\xf6' # xor rsi, rsi


    return op

def movxl(reg, num):

    num_hex = hex(num)[2:]  # On exclut les deux premiers caractères (0x)
    format_num_hex = f'x{num_hex}'  # On ajoute \\x pour chaque caractère hexadécimal

    num_moins_un_hex = hex(num - 1)[2:]  # Exclusion des deux premiers caractères (0x) et réalisation de -1
    format_pour_inc = f'x{num_moins_un_hex}'  # Format pour l'incrémentation

    if reg == 'al':
        op1 = 'xb0' # mov al 
        op2 = 'x04' # add al 

        liste_choix = [
            f'\\{op1}\\{format_num_hex}', # mov al, num
            f'\\x30\\xc0\\{op2}\\{format_num_hex}', # xor al, al - add al , num
            f'\\xfe\\xc0\\{op2}\\{format_pour_inc}' # inc al - add al , num-1
        ]

        choix = random.choice(liste_choix)
        
    return choix

