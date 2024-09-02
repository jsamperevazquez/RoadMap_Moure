"""
    - Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
     en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
    - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición,
     recorrido, conversión a mayúsculas y minúsculas, reemplazo, división, unión,
     interpolación, verificación...

     DIFICULTAD EXTRA (opcional):
    - Crea un programa que analice dos palabras diferentes y realice comprobaciones
      para descubrir si son:
        - Palíndromos
        - Anagramas
        - Isogramas
"""

# Operaciones con caracteres
suma_caracteres = "Hola" + " Python"
print(suma_caracteres)
multiplicar_caracteres = "Hola"
multiplicar_caracteres *= 2
print(multiplicar_caracteres)
anadir = "Hola"
anadir += " Mundo"
print(anadir)

# Buscar caracteres
if suma_caracteres.find("ola"):  # Devuelve bool si está
    print("Están los caracteres")
# Mayusculas y minúsculas
print(anadir.lower())
print(anadir.capitalize())
print(anadir.upper())
# Remplazar caracteres
remplazar = suma_caracteres.replace("Hola", "Adios")
print(remplazar)
# Cortar caracteres
cortar = anadir[2:9]  # Del 2 (incluido) al 9 (no incluido)
print(cortar)
cortar = anadir[1:: 2]  # Del 1 al final con salto 2
print(cortar)


def comprobar_palabras(palabra1, palabra2=None):
    # Palindromo
    if palabra2 is not None and len(palabra2) == len(palabra1):
        palabra_volteada = palabra2[:: -1].lower()
        if palabra_volteada == palabra1.lower():
            print(f"{palabra1} y {palabra2} son palíndromo")
        else:
            print(f"{palabra1} y {palabra2} no son palíndromo")
        # Anagrama
        if len(palabra1) != len(palabra2):
            print(f"{palabra1} no son Anagramas")
        else:
            caracteres_comunes = [x for x in palabra1 if x in palabra2]
            if len(caracteres_comunes) == len(palabra1):
                print(f"{palabra1} y {palabra2} son anagramas")
            else:
                print(f"{palabra1} y {palabra2} no son anagramas")
    # Isogramas
    test_1 = test_isograma(palabra1)
    test_2 = test_isograma(palabra2)
    if test_1 == len(palabra1):
        print(f"{palabra1} es un Isograma")
    else:
        print(f"{palabra1} no es Isograma")
    if test_2 == len(palabra2):
        print(f"{palabra2} es un Isograma")
    else:
        print(f"{palabra2} no es Isograma")


def test_isograma(palabra):
    if palabra is not None:
        lista_caracteres = []
        for c in palabra:
            if c not in lista_caracteres:
                lista_caracteres.append(c)
        return len(lista_caracteres)


comprobar_palabras("Adan", "nada")
comprobar_palabras("cara", "arma")
comprobar_palabras("hola", "rata")
