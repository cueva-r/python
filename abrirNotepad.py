import speech_recognition as sr
import subprocess
import pyautogui

recognizer = sr.Recognizer()
proceso = None
saludo = """"
Hola :D
"""

def ejecutar_comando(comando):
    global proceso
    if "abrir blok de notas" in comando:
        proceso = subprocess.Popen(["notepad.exe"])
    elif "saludar a los demás" in comando:
        pyautogui.write(saludo)
    elif "cerrar block de notas" in comando:
        proceso.terminate()

def escuchar_comandos():
    with sr.Microphone() as source:
        print("En que te puedo ayudar?")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        comando = recognizer.recognize_google(audio, language="es-ES")
        print(f"Comando reconocido: {comando}")
        ejecutar_comando(comando)
    except sr.UnknownValueError:
        print("No se puede entender el comando")
    except sr.RequestError as e:
        print(f"Error al realizar la solicitud: {e}")

while True:
    escuchar_comandos()