#coding=UTF-8
from functional import foldl

def _code_from_array(array, i=0):
    """
    Função Recursiva auxiliar responsável por adicionar os números nas linhas do código.
    """
    if i>=len(array):
        return [] 
    return [str(array[i])%(" "*(2+len(str(len(array)))-len(str(i))), i)]+_code_from_array(array, i+1)

def code_from_array(array, arrow_line=-1):
    """
    Função de Primeira Ordem, pura, onde será aplicado o conceito de Currying.
    Utilização do Lambda e das funções de ordem maior map e foldl
    Essa função é responsável por formatar um Array de código em uma string que será exibida na tela.
    """
    spaces = len(str(len(array)))
    new_array = map(lambda a: "%s%d "+a, array) 
    new_array = _code_from_array(new_array) 
    code = foldl(lambda a,b: a+b, "", new_array)
    return code

def load_file(filename):
    """
    Função responsável por abrir um arquivo no formato da linguagem, sem verificação sintática.
    Entrada: nome do arquivo
    Saída: Array com as linhas de código do arquivo.
    """
    new_file = open(filename)
    buffer = []
    aux = new_file.readline()
    while(aux):
        buffer.append(aux)
        aux = new_file.readline()
    
    return buffer

