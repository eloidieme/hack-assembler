import sys
from parse_asm import parse
from symbol_table import make_st
from tables import COMP_TABLE, DEST_TABLE, JUMP_TABLE

def handle_instruction(inst):
    if inst[0] == '@':
        bin_part = str(bin(int(inst[1:])))[2:]
        if len(bin_part) < 15:
            bin_part = '0'*(15 - len(bin_part)) + bin_part
        return '0' + bin_part + '\n'
    else:
        dest, comp, jump = '', '', ''
        if '=' not in inst and ';' not in inst:
            comp = inst
        elif ';' not in inst:
            [dest, comp] = inst.split('=')
        elif '=' not in inst:
            [comp, jump] = inst.split(';')
        else:
            [dest, after_eq] = inst.split('=')
            [comp, jump] = after_eq.split(';')
        final = '111'
        final += COMP_TABLE[comp]
        final += DEST_TABLE[dest]
        final += JUMP_TABLE[jump]
        return final + '\n'
    
def translate(instruct_list, symbol_t):
    translated = []
    current = 16
    for inst in instruct_list:
        if inst[0] == '@':
            try:
                translated.append(handle_instruction(inst))
            except ValueError:
                if inst[1:] not in symbol_t.keys():
                    symbol_t[inst[1:]] = current
                    current += 1
                final_inst = handle_instruction('@' + str(symbol_t[inst[1:]]))
                translated.append(final_inst)
        elif inst[0] == '(':
            continue
        else:
            translated.append(handle_instruction(inst))
    return translated

def main(path, out):
    clean = parse(path)
    symbol_table = make_st(clean)
    binary = translate(clean, symbol_table)
    with open(out, 'w') as out:
        out.writelines(binary)

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
