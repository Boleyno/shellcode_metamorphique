#!/usr/bin/env python3
import random

def aleatoire_xor(reg) :
    op_liste = [
        f'\\x48\\x31\\{reg}', # xor rax, rax
        f'\\x48\\x29\\{reg}', # sub rax, rax
        #f'\\x48\\x31\\{reg}\\x48\\x6b\\{reg}\\x00', # xor rax, rax - imul rax, rax
        #f'\\xb8\\x01\\x00\\x00\\x00\\x48\\x29\\{reg}', # mov rax, 1 - sub rax, rax
        #f'\\xb8\\x01\\x00\\x00\\x00\\x48\\x21\\{reg}', # mov rax, 1 - and rax, rax
        #f'\\xb8\\x01\\x00\\x00\\x00\\x48\\x31\\{reg}' # mov rax, 1 - xor rax, rax
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
    
    elif reg == 'dil':

        liste_choix = [
            f'\\x40\\xb7\\{format_num_hex}', # mov dil, num
            f'\\x40\\x30\\xff\\x40\\x80\\xc7\\{format_num_hex}', # xor dil, dil - add dil , num
            f'\\x40\\xfe\\xc7\\x40\\x80\\xc7\\{format_pour_inc}' # inc dil - add dil , num-1
        ]
        
        choix = random.choice(liste_choix)

    elif reg == 'sil':

        num_moins_un_hex = hex(num - 1)[2:]  # Exclusion des deux premiers caractères (0x) et réalisation de -1
        format_pour_inc = f'x{num_moins_un_hex}'  # Format pour l'incrémentation
        
        liste_choix = [
            f'\\x40\\xb6\\{format_num_hex}', # mov sil, num
            f'\\x40\\x30\\xf6\\x40\\x80\\xc6\\{format_num_hex}', # xor sil, sil - add sil , num
        ]
        
        choix = random.choice(liste_choix)

    elif reg == 'dl':

        num_moins_un_hex = hex(num - 1)[2:]  # Exclusion des deux premiers caractères (0x) et réalisation de -1
        format_pour_inc = f'x{num_moins_un_hex}'  # Format pour l'incrémentation
        
        liste_choix = [
            f'\\xb2\\{format_num_hex}', # mov dl, num
            f'\\x30\\xd2\\x80\\xc2\\{format_num_hex}', # xor dl, dl - add dl , num
            f'\\xfe\\xc2\\x80\\xc2\\{format_pour_inc}' # inc dl - add dl , num-1
        ]
        
        choix = random.choice(liste_choix)

    return choix

def full_random():

    reg_liste = [
        'xd2', # Registre : r10
        'xdb', # Registre : r11
        'xe4', # Registre : r12
        'xed', # Registre : r13
        'xf6' # Registre : r14
    ]

    reg = random.choice(reg_liste)

    if reg == 'xd2':
        reg_c = 'xc2' # Exemple pour l'opérande de l'opération 'inc r10' ->  "\\x49\\xff\\c2"
        reg_push = 'x52' # Push = '\\x41\\x53'
        reg_pop = 'x5a' # Pop = '\\x41\\x5b'

    if reg == 'xdb':
        reg_c = 'xc3' 
        reg_push = 'x53' 
        reg_pop = 'x5b' 

    if reg == 'xe4':
        reg_c = 'xc4' 
        reg_push = 'x54' 
        reg_pop = 'x5c' 

    if reg == 'xed':
        reg_c = 'xc5'
        reg_push = 'x55' 
        reg_pop = 'x5d' 

    if reg == 'xf6':
        reg_c = 'xc6'
        reg_push = 'x56' 
        reg_pop = 'x5e' 

    op_liste = [
        f"\\x4d\\x31\\{reg}", # xor rXX, rXX 
        f"\\x49\\xff\\{reg_c}\\x4d\\x31\\{reg}", # inc rXX - xor rXX, rXX 
        f"\\x41\\{reg_push}\\x41\\{reg_pop}" # push rXX - pop rXX
        f"\\x49\\x83\\{reg_c}\\x01\\x4d\\x31\\{reg}", # xor rXX, rXX - add rXX, 01 - 
    ]

