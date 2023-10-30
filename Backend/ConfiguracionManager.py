class ConfiguracionManager:
    def __init__(self):
        self.diccionario_positivos = set()
        self.diccionario_negativos = set()

    def agregar_configuracion(self, configuracion):
        self.diccionario_positivos.update(configuracion.positivos)
        self.diccionario_negativos.update(configuracion.negativos)

    def limpiar_configuracion(self):
        self.diccionario_positivos.clear()
        self.diccionario_negativos.clear()