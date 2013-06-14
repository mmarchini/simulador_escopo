#coding=UTF-8
from interpreter import Interpreter
import copy

class StaticInterpreter(Interpreter):

    def __init__(self, code, **kw):
        super(StaticInterpreter, self).__init__(code, **kw)
 
    @property
    def variables(self):
        aux = self.mount.stack
        for a in aux:
            print a.name
            print a.value
            print a.scope
        b = {}
        scopes = copy.deepcopy(self.scope)
        aux_scope = []
        for scope in scopes:
            print ">",aux_scope
            variables = self.mount.search(aux_scope, lambda a: a.scope)
            for var in variables:
                if var.line < self.position:
                    b[var.name]=var.value
            aux_scope.append(scope)
        variables = self.mount.search(aux_scope, lambda a: a.scope)
        for var in variables:
            if var.line < self.position:
                b[var.name]=var.value
        return b 

    def variable(self, var):
        aux = self.mount.search(var, lambda a: a.name)
        return aux and aux[-1] or none

