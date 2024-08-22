"""
EJERCICIO:
 - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
   que representen todos los tipos de estructuras de control que existan
   en tu lenguaje:
   Condicionales, iterativas, excepciones...
 - Debes hacer print por consola del resultado de todos los ejemplos.

 * DIFICULTAD EXTRA (opcional):
- Crea un programa que imprima por consola todos los números comprendidos
  entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
"""
import math

num_1 = int(input("Introduce el primer número \n"))
num_2 = int(input("Introduce el segundo número \n"))
separador = "****"
print(f"{separador} Aritméticos {separador}")
print(f"suma: {num_1 + num_2}")
print(f"resta: {num_1 - num_2}")
print(f"multiplicación: {num_1 * num_2}")
print(f"division: {num_1 / num_2}")
print(f"potencia: {num_1 ** num_2}")
print(f"modulo: {num_1 % num_2}")
print(f"cociente: {num_1 // num_2}")
print("\n")

print("\n")
print(f"{separador} Lógicos {separador}")
print(True if num_1 > num_2 and num_1 == num_2 else False)
print(True if num_1 > num_2 or num_1 == num_2 else False)
print(not True if num_1 > num_2 else not False)

print("\n")
a = num_1
b = num_2
print("Operadores de asignación")
x=a; x+=b;  print("x+=", x)
x=a; x-=b;  print("x-=", x)
x=a; x*=b;  print("x*=", x)
x=a; x/=b;  print("x/=", x)
x=a; x%=b;  print("x%=", x)
x=a; x//=b; print("x//=", x)
x=a; x**=b; print("x**=", x)
x=a; x&=b;  print("x&=", x)
x=a; x|=b;  print("x|=", x)
x=a; x^=b; print("x^=", x)
x=a; x>>=b; print("x>>=", x)
x=a; x<<=b; print("x<<=", x)

print("\n")
print(f"{separador} Operadores de Identidad {separador}")
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
print(a is b)
print(a is not b)

print("\n")
print(f"{separador} Operadores de pertenencia {separador}")
cadena = "Esto es una prueba"
print("prueba" in cadena)


num = 10
while 10 <= num <= 55:
    if num % 2 == 0 and num != 16 and num %3 != 0:
        print(num)
    num += 1


