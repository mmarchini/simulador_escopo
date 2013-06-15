#coding=UTF-8
import re
from memory import Memory, Variable, MemoryFrame
import copy
import syntax


class Interpreter(Memory):
    '''
    Classe abstrata que define os métodos e atributos básicos para um interpretador,
    deixando os métodos que retornam variáveis como métodos abstratos, pois a implementação
    dos mesmos define se o interpretador possuí escopo estático ou dinâmico.
    '''

    __scope = []

    ###############
    # Constructor #
    ###############

    def __init__(self, code=None, **kw):
        super(Interpreter, self).__init__(code, **kw)

    ###########
    # Getters #
    ###########

    @property
    def scope(self):
        return copy.deepcopy(self.__scope)

    ###########
    # Setters #
    ###########

    @scope.setter
    def scope(self, value):
        self.__scope = value

    ##############################
    # Instance Protected Methods #
    ##############################

    def _increment_position(self):
        self.position = self.position+1

    def _eval_current_line(self): 
        self.position = self._eval_line(self.position)

    def _eval_line(self, i):
        """
        Esse método é responsável por executar o código presente na linha 'i' do interpretador. 
        """
        # IF
        if re.compile(syntax.ifline).match(self.code[i]):
            boolexpr = re.compile(syntax.ifline).match(self.code[i]).groups()[0]
            if eval(boolexpr, self.variables):
                self.scope = self.scope + ["if"]
            else:
                flag = True 
                while (flag):
                    i=i+1
                    if re.compile(syntax.elseline).match(self.code[i]):
                        self.scope = self.scope + ["else"]
                        flag=False
                    elif re.compile(syntax.endif).match(self.code[i]):
                        flag=False
                self.position = i
        # ELSE
        elif re.compile(syntax.elseline).match(self.code[i]):
            while not (re.compile(syntax.endif).match(self.code[i])):
                i = i+1
            self.position = i
            self.destroy_current_scope()
        # ENDIF
        elif re.compile(syntax.endif).match(self.code[i]):
            self.destroy_current_scope()
        # DEF FUNCTION
        elif re.compile(syntax.deffunc).match(self.code[i]):
            a=re.compile(syntax.deffunc).match(self.code[i]).groups()[0]
            self.define_variable(a,"function")
            var = self.variable(a)
            var.value = i

            while(not re.compile(syntax.endfunc).match(self.code[i])):
                i = i + 1
            self.position = i
        # RETURN
        elif re.compile(syntax.returnline).match(self.code[i]):
            mf = self._stack.pull()
            if mf.return_var:
                mf._MemoryFrame__return_var.value = eval(re.compile(syntax.returnline).match(self.code[i]).groups()[0], self.variables)  # Quebrando encapsulamento por uma boa causa
            self.destroy_current_scope()
            self.position = mf.callback
            self.scope = mf.scope
            i = mf.callback
        # END FUNCTION
        elif re.compile(syntax.endfunc).match(self.code[i]):
            mf = self._stack.pull()
            if mf.return_var:
                raise Exception
            self.destroy_current_scope()
            self.position = mf.callback
            self.scope = mf.scope
            i = mf.callback
        # DECLARE
        elif re.compile(syntax.declare).match(self.code[i]):
            groups=re.compile(syntax.declare).match(self.code[i]).groups()
            self.define_variable(groups[1],groups[0])
            if groups[2]:
                self._declare(groups[1], groups[2])
        # ATTRIBUTION
        elif re.compile(syntax.attr).match(self.code[i]):
            groups = re.compile(syntax.attr).match(self.code[i]).groups()
            if re.compile(syntax.var).match(groups[0]):
                self._declare(groups[0], groups[1])
            else:
                raise SyntaxError
        # EXCECUTE FUNCTION
        elif re.compile(syntax.funcline).match(self.code[i]):
            #TODO armazenar a variável que vai ser alterada na pilha, e a linha atual
            func_groups = re.compile(syntax.func).match(expr).groups()
            func_attrs = [eval(a, self.variables) for a in func_groups[1].replace(" ", "").split(",")]
            mf = MemoryFrame(callback=self.position, parameters=func_attrs, scope=self.scope, function_name=func_groups[0])
            self._stack.push(mf)
            self.scope = self.scope + [func_groups[0]]
            self.position = self.variable(func_groups[0]).value
            self.scope= self.variable(func_groups[0]).scope
            params = re.compile(" *, *").split(re.compile(syntax.deffunc).match(self.code[self.position]).groups()[1])
            for i,param in enumerate(params):
                param = re.compile(" +").split(param)
                self.define_variable(param[1], param[0])
                param_var = self.variable(param[1])
                param_var.value = func_attrs[i]
        # NADA
        elif re.compile("^ *$").match(self.code[i]):
            pass
        # ERRO DE SINTAXE
        else:
            raise SyntaxError
        if i == self.position:
            return i 
        else:
            return self.position
            
    def _declare(self, varname, varvalue):
        """
        Esse método é responsável por atribuir valores as variáveis.
        """
        var = self.variable(varname)
        expr = varvalue 
        if var:
            """
            Verifica qual o tipo da atribuição
            """
            # Retorno de Função
            if re.compile(syntax.func).match(expr):
                #TODO armazenar a variável que vai ser alterada na pilha, e a linha atual
                func_groups = re.compile(syntax.func).match(expr).groups()
                func_attrs = [eval(a, self.variables) for a in func_groups[1].replace(" ", "").split(",")]
                mf = MemoryFrame(callback=self.position, returnvar=var, parameters=func_attrs, scope=self.scope, function_name=func_groups[0])
                self._stack.push(mf)
                self.scope = self.scope + [func_groups[0]]
                self.position = self.variable(func_groups[0]).value
                params = re.compile(" *, *").split(re.compile(syntax.deffunc).match(self.code[self.position]).groups()[1])
                for i,param in enumerate(params):
                    param = re.compile(" +").split(param)
                    self.define_variable(param[1], param[0])
                    param_var = self.variable(param[1])
                    param_var.value = func_attrs[i]

            # Avaliação de uma Expressão Aritmética
            elif re.compile(syntax.aritexpr).match(expr):
                var.value = eval(expr, self.variables)

            # Variável 
            elif re.compile(syntax.avar).match(expr):
                var2 = self.variable(expr)
                if var2 and var2.value:
                    var.value = var2.value
                else:
                    raise Exception
            # Número 
            elif re.compile(syntax.anum).match(expr):
                var.value = eval(expr)
            else:
                raise SyntaxError
        else:
            raise AttributeError


    ###########################
    # Instance Public Methods #
    ###########################

    def step(self):
        """
        Método responsável por executar a linha atual e avançar para a próxima linha.
        """
        if self.position < len(self.code):
            self._eval_current_line()
            self._increment_position()

    def define_variable(self, name, vartype):
        """
        Método responsável por alocar uma variável no monte.
        """
        if name == "int":
            raise Exception
        var = Variable(name, vartype, self.scope, self.position)
        self._mount.push(var)

    def destroy_current_scope(self):
        """
        Método responsável por apagar todas as variáveis que foram alocadas no monte no escopo atual,
        e voltar para o escopo anterior.
        """
        self._mount.remove(self.scope, lambda a: a.scope)
        self.scope = self.scope[:-1]

