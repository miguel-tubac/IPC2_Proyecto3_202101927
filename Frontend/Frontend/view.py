from django.http import HttpResponse
from django.template import  loader
# aca se deven de ir importando las peticiones de tipo: get, post.........
from requests import post, get

# Devuelve alguna informacion:
def getInfoEstudiante(request):
    return HttpResponse("Frontend: Estudiante de IPC2")

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
    objetoTemplate = loader.get_template("reporte.html")
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
        # Aquí puedes realizar cualquier procesamiento necesario con el archivo

        # Por ejemplo, imprimir el contenido del archivo
        contenido = archivo_configuracion.read().decode('utf-8')
        print(contenido)

    return HttpResponse("Archivo de configuración procesado correctamente.")