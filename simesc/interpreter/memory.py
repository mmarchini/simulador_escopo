from abc import ABCMeta, abstractmethod, abstractproperty
from stack import Stack

class MemoryStack(object):
    pass

class MemoryReference(object):
    pass

class Memory(object):
    __metaclass__ = ABCMeta
    ##############
    # Attributes #
    ##############
    __position__ = 0
    __code__ = []
    __stack__ = None
    __mount__ = None
    
    ###############
    # Constructor #
    ###############
    
    def __init__(self, code=None):
        self.__stack__ = Stack(MemoryStack)
        self.__mount__ = Stack(MemoryReference)
        
        self.code = code
        
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
        if type(value) == str or type(value) == unicode:
            self.__code__ = value.split("\n")
        elif type(value) == list:
            self.__code__ = value
        else:
            raise TypeError

    @position.setter
    def position(self, value):
        self.__position__ = value
        
    @stack.setter
    def stack(self, value):
        self.__stack__ = value

    @mount.setter
    def mount(self, value):
        self.__mount__ = value
