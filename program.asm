mov eax, 0x6C6C6548
mov [0x520], eax
mov eax, 0x6F77206F
mov [0x524], eax
mov eax, 0x21646C72
mov [0x528], eax
mov eax, 0x00
mov [0x532], eax
mov eax, [0x504]
mov ecx, 0x520
push ecx
call eax
pop ecx
ret
