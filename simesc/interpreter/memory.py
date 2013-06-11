from abc import ABCMeta, abstractmethod, abstractproperty
from stack import Stack

class MemoryFrame(object):
    __callback = -1
    __function_name = ""
    return_var = None
    parameters = []

    ###############
    # Constructor #
    ###############    
    
    def __init__(self, callback, function_name, parameters, returnvar=None):
        self.callback = callback
        self.function_name = function_name
        self.return_var = returnvar 
        self.parameters=parameters
    
    ###########
    # Getters #
    ###########
    
    @property
    def callback(self):
        return self.__callback

    @property
    def function_name(self):
        return self.__function_name

    ###########
    # Setters #
    ###########

    @callback.setter
    def callback(self, value):
        self.__callback = value

    @function_name.setter
    def function_name(self, value):
        self.__function_name = value
        
class Variable(object):
    name = ""
    vartype = None
    value = 0 
    scope=[]

    def __init__(self, name, vartype, scope):
        self.name = name
        self.vartype = vartype
        self.scope = scope

class Memory(object):
    __metaclass__ = ABCMeta
    
    ##############
    # Attributes #
    ##############
    __position = 0
    __code = []
    __stack = None
    __mount = None
    
    ###############
    # Constructor #
    ###############
    
    def __init__(self, code=None):
        self.stack = Stack(MemoryFrame)
        self.mount = Stack(Variable)
        
        self.code = code
        
    ###########
    # Getters #
    ###########
    
    @property
    def code(self):
        return self.__code

    @property
    def position(self):
        return self.__position
        
    @property
    def stack(self):
        return self.__stack

    @property
    def mount(self):
        return self.__mount

    @abstractproperty
    def variables(self):
        pass
    
    ###########
    # Setters #
    ###########

    @code.setter
    def code(self, value):
        if type(value) == str or type(value) == unicode:
            self.__code = value.split("\n")
        elif type(value) == list:
            self.__code = value
        else:
            raise TypeError

    @position.setter
    def position(self, value):
        self.__position = value
        
    @stack.setter
    def stack(self, value):
        self.__stack = value

    @mount.setter
    def mount(self, value):
        self.__mount = value

    ####################
    # Abstract Methods #
    ####################
    
    @abstractmethod
    def define_variable(self):
        pass

