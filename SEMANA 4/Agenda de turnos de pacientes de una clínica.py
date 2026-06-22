class Paciente:
    def __init__(self, nombre, cedula, turno):
        self.nombre = nombre
        self.cedula = cedula
        self.turno = turno


class Clinica:
    def __init__(self):
        self.pacientes = []

    def registrar_paciente(self):
        nombre = input("Nombre: ")
        cedula = input("Cédula: ")
        turno = input("Turno: ")

        paciente = Paciente(nombre, cedula, turno)
        self.pacientes.append(paciente)

        print("Paciente registrado correctamente.")

    def mostrar_pacientes(self):
        if len(self.pacientes) == 0:
            print("No existen pacientes registrados.")
            return

        print("\nLISTA DE PACIENTES")
        for paciente in self.pacientes:
            print(f"Nombre: {paciente.nombre}")
            print(f"Cédula: {paciente.cedula}")
            print(f"Turno: {paciente.turno}")
            print("---------------------")


clinica = Clinica()

while True:
    print("\nAGENDA DE TURNOS")
    print("1. Registrar paciente")
    print("2. Mostrar pacientes")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        clinica.registrar_paciente()
    elif opcion == "2":
        clinica.mostrar_pacientes()
    elif opcion == "3":
        break