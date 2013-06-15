"""
Expressões regulares utilizadas para avaliar a sintaxe da linguagem.
"""
aoperadores="(?:\+|\-|\*|/)"
boperadores="(?:(?:and)|(?:or)|(?:==)|(?:\>={0,1})|(?:\<={0,1})|(?:not)|(?:!=))"
types="(?:(?:int)|(?:float)|(?:void))"

var="(?:[a-zA-Z]+[a-zA-Z0-9]*)"
avar="-{0,1}(?:[a-zA-Z]+[a-zA-Z0-9]*)"
num="(?:[0-9]+\.{0,1}[0-9]*)"
anum="-{0,1}(?:[0-9]+\.{0,1}[0-9]*)"
varornum="(?:%s|%s)"%(var, num)

avarornum="-{0,1}(?:%s|%s)"%(var, num)
bvarornum="(?:not){0,1}(?:%s|%s)"%(var, num)

boolexpr="(?: *%s *%s *%s *)+ *"%(bvarornum, boperadores, bvarornum)
aritexpr="(?: *%s *%s *%s *)+ *"%(avarornum, aoperadores, avarornum)

ifline="^ *if *\( *(%s) *\) *: *$"%(boolexpr)
elseline="^ *else: *$"
endif="^ *endif *$"
func="(?:(%s)\( *((?: *)|(?:%s)|(?:(?: *%s, *%s *)+)) *\) *)"%(var, avarornum, avarornum, avarornum)
funcline="^ *%s *$"%(func)
declare="^ *(%s) +(%s) *(?::= *((?:%s)|(?:%s)|(?:%s))){0,1} *$"%(types, var, aritexpr, func, avarornum)
deffunc="^ *def +(%s)\( *((?: *)|%s +%s|(?: *%s +%s, *%s +%s *)) *\) *: *$"%(var, types, var, types, var, types, var)
returnline="^ *return +(%s) *$"%avarornum
endfunc="^ *endfunc *$"
attr="^ *(%s) *:= *((?:%s)|(?:%s)|(?:%s)) *$"%(var, aritexpr, func, avarornum)

