import cv2

# Cargar las imágenes
img = cv2.imread('imagen2.png')  # La imagen original
luffy = cv2.imread('luffy.jpg')  # La imagen de Luffy

# Redimensionar la imagen de Luffy para hacerla aún más grande
luffy_resized = cv2.resize(luffy, (300, 300))  # Aumentar el tamaño de la imagen de Luffy

# Definir las coordenadas (x, y) donde colocarás la imagen de Luffy en la parte superior derecha
x, y = img.shape[1] - luffy_resized.shape[1] - 50, 50  # Coordenadas en la esquina superior derecha

# Asegurarse de que la imagen de Luffy no sobresalga de la imagen principal
h, w = luffy_resized.shape[:2]
if y + h <= img.shape[0] and x + w <= img.shape[1]:
    img[y:y+h, x:x+w] = luffy_resized

# Aplicar desenfoque gaussiano a la imagen original
blurred = cv2.GaussianBlur(img, (11, 11), 0)

# Mantener la imagen de Luffy sin desenfoque
blurred[y:y+h, x:x+w] = luffy_resized

# Guardar la imagen desenfocada con Luffy
cv2.imwrite('Imagen_con_luffy_en_arriba_derecha.png', blurred)

# Actualizar las coordenadas y guardarlas en un archivo de texto
with open('coordenadas_luffy.txt', 'w') as f:
    f.write(f'Coordenadas de Luffy: x={x}, y={y}\n')

# Mostrar la imagen con Luffy
cv2.imshow('Imagen con Luffy en la esquina superior derecha', blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()





