import random
import string

# Clase base que representa un material genérico de biblioteca
class MaterialBiblioteca:
    def __init__(self, titulo, autor):
        # Atributos protegidos: título, autor, código único y estado de préstamo
        self._titulo = titulo
        self._autor = autor
        self._codigo_unico = self._generar_codigo()  # Se genera automáticamente
        self._estado_prestamo = False  # False = disponible, True = prestado

    # Método privado para generar un código único aleatorio
    def _generar_codigo(self):
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

    # Método para prestar el material
    def prestar(self):
        if not self._estado_prestamo:
            self._estado_prestamo = True
            print(f"✅ Material '{self._titulo}' prestado correctamente.")
        else:
            print(f"⚠️ El material '{self._titulo}' ya está prestado.")

    # Método para devolver el material
    def devolver(self):
        if self._estado_prestamo:
            self._estado_prestamo = False
            print(f"✅ Material '{self._titulo}' devuelto correctamente.")
        else:
            print(f"⚠️ El material '{self._titulo}' no estaba prestado.")

    # Método para mostrar la información del material
    def mostrar_informacion(self):
        estado = "Prestado" if self._estado_prestamo else "Disponible"
        print(f"📚 Título: {self._titulo}")
        print(f"✍️ Autor: {self._autor}")
        print(f"🔑 Código único: {self._codigo_unico}")
        print(f"📌 Estado: {estado}")


    
#LIBRO FISICO
# Clase que representa un libro físico, hereda de MaterialBiblioteca
class LibroFisico(MaterialBiblioteca):
    def __init__(self, titulo, autor, numero_ejemplar):
        super().__init__(titulo, autor)  # Llama al constructor de la clase base
        self._numero_ejemplar = numero_ejemplar
        self._dias_prestamo = 7  # Tiempo máximo de préstamo en días

    # Sobrescribe el método para mostrar información, añadiendo detalles específicos
    def mostrar_informacion(self):
        super().mostrar_informacion()  # Muestra la info base
        print(f"🔢 Número de ejemplar: {self._numero_ejemplar}")
        print(f"⏳ Tiempo máximo de préstamo: {self._dias_prestamo} días")



# Clase que representa un libro digital, hereda de MaterialBiblioteca
class LibroDigital(MaterialBiblioteca):
    def __init__(self, titulo, autor, tamano_archivo):
        super().__init__(titulo, autor)
        self._tamano_archivo = tamano_archivo  # Tamaño en MB
        self._dias_prestamo = 3  # Tiempo máximo de préstamo en días

    # Sobrescribe el método para mostrar información
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"💾 Tamaño del archivo: {self._tamano_archivo} MB")
        print(f"⏳ Tiempo máximo de préstamo: {self._dias_prestamo} días")





# Clase que gestiona el sistema completo de la biblioteca
class SistemaBiblioteca:
    def __init__(self):
        self.materiales = []  # Lista para almacenar todos los materiales registrados

    # Muestra el menú principal
    def mostrar_menu(self):
        print("\n📚 MENÚ DE BIBLIOTECA")
        print("1. Registrar libro físico")
        print("2. Registrar libro digital")
        print("3. Mostrar información de todos los materiales")
        print("4. Prestar material")
        print("5. Devolver material")
        print("6. Salir")

    # Busca un material por su código único
    def buscar_material_por_codigo(self, codigo):
        for material in self.materiales:
            if material._codigo_unico == codigo:
                return material
        return None  # Si no se encuentra, retorna None

    # Registra un nuevo libro físico
    def registrar_libro_fisico(self):
        titulo = input("Título del libro físico: ")
        autor = input("Autor: ")
        numero_ejemplar = input("Número de ejemplar: ")
        libro = LibroFisico(titulo, autor, numero_ejemplar)
        self.materiales.append(libro)
        print("✅ Libro físico registrado.")

    # Registra un nuevo libro digital
    def registrar_libro_digital(self):
        titulo = input("Título del libro digital: ")
        autor = input("Autor: ")
        tamano = float(input("Tamaño del archivo (MB): "))
        libro = LibroDigital(titulo, autor, tamano)
        self.materiales.append(libro)
        print("✅ Libro digital registrado.")

    # Muestra todos los materiales registrados
    def mostrar_materiales(self):
        if not self.materiales:
            print("⚠️ No hay materiales registrados.")
        else:
            for material in self.materiales:
                print("\n-------------------------")
                material.mostrar_informacion()

    # Presta un material según su código
    def prestar_material(self):
        codigo = input("🔍 Ingresa el código único del material a prestar: ")
        material = self.buscar_material_por_codigo(codigo)
        if material:
            material.prestar()
        else:
            print("❌ Material no encontrado.")

    # Devuelve un material según su código
    def devolver_material(self):
        codigo = input("🔍 Ingresa el código único del material a devolver: ")
        material = self.buscar_material_por_codigo(codigo)
        if material:
            material.devolver()
        else:
            print("❌ Material no encontrado.")

    # Ejecuta el ciclo principal del sistema
    def ejecutar(self):
        while True:
            self.mostrar_menu()
            opcion = input("Selecciona una opción: ")

            if opcion == "1":
                self.registrar_libro_fisico()
            elif opcion == "2":
                self.registrar_libro_digital()
            elif opcion == "3":
                self.mostrar_materiales()
            elif opcion == "4":
                self.prestar_material()
            elif opcion == "5":
                self.devolver_material()
            elif opcion == "6":
                print("👋 Gracias por usar el sistema de biblioteca.")
                break
            else:
                print("⚠️ Opción inválida. Intenta de nuevo.")



# Punto de entrada del programa
if __name__ == "__main__":
    sistema = SistemaBiblioteca()
    sistema.ejecutar()