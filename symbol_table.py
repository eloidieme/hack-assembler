def make_st(instruct_list):
    symbol_t = {f'R{i}': i for i in range(16)}
    symbol_t['SCREEN'] = 16384
    symbol_t['KBD'] = 24576
    symbol_t['SP'] = 0
    symbol_t['LCL'] = 1
    symbol_t['ARG'] = 2
    symbol_t['THIS'] = 3
    symbol_t['THAT'] = 4
    count = 0
    for inst in instruct_list:
        if inst[0] == '(':
            symbol_t[inst[1:-1]] = count
        else:
            count += 1
    return symbol_t