import cv2
import numpy as np

def calcular_estatura(distancia, relacion_altura_pixel):
    estatura_cm = distancia * relacion_altura_pixel
    return estatura_cm

def medir_estatura():
    # Inicializar la cámara
    cap = cv2.VideoCapture(0)

    # Cargar el clasificador de caras de OpenCV
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    while True:
        # Capturar el frame de la cámara
        ret, frame = cap.read()

        # Convertir el frame a escala de grises
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detectar caras en el frame
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in faces:
            # Dibujar un rectángulo alrededor de la cara
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

            # Calcular la distancia estimada a la persona (puedes ajustar este valor según tu configuración)
            distancia_estimada = 100

            # Calcular la relación de altura en píxeles
            relacion_altura_pixel = 170 / h  # Puedes ajustar este valor según tu configuración

            # Calcular la estatura
            estatura = calcular_estatura(distancia_estimada, relacion_altura_pixel)

            # Mostrar la estatura en el frame
            cv2.putText(frame, f'Estatura: {estatura:.2f} cm', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

        # Mostrar el frame
        cv2.imshow("Medidor de Estatura", frame)

        # Esperar la tecla 'q' para salir
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Liberar la cámara y cerrar la ventana
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    medir_estatura()
