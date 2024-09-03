"""
* EJERCICIO:
     - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
       su tipo de dato.
     - Muestra ejemplos de funciones con variables que se les pasan "por valor" y
      "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
      (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)

 * DIFICULTAD EXTRA (opcional):
     -Crea dos programas que reciban dos parámetros (cada uno) definidos como
      variables anteriormente.
     - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
       Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
       se asigna a dos variables diferentes a las originales. A continuación, imprime
       el valor de las variables originales y las nuevas, comprobando que se ha invertido
       su valor en las segundas.
       Comprueba también que se ha conservado el valor original en las primeras.
"""
from typing import Tuple

# Paso por valor (Enteros)
a:int = 5
def comprobar_id(entrada):
    entrada = 0
    print(id(entrada))
comprobar_id(a)
print(id(a))

# Paso por referencia (listas)
lista = [10, 20, 30]
def comprobar_id_ref(entrada):
    print(id(entrada))
    entrada.append(40)
comprobar_id_ref(lista)
print(id(lista))
print(a)
print(lista)

val1:int = 4
val2:int = 6
ref1:list = [10, 20, 30]
ref2:list = [40, 50, 60]
def programa_1(valor_1:int, valor_2:int) -> tuple:
    temp:int = valor_1
    valor_1 = valor_2
    valor_2 = temp
    return valor_1, valor_2

def programa_2(referencia1:list, referencia2:list) -> tuple[list, list]:
    temp:list = referencia1
    referencia1 = referencia2
    referencia2 = temp
    return referencia1, referencia2

valor1,valor2  = programa_1(val1, val2)
ref_1, ref_2 = programa_2(ref1, ref2)
print(valor1, valor2)
print(ref_1, ref_2)
