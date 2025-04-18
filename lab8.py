import cv2


img = cv2.imread('imagen2.png') 
luffy = cv2.imread('luffy.jpg')  


luffy_resized = cv2.resize(luffy, (300, 300))  
x, y = img.shape[1] - luffy_resized.shape[1] - 50, 50 

h, w = luffy_resized.shape[:2]
if y + h <= img.shape[0] and x + w <= img.shape[1]:
    img[y:y+h, x:x+w] = luffy_resized


blurred = cv2.GaussianBlur(img, (11, 11), 0)


blurred[y:y+h, x:x+w] = luffy_resized


cv2.imwrite('Imagen_con_luffy_en_arriba_derecha.png', blurred)


with open('coordenadas_luffy.txt', 'w') as f:
    f.write(f'Coordenadas de Luffy: x={x}, y={y}\n')


cv2.imshow('Imagen con Luffy en la esquina superior derecha', blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()





