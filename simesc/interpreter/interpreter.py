#coding=UTF-8
import re
from memory import Memory



"[[\+\-\*\/>[=]{0,1} <[=]{0,1} =[=]{0,1} & |] ]*"

class Interpreter(Memory):
    '''
    Classe que define os métodos e atributos básicos para um interpretador
    '''

    ###############
    # Constructor #
    ###############

    def __init__(self, code=None,  ):
        pass

    ############################
    # Instance Private Methods #
    ############################

    def __syntax_analyzer(self):
        pass 

    ##############################
    # Instance Protected Methods #
    ##############################

    def _increment_position_(self):
        self.position = self.position+1

    def _eval_current_lite(self): 
        self._eval_line(self.position)

    def _eval_line(self, i):
        self._eval(self.code[self.position])

    def _eval(self, code):
        if re.compile("").match(code):
            pass

    ###########################
    # Instance Public Methods #
    ###########################

    def step(self, code):
        self._increment_position()
        self._eval_current_line()

    def reload_code(self, code):
        pass
