"""
EJERCICIO:
 - Muestra ejemplos de creación de todas las estructuras soportadas por defecto
   en tu lenguaje.
 - Utiliza operaciones de inserción, borrado, actualización y ordenación.

 DIFICULTAD EXTRA (opcional):
 - Crea una agenda de contactos por terminal.
 - Debes implementar funcionalidades de búsqueda, inserción, actualización
   y eliminación de contactos.
 - Cada contacto debe tener un nombre y un número de teléfono.
 - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
   y a continuación los datos necesarios para llevarla a cabo.
 - El programa no puede dejar introducir números de teléfono no númericos y con más
   de 11 dígitos (o el número de dígitos que quieras).
 - También se debe proponer una operación de finalización del programa.
"""


## Tipos de datos
## Listas:
una_lista = ['Maria', 25, True]
otra_lista = list()
elementos_a_ingresar = ['Andrea', 27, False]
for elemento in elementos_a_ingresar:
    otra_lista.append(elemento)
print(una_lista, type(una_lista))
print(otra_lista, type(otra_lista))

## Tuplas
una_tupla = (5, 7, 9)
print(una_tupla, type(una_tupla))
otra_tupla = tuple((8, 9, 10))
print(otra_tupla, type(otra_tupla))

## Diccionarios
un_diccionario = {"3673674": "Angel",
                  "8374384": "Marcos",
                  "7463737": "Miguel"}
for key in un_diccionario:
    print(key, un_diccionario[key])

    ## Matrices
una_matriz = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
for fila in una_matriz:
    for columna in fila:
        print(columna)
    print(fila)


## Clase para gestionar una agenda de teléfonos
class Agenda:
    def __init__(self):
        self.contactos = {}
        self.no_encontrado = True
        self.antiguo_telefono = None
        self.numero_de_contactos = 0

    # Función para buscar un contacto por el nombre
    def buscar_contacto(self, contacto):
        self.no_encontrado = True
        for c in self.contactos:
            if contacto.lower() == self.contactos[c].lower():
                print(f"{self.contactos[c]}: {c}")
                self.no_encontrado = False
        if self.no_encontrado:
            print(f"{contacto} no encontrado")

    # Función para insertar contacto
    def insertar_contacto(self, contacto):
        self.contactos.update({list(contacto.keys())[0]: list(contacto.values())[0]}) ## Actualizo el diccionario
        self.numero_de_contactos += 1 # Subo el contador de contactos

    # Función para actualizar contactos de la agenda
    def actualizar_contacto(self, contacto):
            for c in self.contactos:
                if self.contactos[c].lower() == list(contacto.values())[0].lower():
                    self.antiguo_telefono = c # asigno la clave del valor encontrado
            if self.antiguo_telefono:
                nuevo_contacto = self.contactos.pop(self.antiguo_telefono) # Elimino ese contacto pero capturo el valor
                self.contactos.update({list(contacto.keys())[0]: nuevo_contacto}) # Actualizo el dict con el nuevo valor
            else:
                print("Contacto no encontrado para actualizar")

    # Función para borrar los contactos
    def eliminar_contacto(self, contacto):
        try:
            for c in self.contactos:
                if self.contactos[c].lower() == contacto.lower(): # Busco el nombre en el diccionario
                    self.antiguo_telefono = c
            if input(f"Seguro que quiere borrar a {contacto}? -> s para borrar \n").lower() == "s": # Aseguramos decisión
                self.contactos.pop(self.antiguo_telefono)  ## Borro el contacto por su clave
                self.numero_de_contactos -= 1 # Actualizo el número de contactos
            else:
                print("Contacto no eliminado")
        except KeyError:
            print("Contacto no encontrado")

    # Función extra para mostrar todos los contactos
    def mostrar_contactos(self):
        print("         AGENDA       ")
        print("----------------------")
        for row, contacto in enumerate(self.contactos):
            print(f"Nombre:   {self.contactos[contacto]} \n"
                  f"Teléfono: {contacto}\n"
                  f"*********************")
            self.numero_de_contactos = row

        print(f"Numero de contactos en la agenda: {self.numero_de_contactos + 1}")


agenda = Agenda()
# Función para validar el número de tfno
def validar_telefono(tfno):
    if len(tfno) > 11:
        raise ValueError("Número de caracteres invalido")
    return tfno

while True:
    decision = int(input("Selecciona una de las siguientes opciones:\n"
                     "1-> Insertar un nuevo contacto\n"
                     "2-> Buscar un contacto\n"
                     "3-> Actualizar un contacto\n"
                     "4-> Eliminar un contacto\n"
                     "5-> Mostrar contactos\n"
                     "6-> Salir de la agenda\n"))
    match decision:
        case 1:
            try:
                nombre = (input("Ingrese el nombre: \n"))
                telefono = validar_telefono(input("Ingrese el teléfono: \n"))
                contactos = {telefono: nombre}
                agenda.insertar_contacto(contactos)
            except ValueError:
                print("Tiene que ingresar valores numéricos(máximo 11)")
        case 2:
            agenda.buscar_contacto(input("Ingrese el nombre del contacto: \n"))
        case 3:
            nombre = (input("Ingrese el nombre: \n"))
            telefono = validar_telefono(input("Ingrese el teléfono: \n"))
            agenda.actualizar_contacto({int(telefono): nombre})
        case 4:
            agenda.eliminar_contacto(input("Ingrese el nombre del contacto: \n"))
        case 5:
            agenda.mostrar_contactos()
        case 6:
            print("Gracias por usar el servicio")
            break
        case _:
            print("Opción invalida")




