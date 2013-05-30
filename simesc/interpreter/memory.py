from abc import ABCMeta, abstractmethod, abstractproperty
from stack import Stack

class MemoryStack(object):
    pass

class MemoryReference(object):
    pass

class Memory(object):
    __metaclass__ = ABCMeta
    
    __code__ = []
    __position__ = 0
    __stack__ = None
    __mount__ = None
    
    def __init__(self, **kw):
        self.__stack__ = Stack(MemoryStack)
        self.__mount__ = Stack(MemoryReference)
        
    ###########
    # Getters #
    ###########
    
    @property
    def code(self):
        return self.__code__

    @property
    def position(self):
        return self.__position__
        
    @property
    def stack(self):
        return self.__stack__

    @property
    def mount(self):
        return self.__mount__
    
    ###########
    # Setters #
    ###########

    @code.setter
    def code(self, value):
        self.__code__ = value

    @position.setter
    def position(self, value):
        self.__position__ = value
        
    @stack.setter
    def stack(self, value):
        self.__stack__ = value

    @mount.setter
    def mount(self, value):
        self.__mount__ = value
