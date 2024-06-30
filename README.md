# Documentation du shellcode_metamorphique

Le projet de shellcode est constitué de 10 fichiers Python, avec `shellcode.py` comme fichier principal. Voici la documentation de ce programme :

```
shellcode.py --help
usage: shellcode.py [-h] --ip IP --port PORT [--random RANDOM]

Convertir l'adresse IP et le port en format hexadécimal.

options:
  -h, --help       show this help message and exit
  --ip IP          Adresse IP à convertir
  --port PORT      Port à convertir
  --random RANDOM  Aléatoire au milieu du shellcode afin d'éliminer les paternes | --random yes
```


J'ai divisé le projet en plusieurs composants :

- `choix_part0.py`
- `...`
- `choix_part6.py`

Ces fichiers sont reliés via `choix_général.py`.

Enfin, le fichier `func_instru.py` gère la partie métamorphique du programme.


