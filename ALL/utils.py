
def find(l :list, item)->int:
    for i in range(len(l)):
        if l[i] == item:
            return i
    return -1

def insert(string: str, char: str, index: int):
    str_out=''
    for i in range(len(string)):
        if i != index:
            str_out += string[i]
        else:
            str_out += char
    
    return str_out

def remove_items(l :list, item)->list:
    return [i for i in l if i!= item]

def format_line(line: str):
    line=line.replace('\n', '')
    line = line.split(' ')
    line = remove_items(line, '')
    return line