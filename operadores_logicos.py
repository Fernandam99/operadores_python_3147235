'''
OPEADORES LOGICOS
Los operadores logicos son: and, or, not
obedecen las ttablas de verdad:

'''

op1 = False
op2 = True
op3 = op1 or op2
print(op3)

#Operador not
op4 = not op2
print (op4)

''' 
GERANQUIA DEFINITIVA DE OPERDORES
1       ()
2       **
3      +,/,%
4       +,-
5 >,<,!=,==,<=,>=
6       not
7       and
8        or
9        =

Nota: si hay operciones en el miso nivel dejerarqui se resuelven de izquierda a derecha
'''
op1 = False
op2 = True
op3 = False
op4 = True

resultado = not op1 and (op2 or op3 and not op1) and not op4

print(resultado)