#coding=UTF-8
"""
Implementação de uma classe de Pilha parametrizada
"""

class Stack(object):
    __type__ = None
    __stack__ = []
    
    def __init__(self, _type):
        self.__type__ = _type
        
    def push(self):
        pass
        
    def pull(self):
        pass
        
    @property
    def stack(self):
        pass
