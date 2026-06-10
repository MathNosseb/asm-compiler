opcodes = {
    "mov_eax_imm" : b"\xB8"
}


def assemble(filename):
    lines = open(filename).read().splitlines()
    for command in lines:
        if command.endswith(':'):
            continue #skip pour le moment
        opcodes = command.replace(",", "").split()

        mnemonic = opcodes[0]
        op1 = opcodes[1]

        op2 = ""
        if len(opcodes) > 2:
            op2 = opcodes[2]

        if mnemonic == "mov":
            if op1 == "eax":
                print("MOV EAX, IMM")
    


assemble("program.asm")
