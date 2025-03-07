'''
OPERADORES LOGICOS
Los operadores logicos son:
and , or , not
obedecen las tablas de verdad:

'''
op1 = False
op2 = True
op3 = op1 or op2
print(op3)

#operador not
op4 = not op2
print(op4)

'''
JERARQUIA DEFINITIVA DE OPERADORES
1.          ()
2.          **
3.      * , / , %
4.         + , - 
5.  >, < , != , == , <= , >=
6.          NOT
7.          AND
8.           0R
9.           =
NOTA: Si hay operaciones en el mismo nivel
de jerarquía, se resuelven de izquierda a derecha
'''

op1 = False
op2 = True
op3 = False
op4 = True

resultado = not op1 and (op2 or op3 and not op1) and not op4