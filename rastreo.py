import cv2
import numpy as np

# Cargar la imagen tomada con la cámara (en este caso, la imagen impresa)
img = cv2.imread('impresion.jpg')  # Asegúrate de que el nombre del archivo sea correcto

# Convertir la imagen a escala de grises
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Aplicar un umbral para hacer la imagen binaria
_, thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

# Encontrar los contornos en la imagen
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Dibujar los contornos en la imagen original
cv2.drawContours(img, contours, -1, (0, 255, 0), 2)  # Puedes cambiar el color y grosor del contorno

# Mostrar la imagen con los contornos detectados
cv2.imshow('Detección de Contornos', img)

# Guardar la imagen con los contornos
cv2.imwrite('Imagen_con_contornos_impresion.png', img)

# Esperar hasta que se presione una tecla para cerrar la ventana
cv2.waitKey(0)
cv2.destroyAllWindows()
