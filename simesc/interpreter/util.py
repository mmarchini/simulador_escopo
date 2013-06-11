#coding=UTF-8

def code_from_array(array, arrow_line=-1):
    spaces = len(str(len(array)))
    code = """"""
    i=0
    for line in array:
        if i==arrow_line:
            code = code+">%s%d %s"%(" "*(1+spaces-len(str(i))), i, line)
        else:
            code = code+"%s%d %s"%(" "*(2+spaces-len(str(i))), i, line)
        i=i+1
    return code
    

def load_file(filename, syntax_analyzer=None):
    new_file = open(filename)
    buffer = []
    aux = new_file.readline()
    while(aux):
        buffer.append(aux)
        aux = new_file.readline()
    
    return buffer

