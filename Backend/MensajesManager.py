class MensajesManager:
    def __init__(self):
        self.mensajes = []

    def agregar_mensaje(self, mensaje):
        self.mensajes.append(mensaje)

    def limpiar_mensajes(self):
        self.mensajes.clear()

    def obtener_hashtags(self):
        hashtags = set()
        for mensaje in self.mensajes:
            texto = mensaje.texto
            hashtags.update(tag[1:] for tag in texto.split() if tag.startswith('#'))
        return list(hashtags)

    def obtener_menciones(self):
        menciones = set()
        for mensaje in self.mensajes:
            texto = mensaje.texto
            menciones.update(mention[1:] for mention in texto.split() if mention.startswith('@'))
        return list(menciones)