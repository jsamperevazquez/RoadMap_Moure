"""/*
  EJERCICIO:
    - Crea ejemplos de funciones básicas que representen las diferentes
      posibilidades del lenguaje:
      Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
    - Comprueba si puedes crear funciones dentro de funciones.
    - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
    - Pon a prueba el concepto de variable LOCAL y GLOBAL.
    - Debes hacer print por consola del resultado de todos los ejemplos.
     (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)

    DIFICULTAD EXTRA (opcional):
    - Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
    - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
    - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
    - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
    - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
    - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
"""
import sys


def saludo():
    return (f"Hola desde {sys.version}"
    )
def concatenar(texto1, texto2):
    print(texto1 + texto2)

def sumar(num1, num2):
    return num1 + num2

saludo()
concatenar(saludo(), str(sys.api_version))
print(sumar(5, 4))

def operaciones(numero1, numero2):
    print(numero1 * numero2)
    def dividir(num1, num2):
        print( num1 / num2)
    dividir(numero1, numero2)

operaciones(5, 4)

var_global = 20 ## variable global
def cambiar_valor_no():
    nuevo_valor = 30 ##variable local
    var_global = nuevo_valor
    print(var_global)

cambiar_valor_no()
print(var_global)

## Dificultad extra
def contar_cadenas(texto1, texto2):
    contador_textos = 0
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(texto1, texto2)
        elif i % 3 == 0:
            print(texto1)
        elif i % 5 == 0:
            print(texto2)
        else:
            print(i)
            contador_textos += 1

    return contador_textos

print(contar_cadenas("hola", "adios"))