#coding=utf-8
from abc import ABCMeta, abstractmethod, abstractproperty
from stack import Stack
from copy import deepcopy

class MemoryFrame(object):
    """
    Classe que representa um Frame de Execução de uma Função na Memória.
    """
    __callback = -1
    __function_name = ""
    __scope = None
    __return_var = None
    __parameters = []

    ###############
    # Constructor #
    ###############    
    
    def __init__(self, callback, function_name, parameters, scope, returnvar=None):
        self.callback = callback
        self.function_name = function_name
        self.return_var = returnvar 
        self.parameters=parameters
        self.scope=scope

    ###########
    # Getters #
    ###########
    
    @property
    def callback(self):
        return deepcopy(self.__callback)

    @property
    def function_name(self):
        return deepcopy(self.__function_name)
    
    @property
    def scope(self):
        return deepcopy(self.__scope)
    
    @property
    def return_var(self):
        return self.__return_var
    
    @property
    def parameters(self):
        return deepcopy(self.__parameters)

    ###########
    # Setters #
    ###########

    @callback.setter
    def callback(self, value):
        self.__callback = value

    @function_name.setter
    def function_name(self, value):
        self.__function_name = value

    @scope.setter
    def scope(self, value):
        self.__scope = value

    @return_var.setter
    def return_var(self, value):
        self.__return_var = value

    @parameters.setter
    def parameters(self, value):
        self.__parameters = value


class Variable(object):
    """
    Classe que representa uma variável alocada na Memória.
    """
    __name = ""
    __vartype = None
    __value = 0 
    __line = -1
    __scope=[]

    def __init__(self, name, vartype, scope, line):
        self.name = name
        self.vartype = vartype
        self.scope = scope
        self.line = line 
    
    ###########
    # Getters #
    ###########
    
    @property
    def vartype(self):
        return deepcopy(self.__vartype)

    @property
    def name(self):
        return deepcopy(self.__name)
    
    @property
    def scope(self):
        return deepcopy(self.__scope)
    
    @property
    def value(self):
        return deepcopy(self.__value)
    
    @property
    def line(self):
        return deepcopy(self.__line)

    ###########
    # Setters #
    ###########

    @vartype.setter
    def vartype(self, value):
        self.__vartype = value

    @name.setter
    def name(self, value):
        self.__name = value

    @scope.setter
    def scope(self, value):
        self.__scope = value

    @value.setter
    def value(self, value):
        self.__value = value

    @line.setter
    def line(self, value):
        self.__line = value


class Memory(object):
    """
    Classe Abstrata que tenta reproduzir a estrutura de uma área de Memória que seria utilizada pelo interpretador de uma linguagem.
    Possuí três métodos abstratos(que devem ser implementados nas classes filhas:
    - variables: é uma property abstrata que retorna um dicionário com as variáveis visíveis no escopo atual.
    - variable: recebe o nome de uma variável e retorna um objeto do tipo Variable que representa essa variável na memória, levando em cosideração o escopo atual.
    - define_variable: aloca uma variável no monte caso ainda não exista uma variável com mesmo nome alocada no escopo atual.
    """
    __metaclass__ = ABCMeta
    
    ##############
    # Attributes #
    ##############
    __position = 0
    __code = []
    _stack = None
    _mount = None
    
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
        return deepcopy(self.__code)

    @property
    def position(self):
        return deepcopy(self.__position)
        
    @property
    def stack(self):
        return deepcopy(self._stack)

    @property
    def mount(self):
        return deepcopy(self._mount)

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
        self._stack = value

    @mount.setter
    def mount(self, value):
        self._mount = value

    ####################
    # Abstract Methods #
    ####################
    
    @abstractmethod
    def define_variable(self):
        pass
    
    @abstractmethod
    def variable(self, var):
        pass

