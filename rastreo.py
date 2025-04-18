import cv2
import numpy as np


img = cv2.imread('impresion.jpg')  

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


_, thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)


contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


cv2.drawContours(img, contours, -1, (0, 255, 0), 2) 

cv2.imshow('Detección de Contornos', img)


cv2.imwrite('Imagen_con_contornos_impresion.png', img)


cv2.waitKey(0)
cv2.destroyAllWindows()
