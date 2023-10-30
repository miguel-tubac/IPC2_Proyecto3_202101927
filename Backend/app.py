from flask import Flask, request, jsonify
import xml.etree.ElementTree as ET
from tkinter.filedialog import askopenfilename

# Importaciones realizadas:
from MensajesManager import MensajesManager
from Mensaje import Mensaje
from ConfiguracionManager import ConfiguracionManager
from Configuracion import Configuracion

# Inicializacion de Flask:
app = Flask(__name__)

# Cargar datos iniciales desde archivos XML
mensajes_manager = MensajesManager()
configuracion_manager = ConfiguracionManager()


# Cargar Archivos:
def open_file():
    filepath = askopenfilename(
        filetypes=[("XML Files", "*.xml"), ("All Files", "*.*")]
    )
    if not filepath:
        # Si no se selecciona nada
        return
    
    return filepath 


def cargar_mensajes(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    for mensaje_elem in root.findall('.//MENSAJE'):
        fecha = mensaje_elem.find('FECHA').text
        texto = mensaje_elem.find('TEXTO').text
        mensaje = Mensaje(fecha, texto)
        mensajes_manager.agregar_mensaje(mensaje)

def cargar_configuracion(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    positivos = [palabra.text.strip().lower() for palabra in root.findall('.//sentimientos_positivos/palabra')]
    negativos = [palabra.text.strip().lower() for palabra in root.findall('.//sentimientos_negativos/palabra')]

    configuracion = Configuracion(positivos, negativos)
    configuracion_manager.agregar_configuracion(configuracion)

# Endpoint para agregar Mensajes
@app.route('/grabarMensaje', methods=['POST'])
def grabar_mensaje():
    data = request.get_json()
    mensaje = Mensaje(data['fecha'], data['texto'])
    mensajes_manager.agregar_mensaje(mensaje)
    return jsonify({'message': 'Mensaje grabado con éxito'})

# Endpoint para agregar Configuracion
@app.route('/grabarConfiguracion', methods=['POST'])
def grabar_configuracion():
    data = request.get_json()
    configuracion = Configuracion(data['positivos'], data['negativos'])
    configuracion_manager.agregar_configuracion(configuracion)
    return jsonify({'message': 'Configuración grabada con éxito'})

# Endpoint para limpiar datos
@app.route('/limpiarDatos', methods=['POST'])
def limpiar_datos():
    mensajes_manager.limpiar_mensajes()
    configuracion_manager.limpiar_configuracion()
    return jsonify({'message': 'Datos limpiados con éxito'})

# Endpoint para devolver Hashings
@app.route('/devolverHashtags', methods=['GET'])
def devolver_hashtags():
    hashtags = mensajes_manager.obtener_hashtags()
    return jsonify({'hashtags': hashtags})

# Endpoint para devolver Menciones
@app.route('/devolverMenciones', methods=['GET'])
def devolver_menciones():
    menciones = mensajes_manager.obtener_menciones()
    return jsonify({'menciones': menciones})

if __name__ == '__main__':
    # Cargar datos iniciales desde archivos XML
    cargar_mensajes('EntradaMensajes.xml')
    cargar_configuracion('EntradaDiccionario.xml')
    
    app.run(debug=True)
