from django.http import HttpResponse
from django.template import  loader
# aca se deven de ir importando las peticiones de tipo: get, post.........
from requests import post, get
import os
import webbrowser

# Devuelve alguna informacion:
def getInfoEstudiante(request):
    # cargamos el html en un template:
    objetoTemplate = loader.get_template("datosEstudiante.html")
    html = objetoTemplate.render()
    return HttpResponse(html)

def reporte(request):
    # Estas direcciones la tomo de postman (es la parte donde conecto el Backend con el Frontend):
    url = "http://127.0.0.1:5000/grabarMensaje"
    resp = post(url)
    print(respu.json())

    # Esto es lo que necesito retornar del Backend:
    existe = False
    nombre_reporte = "Sentimiento de mensaje"
    descripcion_reporte = "Reporte de sentimiento de mensaje"
    conteo_sentimientos = [10, 20, 50]

    # cargamos el html en un template:
    objetoTemplate = loader.get_template("datosEstudiante.html")
    html = objetoTemplate.render({"existe":existe,"respuest":resp.json(),"idNombre_reporte":nombre_reporte, "descripcion":descripcion_reporte,"valores":conteo_sentimientos})
    return HttpResponse(html)

def incio(request):
    # cargamos el html en un template:
    objetoTemplate = loader.get_template("index.html")
    html = objetoTemplate.render()
    return HttpResponse(html)

def procesar_configuracion(request):
    if request.method == 'POST':
        archivo_configuracion = request.FILES.get('archivoConfiguracion')

        # Leer el contenido del archivo
        contenido = archivo_configuracion.read()

        # Realizar la solicitud al endpoint del backend
        url_backend = 'http://127.0.0.1:5000/grabarConfiguracion'  # Reemplaza con la dirección correcta
        headers = {'Content-Type': 'application/xml'}

        response = request.post(url_backend)

        #response = requests.post(url_backend, data=contenido, headers=headers)

        if response.status_code == 200:
            return HttpResponse("Archivo de configuración procesado correctamente.")
        else:
            return HttpResponse(f"Error en la solicitud al backend: {response.status_code}")

def mostrarDocumentacion(request):
    ruta_absoluta = os.path.abspath("Documentacion/Proyecto3.pdf")

    try:
        # Intenta abrir el archivo con el visor de PDF predeterminado del sistema
        webbrowser.open(ruta_absoluta, new=2)
        getInfoEstudiante(request)
        objetoTemplate = loader.get_template("datosEstudiante.html")
        html = objetoTemplate.render()
        return HttpResponse(html)
    except Exception as e:
        return HttpResponse(f"Error al abrir el documento: {e}")