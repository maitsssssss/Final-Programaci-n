from datetime import datetime
import json
from usuario import Usuario
import matplotlib.pyplot as plt

class AppHealthTrack:
    def __init__(self):
        """
        Inicializa una nueva instancia de AppHealthTrack.
        """
        self.usuarios = []

    def crear_usuario(self, nombre, peso, altura, medidas, objetivos, fecha_peso_inicial):
        """
        Crea un nuevo usuario y lo agrega a la lista de usuarios de la aplicación.

        Args:
            nombre (str): El nombre del usuario.
            peso (float): El peso del usuario.
            altura (float): La altura del usuario.
            medidas (dict): Medidas del usuario (pecho, cintura, caderas).
            objetivos (list): Objetivos saludables del usuario.
            fecha_peso_inicial (str): La fecha en la que se registró el peso inicial.

        Returns:
            Usuario: El usuario creado.
        """
        # Convertir la fecha de string a objeto datetime.date
        fecha_peso_inicial = datetime.strptime(fecha_peso_inicial, "%Y-%m-%d").date()

        usuario_nuevo = Usuario(nombre, peso, altura, medidas, objetivos, fecha_peso_inicial)
        usuario_nuevo.agregar_peso(peso, fecha_peso_inicial)  # Agregar el peso inicial con la fecha proporcionada
        self.usuarios.append(usuario_nuevo)
        return usuario_nuevo

    def guardar_usuarios(self):
        """
        Guarda la lista de usuarios en un archivo JSON.
        """
        data = []
        for usuario in self.usuarios:
            data.append({
                "nombre": usuario.nombre,
                "peso_inicial": usuario.historial_pesos[0],
                "altura": usuario.talla,
                "medidas": usuario.medidas,
                "objetivos": usuario.objetivos,
                "fecha_peso_inicial": usuario.fechas_pesos[0].strftime("%Y-%m-%d")
            })

        with open("usuarios.json", "w") as file:
            json.dump(data, file, indent=4)

    def cargar_usuarios(self):
        """
        Carga la lista de usuarios desde un archivo JSON.
        """
        try:
            with open("usuarios.json", "r") as file:
                data = json.load(file)
                for item in data:
                    self.crear_usuario(item["nombre"], item["peso_inicial"], item["altura"], item["medidas"], item["objetivos"], item["fecha_peso_inicial"])
        except FileNotFoundError:
            print("No se encontró el archivo de usuarios. Se creará uno nuevo al guardar datos.")

    # Otros métodos de la clase...

    def ejecutar_aplicacion(self):
        """
        Ejecuta la aplicación HealthTrack.
        """
        self.cargar_usuarios()

        while True:
            print("1. Crear nuevo usuario")
            print("2. Ingresar nuevo peso y medidas de usuario existente")
            print("3. Mostrar ideas de comida")
            print("4. Mostrar ejercicios recomendados")
            print("5. Mostrar tips saludables")
            print("6. Mostrar último peso registrado de usuario")
            print("7. Mostrar progreso de usuario")
            print("8. Salir")
            opcion = input("Elija una opción: ")

            if opcion == "1":
                self.crear_nuevo_usuario()
            elif opcion == "2":
                self.ingresar_nuevo_peso()
            elif opcion == "3":
                self.mostrar_ideas_comida()
            elif opcion == "4":
                self.mostrar_ejercicios_recomendados()
            elif opcion == "5":
                self.mostrar_tips_saludables()
            elif opcion == "6":
                self.mostrar_ultimo_peso()
            elif opcion == "7":
                nombre_usuario = input("Ingrese el nombre del usuario para ver el progreso: ")
                self.mostrar_progreso(nombre_usuario)
            elif opcion == "8":
                self.guardar_usuarios()
                print("¡Hasta luego!")
                break
            else:
                print("Opción inválida. Intente nuevamente.")

    def crear_nuevo_usuario(self):
        """
        Crea un nuevo usuario solicitando los datos necesarios al usuario.
        """
        nombre = input("Ingrese su nombre: ")
        peso_inicial = self.validar_numero("Ingrese su peso inicial (kg): ")
        altura = self.validar_numero("Ingrese su altura (m): ")
        medidas = {
            "pecho": self.validar_numero("Ingrese medida de pecho (cm): "),
            "cintura": self.validar_numero("Ingrese medida de cintura (cm): "),
            "caderas": self.validar_numero("Ingrese medida de caderas (cm): ")
        }
        fecha_peso_inicial = input("Ingrese la fecha del peso inicial (YYYY-MM-DD): ")
        objetivos = input("Ingrese sus objetivos saludables separados por coma: ").split(",")
        usuario_nuevo = self.crear_usuario(nombre, peso_inicial, altura, medidas, objetivos, fecha_peso_inicial)
        print(f"Usuario creado exitosamente. ¡Bienvenid@, {usuario_nuevo}!")
        self.guardar_usuarios()  # Guardar automáticamente después de crear un nuevo usuario

    def validar_numero(self, mensaje):
        """
        Solicita al usuario un número y valida la entrada.

        Args:
            mensaje (str): El mensaje que se muestra al solicitar la entrada.

        Returns:
            float: El número ingresado por el usuario.
        """
        while True:
            try:
                numero = float(input(mensaje))
                break
            except ValueError:
                print("Error: Por favor, ingrese un número válido.")
        return numero

    def ingresar_nuevo_peso(self):
        """
        Ingresa un nuevo peso y medidas para un usuario existente.
        """
        nombre_usuario = input("Ingrese el nombre del usuario al que desea actualizar peso y medidas: ")
        usuario_existente = self.buscar_usuario(nombre_usuario)
        if usuario_existente:
            nuevo_peso = self.validar_numero(f"Ingrese el nuevo peso para {nombre_usuario}: ")
            fecha_registro = input("Ingrese la fecha del nuevo peso (YYYY-MM-DD): ")
            usuario_existente.agregar_peso(nuevo_peso, fecha_registro)
            medidas = {
                "pecho": self.validar_numero(f"Ingrese nueva medida de pecho (cm) para {nombre_usuario}: "),
                "cintura": self.validar_numero(f"Ingrese nueva medida de cintura (cm) para {nombre_usuario}: "),
                "caderas": self.validar_numero(f"Ingrese nueva medida de caderas (cm) para {nombre_usuario}: ")
            }
            usuario_existente.medidas = medidas
            print(f"Peso y medidas actualizados exitosamente para {nombre_usuario}.")
        else:
            print("Usuario no encontrado.")

    def buscar_usuario(self, nombre):
        """
        Busca un usuario en la lista de usuarios por nombre.

        Args:
            nombre (str): El nombre del usuario a buscar.

        Returns:
            Usuario: El usuario encontrado, o None si no se encuentra.
        """
        for usuario in self.usuarios:
            if usuario.nombre == nombre:
                return usuario
        return None

    def mostrar_ideas_comida(self):
        """
        Muestra ideas de comida y recetas saludables.
        """
        print("1. Ensalada de pollo")
        print("2. Salmón al horno")
        print("3. Batido de frutas")
        opcion = input("Elija una opción de comida: ")
        if opcion == "1":
            print("Receta de ensalada de pollo...")
        elif opcion == "2":
            print("Receta de salmón al horno...")
        elif opcion == "3":
            print("Receta de batido de frutas...")
        else:
            print("Opción inválida")

    def mostrar_ejercicios_recomendados(self):
        """
        Muestra ejercicios recomendados.
        """
        print("1. Correr")
        print("2. Nadar")
        print("3. Yoga")
        opcion = input("Elija una opción de ejercicio: ")
        if opcion == "1":
            print("Instrucciones para correr...")
        elif opcion == "2":
            print("Instrucciones para nadar...")
        elif opcion == "3":
            print("Instrucciones para hacer yoga...")

    def mostrar_tips_saludables(self):
        """
        Muestra tips saludables para una vida balanceada.
        """
        print("1. Beba suficiente agua")
        print("2. Duerma lo suficiente")
        print("3. Reduzca el consumo de azúcar")
        opcion = input("Elija un tip saludable: ")
        if opcion == "1":
            print("Recuerde beber al menos 8 vasos de agua al día")
        elif opcion == "2":
            print("Trate de dormir al menos 7-8 horas por noche")
        elif opcion == "3":
            print("Limite el consumo de alimentos y bebidas azucaradas...")
        else:
            print("Opción inválida")

    def mostrar_ultimo_peso(self):
        """
        Muestra el último peso registrado para un usuario.
        """
        nombre_usuario = input("Ingrese el nombre del usuario del que desea ver el último peso: ")
        usuario_existente = self.buscar_usuario(nombre_usuario)
        if usuario_existente:
            if usuario_existente.historial_pesos:
                ultimo_peso = usuario_existente.historial_pesos[-1]
                print(f"El último peso registrado para {nombre_usuario} es: {ultimo_peso} kg")
            else:
                print(f"No se ha registrado ningún peso para {nombre_usuario}.")
        else:
            print(f"No se encontró el usuario {nombre_usuario}.")

if __name__ == "__main__":
    app = AppHealthTrack()
    app.ejecutar_aplicacion()
