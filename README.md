# ASM-Compiler

Compilateur assembleur vers code machine 32 bits pour x86

## Fonctionnalités

- Lecture de fichiers asm
- Parsing de fichiers
- Détection d'opcodes
- Opcode MOV
- Opcode RET
- Opcode CALL
- Opcode PUSH
- Opcode POP

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
    mov eax, 0x6C6C6548; les lettres Hell en little endian
    mov [0x520], eax; on met les lettres dans la memoire a un espace libre
    ;le placement dans la mémoire est fait avec un espace toujours libre mais
    ;attention car ça peut corompre la mémoire d'écrire n'importe ou
    ;il vaut mieux ecrire dans la stack et recuperer le pointeur avec esp
    mov eax, 0x6F77206F ; lettres o wo
    mov [0x524], eax; placer en memoire
    mov eax, 0x21646C72; rld!
    mov [0x528], eax; placer en memoire
    mov eax, 0x00; 0, fin de string
    mov [0x532], eax; mettre en memoire
    mov eax, [0x504]; mettre l adresse de la fonction sys print OScour dans eax
    mov ecx, 0x520; mettre l adresse de la string dans ecx
    push ecx ; mettre ecx sur la stack
    call eax; appel de la fonction systeme print
    pop ecx ; decrementer le stack pointer
    ret ; revenir au code C
```

