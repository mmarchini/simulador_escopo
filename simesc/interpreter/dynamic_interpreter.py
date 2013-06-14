#coding=UTF-8
from interpreter import Interpreter

class DynamicInterpreter(Interpreter):
    
    def __init__(self, code, **kw):
        super(DynamicInterpreter, self).__init__(code, **kw)
 
    @property
    def variables(self):
        aux = self.mount.stack
        b = {}
        for a in aux:
            b[a.name]=a.value
        return b 

    def variable(self, var):
        aux = self.mount.search(var, lambda a: a.name)
        return aux and aux[-1] or none

