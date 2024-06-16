#!/usr/bin/env python3
import argparse
from choix_general import fn_choix_general

# Fonction permettant de convertir l'adresse IP de l'argument '--ip' dans le bon format hexadecimal. 
def ip_to_hex(ip):

    octets = ip.split('.') # Récupération de chaque octet de l'adresse IP
    escaped_ip = ''
    
    for i, octet in enumerate(octets):
        if i != 0:
            escaped_ip += '\\'
        escaped_ip += f'x{int(octet):02x}'# Mise sous la forme : \\xHexa - Exemple : 127.1.1.1 = \\x7f\\x01\\x01\\x01

    # Le retour de cette fonction est sous la forme d'une chaîne de caractères formatée.
    return escaped_ip


# Fonction permettant de convertir le port de l'argument '--port' dans le bon format hexadecimal. 
def port_to_hex(port):

    # Étapes de calcul pour convertir le port en hexadécimal : 
    high_byte = port >> 8 # Calcul de byte supérieur
    low_byte = port & 0xFF # Calcul du byte inférieur

    # Le retour de cette fonction est sous la forme d'une chaîne de caractères formatée.
    return f'x{high_byte:02x}\\x{low_byte:02x}' # Mise sous la forme : \\xHexa - Exemple : 4444 = \\x11\\x5c

def banner():
    print("""

 .----------------.  .----------------.  .-----------------. .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |  ________    | || |      __      | || | ____  _____  | || |  ____  ____  | || |    _______   | || |  ____  ____  | || |  _________   | || |   _____      | || |   _____      | |
| | |_   ___ `.  | || |     /  \     | || ||_   \|_   _| | || | |_  _||_  _| | || |   /  ___  |  | || | |_   ||   _| | || | |_   ___  |  | || |  |_   _|     | || |  |_   _|     | |
| |   | |   `. \ | || |    / /\ \    | || |  |   \ | |   | || |   \ \  / /   | || |  |  (__ \_|  | || |   | |__| |   | || |   | |_  \_|  | || |    | |       | || |    | |       | |
| |   | |    | | | || |   / ____ \   | || |  | |\ \| |   | || |    \ \/ /    | || |   '.___`-.   | || |   |  __  |   | || |   |  _|  _   | || |    | |   _   | || |    | |   _   | |
| |  _| |___.' / | || | _/ /    \ \_ | || | _| |_\   |_  | || |    _|  |_    | || |  |`\____) |  | || |  _| |  | |_  | || |  _| |___/ |  | || |   _| |__/ |  | || |   _| |__/ |  | |
| | |________.'  | || ||____|  |____|| || ||_____|\____| | || |   |______|   | || |  |_______.'  | || | |____||____| | || | |_________|  | || |  |________|  | || |  |________|  | |
| |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 
    -> Author : Boleyno
          
""")


def main():

    # fullrdm = None si l'argument facultatif '--random' n'est pas sélectionné lors de l'exécution du programme. 
    fullrdm = None

    # Arguments du programme
    parser = argparse.ArgumentParser(description='Convertir l\'adresse IP et le port en format hexadécimal.')
    parser.add_argument('--ip', type=str, required=True, help='Adresse IP à convertir')
    parser.add_argument('--port', type=int, required=True, help='Port à convertir')
    parser.add_argument('--random', type=str, required=False, help='Aléatoire au milieu du shellcode afin d\'éliminer les paternes | --random yes')
    args = parser.parse_args()

    # Affichage de la bannière
    banner()

    ip = ip_to_hex(args.ip)
    port = port_to_hex(args.port)
    fullrdm = args.random

    fn_choix_general(port, ip, fullrdm)

if __name__ == "__main__":
    main()
