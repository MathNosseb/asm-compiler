import struct

table_mod = {
    "mem" : 0b00,
    "mem_8bits" : 0b01,
    "mem_32bits" : 0b10,
    "reg" : 0b11,

}

registers = {
    "eax": 0b000,
    "ecx": 0b001,
    "edx": 0b010,
    "ebx": 0b011,
    "esp": 0b100,
    "ebp": 0b101,
    "esi": 0b110,
    "edi": 0b111
}

def modRM(mnemonic, op1, op2, line_number):
    mod = 0b0
    reg = 0b0
    rm = 0b0
    if (op1.startswith("[") and op1.endswith("]")) and (op2.startswith("[") and op2.endswith("]")):
        raise Exception("IMPOSSIBLE D AVOIR DEUX ADRESSES, PASSE PAR UN REGISTRE ",line_number)
    #on calcul le mod
    #mod (2bits) reg (3bits) r/m(3bits)
    #4 choix pour le mod, 00, 01, 10, 11

    #pour 00 c'est uniquement quand on accede a de la memoire sans déplacement
    if (op1.startswith("[") and op1.endswith("]")) or (op2.startswith("[") and op2.endswith("]")):
        #si on detecte un changement de memoire dans op1 ou op2
        #le mod sera 0x00
        #LE DEPLACEMENT DE MEMOIRE N EST PAS ENCORE SUPPORTE
        mod = table_mod["mem"]
    else:
        #pas de deplacement memoire -> registre direct
        mod = table_mod["reg"]


    #quand on a de la memoire dans le code et pas des registres on les stockes
    op1_mem_adr = 0b0
    op2_mem_adr = 0b0

    memory_executed = False

    #on calcul le reg
    #on verifie que c'est pas une adresse (deplacement dans une adresse)
    #ex mov [0x100], ...
    #si c'est le cas (detection)
    if op1.startswith("[") and op1.endswith("]"):
        #on detecte une adresse memoire
        #LE DEPLACEMENT DE MEMOIRE N EST PAS ENCORE PRIS EN COMPTE
        adr = op1.removeprefix("[").removesuffix("]")
        op1_mem_adr = int(adr,0)
        rm = 0b101
        reg = registers[op2]
        memory_executed = True
    else:
        #on est en registre direct
        if op1 in registers:
            reg = registers[op1]
        else:
            raise Exception("REGISTRE NON TROUVE ",line_number)
    
    #on calcul le rm
    #on verifie que c'est pas une adresse (deplacement dans une adresse)
    #ex mov ..., [0x100]
    #si c'est le cas (detection)
    if not memory_executed:
        if op2.startswith("[") and op2.endswith("]"):
            #on detecte une adresse memoire
            #LE DEPLACEMENT DE MEMOIRE N EST PAS ENCORE PRIS EN COMPTE
            adr = op2.removeprefix("[").removesuffix("]")
            op2_mem_adr = int(adr,0)
            rm = 0b101
            reg = registers[op1]
        else:
            #on est en registre direct
            if op2 in registers:
                rm = registers[op2]
            else:
                raise Exception("REGISTRE NON TROUVE ",line_number)


    octet = mod << 6 | reg << 3 | rm
    return (octet, op1_mem_adr, op2_mem_adr)

def assemble(filename):
    lines = open(filename).read().splitlines()
    line_number = 1
    output = b""
    for command in lines:
        if command.endswith(':'):
            continue #skip pour le moment
        tokens = command.replace(",", "").split()

        mnemonic = tokens[0]


        op1 = ""
        if len(tokens) > 1:
            op1 = tokens[1]

        op2 = ""
        if len(tokens) > 2:
            op2 = tokens[2]
        
        
        if mnemonic == "mov":

            #detection si on a besoin de mod rm
            try:
                int(op2,0)
                #on bouge une valeur
                #op2 imm32
                output += bytes([0xB8 + registers[op1]])
                output += struct.pack("<I", int(op2, 0))
            except ValueError:
                #on recupere toutes les valeurs
                modrm_byte, op1_mem_adr, op2_mem_adr = modRM(mnemonic, op1, op2, line_number)

                #assignation des differents opcodes de modrm
                if op1_mem_adr != 0:
                    output += bytes([0x89])#registre vers memoire
                elif op2_mem_adr != 0:
                    output += bytes([0x8B])#memoire vers registre
                else:
                    raise Exception("ERREUR INCONNU ", line_number)
                
                output += bytes([modrm_byte])

                if op1_mem_adr != 0:
                    output += struct.pack("<I", op1_mem_adr)#registre vers memoire
                elif op2_mem_adr != 0:
                    output += struct.pack("<I", op2_mem_adr)#memoire vers registre
                else:
                    raise Exception("ERREUR INCONNU ", line_number)
           
        elif mnemonic == "ret":
            output += bytes([0xC3])

            
        line_number+=1
    

    return output

    
def write_bin(content, filename):
    with open(filename, "wb") as f:
        f.write(content)

data = assemble("Program/program.asm")
write_bin(data, "program.bin")
print("compilation done !")