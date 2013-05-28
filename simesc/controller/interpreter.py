#coding=UTF-8
import re

class Interpreter:
    '''
    Classe abstrata que define os métodos e atributos básicos para um interpretador
    '''
    ##############
    # Attributes #
    ##############
    __code__ = []
    __position__ = 0
    __stack__ = []
    __memory__ = {}

    ############################
    # Constructors/Destructors #
    ############################

    def __init__(self, code=None,  ):
        pass

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
    def memory(self):
        return self.__memory__
    
    ###########
    # Setters #
    ###########

    #################
    # Class Methods #
    #################

    ############################
    # Instance Private Methods #
    ############################

    def __syntax_analyzer__(self):
        pass 

    ##############################
    # Instance Protected Methods #
    ##############################

    def _increment_position_(self):
        self.position = self.position+1

    def _eval_current_lite_(self): 
        self._eval_line_(self.position)

    def _eval_line_(self, i):
        self._eval_(self.code[self.position])

    def _eval_(self, code):
        pass

    ###########################
    # Instance Public Methods #
    ###########################

    def step(self, code):
        self._increment_position()
        self._eval_current_line()

    def reload_code(self, code):
        pass

