#!/usr/bin/env python3
from choix_part0 import partie0
from choix_part1 import partie1
from choix_part2 import partie2
from choix_part3 import partie3
from choix_part4 import partie4
from choix_part5 import partie5
from choix_part6 import partie6


port = 'x11\\x5c'
ip = 'x7f\\x01\\x01\\x01'

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
