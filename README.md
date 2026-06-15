# ASM-Compiler

Compilateur assembleur vers code machine 32 bits pour x86

## Fonctionnalités

- Lecture de fichiers asm
- Parsing de fichiers
- Détection d'opcodes
- Opcode MOV
- Opcode RET

## Technologies

- x86 Assembly
- x86 Machine Code
- NASM

## Compilation

`python compiler.py` <br>
Le script va prendre le fichier **Program/program.asm** et produire un binaire **out.bin** <br>
La compilation a des gestions d'erreur, il suffit d'avoir python et la librairie struct

## Le Projet

Ce projet de compilateur est présent pour mon premier gros projet, mon OS [Oscour](https://github.com/MathNosseb/OScour). Il compile des programmes en 32bits, j'ai voulu en refaire un malgré que **nasm** fonctionne très bien pour pouvoir comprendre le fonctionnement d'un compilateur mais aussi pour plus tard pouvoir l'implémenter dans mon OS et pouvoir compiler des programmes depuis celui-ci. <br>
Le code parse les instructions, pour le moment seul **RET** et **MOV** sont supportés, c'est déjà
suffisant pour écrire un script qui affiche **A** en blanc sur fond noir à l'écran.

## Le programme asm

```asm
start:
    mov eax, 0x0F41 ;mise en mémoire du caractère A en blanc sur fond noir
    mov [0xB8000], eax ;on place le caractère à l'adresse de la mémoire vidéo
    ret ;retour au programme C
```

