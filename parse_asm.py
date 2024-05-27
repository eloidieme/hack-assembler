
def remove_comment(string):
    new_str = None
    for i in range(len(string) - 1):
        if string[i] == '/' and string[i+1] == '/':
            new_str = string[:i].strip()
            break
    if new_str is None:
        new_str = string
    return new_str

def parse(path):
    with open(path, 'r') as src:
        source_code = src.readlines()

    source_code = [line.strip() for line in source_code]
    no_coms = [remove_comment(line) for line in source_code]
    clean = [line for line in no_coms if (line != '' and line != ' ')]
    return clean