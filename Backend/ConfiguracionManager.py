class ConfiguracionManager:
    def __init__(self):
        self.diccionario_positivos = set()
        self.diccionario_negativos = set()

    def agregar_configuracion(self, configuracion):
        self.diccionario_positivos.update(configuracion.positivos)
        self.diccionario_negativos.update(configuracion.negativos)
    
    def imprimir_configuracion(self):
        print("Diccionario Positivos:", self.diccionario_positivos)
        print("Diccionario Negativos:", self.diccionario_negativos)

    def limpiar_configuracion(self):
        self.diccionario_positivos.clear()
        self.diccionario_negativos.clear()