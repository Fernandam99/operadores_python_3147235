# operadores en python
''' los operadores en python siguen el siguiente orden jeraquico:
1. ()
2. ** exponente
3. / , * , %,
4. + , -
5. =
nota 1: si hay operaciones en el mismo nivel de jerarquia se resuelven de izquierda a derecha
nota 2: si hay parentesis detro del paresis se resuelve primero el parentesis interno
'''

a = 3
b = 2
c = 1
x = 5

y = ((2*a+c)/7)*(a+(9*a)/c)
print(y)