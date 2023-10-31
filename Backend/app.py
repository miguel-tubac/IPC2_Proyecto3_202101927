from flask import Flask, request, jsonify
import xml.etree.ElementTree as ET
#from tkinter.filedialog import askopenfilename

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


# Endpoint para agregar Mensajes
@app.route('/grabarMensaje', methods=['POST'])
def grabar_mensaje():
    if request.headers['Content-Type'] == 'application/xml':
        # Si la solicitud es en formato XML
        data = ET.fromstring(request.data)
        mensaje_element = data.find('MENSAJE')
        # Se coprueba que no venga con dato None
        if mensaje_element is not None:
            mensajes_elementos = data.findall('MENSAJE')
            for mensaje_element in mensajes_elementos:
                fecha = mensaje_element.find('FECHA').text
                texto = mensaje_element.find('TEXTO').text.strip()
                mensaje = Mensaje(fecha, texto)
                mensajes_manager.agregar_mensaje(mensaje)
            #mensajes_manager.imprimir_Mensajes()
            return jsonify({'message': 'Mensajes grabados con éxito'})
        else:
            return jsonify({'error': 'Elemento "MENSAJE" no encontrado en el XML'}), 400
    else:
        return jsonify({'error': 'Formato no soportado'}), 415

# Endpoint para agregar Configuracion
@app.route('/grabarConfiguracion', methods=['POST'])
def grabar_configuracion():
    # Comprobacion adecuada del archivo xml:
    if request.headers['Content-Type'] == 'application/xml':
        #print("Xml resivido: ", request.data)
        data = ET.fromstring(request.data)
        #print(data)
        diccionario_element = data #.find('diccionario')
        #print(diccionario_element)
        # Se compruaba el incio del diccionario
        if diccionario_element is not None:
            sentimientos_positivos = diccionario_element.find('sentimientos_positivos')
            sentimientos_negativos = diccionario_element.find('sentimientos_negativos')

            if sentimientos_positivos is not None and sentimientos_negativos is not None:
                palabras_positivas = [palabra.text.strip() for palabra in sentimientos_positivos.findall('palabra')]
                palabras_negativas = [palabra.text.strip() for palabra in sentimientos_negativos.findall('palabra')]
                #print(palabras_positivas)
                # Se almacenan las configuraciones:
                configuracion = Configuracion(palabras_positivas, palabras_negativas)
                configuracion_manager.agregar_configuracion(configuracion)
                #configuracion_manager.imprimir_configuracion()

                return jsonify({'message': 'Configuración grabada con éxito'})
            else:
                return jsonify({'error': 'Elementos requeridos no encontrados en el XML'}), 400
        else:
            return jsonify({'error': 'Elemento "diccionario" no encontrado en el XML'}), 400
    else:
        return jsonify({'error': 'Formato no soportado'}), 415
    


# Endpoint para limpiar datos
@app.route('/limpiarDatos', methods=['POST'])
def limpiar_datos():
    mensajes_manager.limpiar_mensajes()
    configuracion_manager.limpiar_configuracion()
    # Mensaje de retorno 
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
    # cargar_mensajes('EntradaMensajes.xml')
    # cargar_configuracion('EntradaDiccionario.xml')
    app.run(debug=True)
