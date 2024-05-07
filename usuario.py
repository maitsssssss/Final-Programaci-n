from datetime import datetime

class Usuario:
    def __init__(self, nombre, peso_inicial, talla, medidas, objetivos, fecha_peso_inicial):
        self.nombre = nombre
        self.historial_pesos = [peso_inicial]  # Inicializar el historial de pesos con el peso inicial
        self.talla = talla
        self.medidas = medidas
        self.objetivos = objetivos
        self.fechas_pesos = [fecha_peso_inicial]  # Inicializar la lista de fechas de pesos con la fecha proporcionada

    def agregar_peso(self, nuevo_peso, fecha=None):
        """
        Agrega un nuevo peso al historial de pesos del usuario.

        Args:
            nuevo_peso (float): El nuevo peso a agregar.
            fecha (str, opcional): La fecha en la que se registró el peso. Si no se proporciona,
            se utilizará la fecha actual.
        """
        # Si no se proporciona una fecha, se utiliza la fecha actual
        if fecha is None:
            fecha = datetime.now().date()

        # Agregar el nuevo peso y su fecha correspondiente
        self.historial_pesos.append(nuevo_peso)
        self.fechas_pesos.append(fecha)

    def __str__(self) -> str:
        return f"{self.nombre}"
