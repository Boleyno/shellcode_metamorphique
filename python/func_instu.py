#!/usr/bin/env python3
import random

def aleatoire_xor(reg_rax) :
    op_liste = [
        f'\\x48\\x31\\{reg_rax}', # xor rax, rax
        f'\\x48\\x29\\{reg_rax}', # sub rax, rax
        f'\\x48\\x31\\{reg_rax}\\x48\\x6b\\{reg_rax}\\x00', # xor rax, rax - imul rax, rax
        f'\\xb8\\x01\\x00\\x00\\x00\\x48\\x29\\{reg_rax}', # mov rax, 1 - sub rax, rax
        f'\\xb8\\x01\\x00\\x00\\x00\\x48\\x21\\{reg_rax}', # mov rax, 1 - and rax, rax
        f'\\xb8\\x01\\x00\\x00\\x00\\x48\\x31\\{reg_rax}' # mov rax, 1 - xor rax, rax
    ]

    x = random.randint(0, len(op_liste) - 1)
    op = op_liste[x]
    print(f'OP rax = {op}')

    return op

def randomxor(reg):
    
    if reg == 'al':
        op = '\\x30\\xc0'

    elif reg == 'rax':
        reg_rax = 'xc0'
        op = aleatoire_xor(reg_rax)

    elif reg == 'rbx':
        reg_rbx = 'xdb'
        op = aleatoire_xor(reg_rbx)

    elif reg == 'rcx':
        reg_rcx = 'xc9'
        op = aleatoire_xor(reg_rcx)
    
    elif reg == 'rdx':
        reg_rdx = 'xd2'
        op = aleatoire_xor(reg_rdx)
    
    elif reg == 'rdi':
        reg_rdx = 'xff'
        op = aleatoire_xor(reg_rdx)

    elif reg == 'rsi':
        reg_rdx = 'xf6'
        op = aleatoire_xor(reg_rdx)

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

