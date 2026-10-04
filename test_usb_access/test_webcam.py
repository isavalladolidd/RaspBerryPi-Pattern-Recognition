import cv2

def tomar_foto(nombre_archivo="webcam_fotos/foto.jpg"):
    # 0 selecciona la cámara web predeterminada de tu equipo
    camara = cv2.VideoCapture(0)

    # Verificar si la cámara se abrió correctamente
    if not camara.isOpened():
        print("Error: No se pudo acceder a la cámara.")
        return

    # Esperar unos frames breves para que la cámara ajuste la exposición y el enfoque
    for _ in range(5):
        camara.read()

    # Capturar la foto
    exito, imagen = camara.read()

    if exito:
        # Guardar la imagen en el disco
        cv2.imwrite(nombre_archivo, imagen)
        print(f"¡Foto guardada exitosamente como '{nombre_archivo}'!")
    else:
        print("Error: No se pudo capturar la imagen.")

    # Liberar el recurso de la cámara
    camara.release()

if __name__ == "__main__":
    tomar_foto()
