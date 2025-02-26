import random

class Cuenta:
    def __init__(self, titular, saldo=0.0):
        self.titular = titular
        self.numero_cuenta = self._generar_numero_cuenta()
        self._saldo = saldo
    
    def _generar_numero_cuenta(self):
        return ''.join(str(random.randint(0, 9)) for _ in range(16))
    
    def depositar(self, monto):
        if monto > 0:
            self._saldo += monto
            print(f"Depósito exitoso. Nuevo saldo: ${self._saldo:.2f}")
        else:
            print("El monto a depositar debe ser mayor a cero.")
    
    def retirar(self, monto):
        if 0 < monto <= self._saldo:
            self._saldo -= monto
            print(f"Retiro exitoso. Nuevo saldo: ${self._saldo:.2f}")
        else:
            print("Fondos insuficientes o monto inválido.")
    
    def mostrar_saldo(self):
        print(f"Saldo actual: ${self._saldo:.2f}")
    
    def mostrar_informacion(self):
        print(f"Titular: {self.titular}")
        print(f"Número de cuenta: {self.numero_cuenta}")
        print(f"Saldo: ${self._saldo:.2f}")
    
    def _actualizar_saldo(self, nuevo_saldo):
        self._saldo = nuevo_saldo

class CuentaAhorro(Cuenta):
    def __init__(self, titular, saldo=0.0, tasa_interes=0.02):
        super().__init__(titular, saldo)
        self.tasa_interes = tasa_interes
    
    def calcular_interes(self):
        interes = self._saldo * self.tasa_interes
        self._saldo += interes
        print(f"Interés añadido: ${interes:.2f}. Nuevo saldo: ${self._saldo:.2f}")

class CuentaMonetaria(Cuenta):
    def __init__(self, titular, saldo=0.0, limite_credito=500.0):
        super().__init__(titular, saldo)
        self.limite_credito = limite_credito
    
    def retirar(self, monto):
        if 0 < monto <= (self._saldo + self.limite_credito):
            self._saldo -= monto
            print(f"Retiro exitoso. Nuevo saldo: ${self._saldo:.2f}")
        else:
            print("Fondos insuficientes, excede el límite de crédito o monto inválido.")

def menu():
    cuentas = {}
    while True:
        print("\n--- Menú del Banco ---")
        print("1. Abrir nueva cuenta")
        print("2. Gestionar cuenta existente")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            titular = input("Ingrese el nombre del titular: ")
            print("Seleccione el tipo de cuenta:")
            print("1. Cuenta de Ahorro")
            print("2. Cuenta Monetaria")
            tipo = input("Seleccione una opción: ")

            if tipo == '1':
                cuenta = CuentaAhorro(titular)
            elif tipo == '2':
                cuenta = CuentaMonetaria(titular)
            else:
                print("Opción inválida.")
                continue

            cuentas[cuenta.numero_cuenta] = cuenta
            print("Cuenta creada con éxito.")
            cuenta.mostrar_informacion()

        elif opcion == '2':
            numero_cuenta = input("Ingrese el número de cuenta: ")
            cuenta = cuentas.get(numero_cuenta)
            if cuenta:
                while True:
                    print("\n--- Gestión de Cuenta ---")
                    print("1. Depositar")
                    print("2. Retirar")
                    print("3. Mostrar información")
                    if isinstance(cuenta, CuentaAhorro):
                        print("4. Calcular interés")
                    print("5. Volver al menú principal")
                    opcion_cuenta = input("Seleccione una opción: ")

                    if opcion_cuenta == '1':
                        monto = float(input("Ingrese el monto a depositar: "))
                        cuenta.depositar(monto)
                    elif opcion_cuenta == '2':
                        monto = float(input("Ingrese el monto a retirar: "))
                        cuenta.retirar(monto)
                    elif opcion_cuenta == '3':
                        cuenta.mostrar_informacion()
                    elif opcion_cuenta == '4' and isinstance(cuenta, CuentaAhorro):
                        cuenta.calcular_interes()
                    elif opcion_cuenta == '5':
                        break
                    else:
                        print("Opción inválida.")
            else:
                print("Cuenta no encontrada.")
        elif opcion == '3':
            print("Gracias por usar nuestro banco. ¡Hasta luego!")
            break
        else:
            print("Opción inválida, intente de nuevo.")

if __name__ == "__main__":
    menu()