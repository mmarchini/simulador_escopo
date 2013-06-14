#coding=UTF-8
from functional import foldl

def _code_from_array(array, i=0):
    if i>=len(array):
        return [] 
    return [str(array[i])%(" "*(2+len(str(len(array)))-len(str(i))), i)]+_code_from_array(array, i+1)

def code_from_array(array, arrow_line=-1):
    """
    Função de Primeira Ordem, pura, onde será aplicado o conceito de Currying.
    """
    spaces = len(str(len(array)))
    new_array = map(lambda a: "%s%d "+a, array) 
    new_array = _code_from_array(new_array) 
    code = foldl(lambda a,b: a+b, "", new_array)
    return code

def load_file(filename, syntax_analyzer=None):
    new_file = open(filename)
    buffer = []
    aux = new_file.readline()
    while(aux):
        buffer.append(aux)
        aux = new_file.readline()
    
    return buffer

