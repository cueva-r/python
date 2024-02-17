from pytube import YouTube

# Función para mostrar las opciones de calidad disponibles
def mostrar_opciones(video):
    print("Opciones de calidad disponibles:")
    for stream in video.streams.filter(progressive=True):
        print(stream.resolution)

# Función para descargar el video con la calidad seleccionada
def descargar_video(url, calidad):
    try:
        yt = YouTube(url)
        video = yt.streams.filter(progressive=True, res=calidad).first()
        if video:
            print(f"Descargando video en {calidad}...")
            video.download()
            print("Descarga completada.")
        else:
            print(f"No se encontró una opción de calidad de {calidad}.")
            mostrar_opciones(yt)
    except Exception as e:
        print("Ocurrió un error:", e)

# URL del video de YouTube
url = input("Ingrese el enlace del video de YouTube: ")

# Mostrar opciones de calidad disponibles
try:
    yt = YouTube(url)
    mostrar_opciones(yt)

    # Pedir al usuario que seleccione la calidad
    calidad_seleccionada = input("Ingrese la calidad deseada (por ejemplo, 1080p): ")

    # Descargar el video con la calidad seleccionada
    descargar_video(url, calidad_seleccionada)
except Exception as e:
    print("Ocurrió un error:", e)
