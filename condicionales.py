'''
CONDICIONAL:
Expresion que, al ser evaluada,
da como resultado un valor verdadero o falso.
Por tanto, en una condicional deben haber
operadores relacionales o logicos
'''
#Ejemplo de condicional
a = 3
b = 2
c = 1
d = 4
resultado = not (a ** 2 -b > c ** 2) and (( a * 3 + c ) / 2 < d) or True 
print(resultado)

#Ejemplo de condicional
x = 5
y = 10
z = 5

resultado = (x == z + ( 8 / z) ) and not ((y + 3) * ( 4 / (z + 1)) ) == z
print (resultado)

#Ejemplo de condicional
a = 6
b = 3
c = 7
d = 4
e = 5

resultado = not (a + b  >  c / d) or e * 2 != d + c and not (a < b)
print(resultado)