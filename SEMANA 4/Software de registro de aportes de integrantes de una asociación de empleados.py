class Empleado:
    def __init__(self, nombre, aporte):
        self.nombre = nombre
        self.aporte = aporte


class Asociacion:
    def __init__(self):
        self.empleados = []

    def registrar_aporte(self):
        nombre = input("Nombre del empleado: ")
        aporte = float(input("Valor del aporte: "))

        empleado = Empleado(nombre, aporte)
        self.empleados.append(empleado)

        print("Aporte registrado correctamente.")

    def mostrar_aportes(self):
        if len(self.empleados) == 0:
            print("No existen aportes registrados.")
            return

        total = 0

        print("\nLISTA DE APORTES")
        for empleado in self.empleados:
            print(f"Empleado: {empleado.nombre}")
            print(f"Aporte: ${empleado.aporte:.2f}")
            print("--------------------")
            total += empleado.aporte

        print(f"\nTOTAL RECAUDADO: ${total:.2f}")


asociacion = Asociacion()

while True:
    print("\nREGISTRO DE APORTES")
    print("1. Registrar aporte")
    print("2. Mostrar aportes")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        asociacion.registrar_aporte()
    elif opcion == "2":
        asociacion.mostrar_aportes()
    elif opcion == "3":
        break