#coding=UTF-8
"""
Implementação de uma classe de Pilha parametrizada
"""
import copy

class Stack(object):
    """
    Classe de Pilha.
    O Tipo dos Elementos da Pilha é definido na criação do Objeto da Classe,
    e todos os elementos alocados nessa pilha devem ser do tipo escolhido.
    """
    ##############
    # Attributes #
    ##############
    __type = None
    __stack = []
    
    def __init__(self, _type):
        self.__type = _type
        self.__stack = []
        
    def push(self, value):
        if type(value) == self.__type:
            self.__stack.append(value)
        else:
            raise TypeError
        
    def pull(self):
        return self.__stack.pop()

    @property
    def stack(self):
        return copy.deepcopy(self.__stack)

    def search(self, key, keyfunc=None):
        aux = []
        if keyfunc:
            for a in self.__stack:
                if keyfunc(a) == key:
                    aux.append(a) 
        else:
            for a in self.__stack:
                if a == key:
                    aux.append(a)
        return aux

    def remove(self, key, keyfunc=None):
        if keyfunc:
            for a in self.__stack:
                if keyfunc(a) == key:
                    self.__stack.remove(a) 
        else:
            for a in self.__stack:
                if a == key:
                    self.__stack.remove(a)

