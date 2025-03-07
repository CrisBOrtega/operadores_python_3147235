# Operadores en python
'''
Los operadores en python 
siguen el siguiente orden jerarquico:
1.                 (   )
2.                   **
3.                / , * , % ,
4.                  + , -
5.                    =
NOTA1: Si hay operaciones en el mismo nivel 
de jerarquía,se resuelven de izquierda
a derecha
NOTA": Si hay parentesis dentro de parentesis
se resuelve primero el parentesis interno
'''
a = 3 
b = 2
c = 1

y = a * 2 ** 3 - a + c - c ** 3 + c
print(y)

'''
OPERADORES RELACIONALES:
Las operaciones aritméticas 
resultan en un valor numerico:
Las operaciones relacionales
resultan en un valor booleano:
True False(V , F SI NO)
Operadores Relacionales:
> , < , >= , <=, != , ==
JERARQUIA DE OPERADORES
(incluyendo los relacionale):
1.            ()
2.            **
3.         * , / , %
4.             + , - 
5.       > , < , >= , <=, != , ==
6.             =
'''
a = 3 
b = 2
c = 1

y = x + 2 * a - c != b + x * a
