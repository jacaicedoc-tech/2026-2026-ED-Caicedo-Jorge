class Contacto:
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono


class Agenda:
    def __init__(self):
        self.contactos = []

    def agregar_contacto(self):
        nombre = input("Nombre: ")
        telefono = input("Teléfono: ")

        contacto = Contacto(nombre, telefono)
        self.contactos.append(contacto)

        print("Contacto registrado correctamente.")

    def mostrar_contactos(self):
        if len(self.contactos) == 0:
            print("No hay contactos registrados.")
            return

        print("\nLISTA DE CONTACTOS")
        for contacto in self.contactos:
            print(f"Nombre: {contacto.nombre}")
            print(f"Teléfono: {contacto.telefono}")
            print("-------------------")


agenda = Agenda()

while True:
    print("\nAGENDA TELEFÓNICA")
    print("1. Agregar contacto")
    print("2. Mostrar contactos")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agenda.agregar_contacto()
    elif opcion == "2":
        agenda.mostrar_contactos()
    elif opcion == "3":
        break