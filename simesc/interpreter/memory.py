from abc import ABCMeta, abstractmethod, abstractproperty
from stack import Stack

class MemoryFrame(object):
    __callback__ = -1
    __function_name__ = ""
    __variables__ = []

    ###############
    # Constructor #
    ###############    
    
    def __init__(self, callback, function_name):
        self.callback = callback
        self.function_name = function_name
    
    ###########
    # Getters #
    ###########
    
    @property
    def callback(self):
        return self.__callback__

    @property
    def function_name(self):
        return self.__function_name__
        
    @property
    def variables(self):
        return self.__variables__

    ###########
    # Setters #
    ###########

    @callback.setter
    def callback(self, value):
        self.__callback__ = value

    @function_name.setter
    def function_name(self, value):
        self.__function_name__ = value
        
    @variables.setter
    def variables(self, value):
        self.__variables__ = value

class MemoryReference(object):
    __type__ = None
    __value__ = None
    
    def __init__(self, type, value=0):
        pass
    
class Variable(object):
    __name__ = ""
    __type__ = None
    __value__ = None

class Memory(object):
    __metaclass__ = ABCMeta
    
    ##############
    # Attributes #
    ##############
    __position__ = 0
    __code__ = []
    __stack__ = None
    __mount__ = None
    __variables__ = []
    
    ###############
    # Constructor #
    ###############
    
    def __init__(self, code=None):
        self.stack = Stack(MemoryFrame)
        self.mount = Stack(MemoryReference)
        
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

    ####################
    # Abstract Methods #
    ####################
    
    @abstractmethod
    def load_memory(self, memory):
        pass
