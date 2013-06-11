#coding=UTF-8
from interpreter import Interpreter

class StaticInterpreter(Interpreter):

    def __init__(self, code, **kw):
        super(StaticInterpreter, self).__init__(code, **kw)
