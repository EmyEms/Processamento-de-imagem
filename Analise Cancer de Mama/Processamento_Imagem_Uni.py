#pip install scikit-image
#pip install Pillow

from PIL import Image, ImageDraw, ImageEnhance
from skimage import measure
import numpy as np
import cv2

# Abrir a imagen
imagem = Image.open('imagem2.jpg')

# converter a imagen em escala de cinza
imagem_cinza = imagem.convert('L')

# Converter a imagem em uma matriz numpy
matriz_imagem = np.array(imagem_cinza)

# Detectar os contornos
contornos = measure.find_contours(matriz_imagem, 0.8)

# Desenhar os contornos na imagen original
desenhar = ImageDraw.Draw(imagem)
for contorno in contornos:
  for i in range(len(contorno) - 1):
    desenhar.line((contorno[i][1], contorno[i][0], contorno[i+1][1], contorno[i+1][0]), fill='red', width=2)

# Aumentar o contraste
realcar = ImageEnhance.Contrast(imagem)
imagem = realcar.enhance(15.5)

# Mostrar a imagen com os contornos
imagem.save('mama_contornos.jpg')

import cv2
import numpy as np
img = cv2.imread("mama_contornos.jpg")

#cv2.imshow('image', img)
numero_pixels_branco = np.sum(img == 255)
numero_pixels_preto = np.sum(img == 0)
print("numero de pixels brancos:", numero_pixels_branco)
print("numero de pixels preto:", numero_pixels_preto)
#calcula a média de pixels brancos
percentual_pixels_brancos = numero_pixels_branco / (numero_pixels_branco + numero_pixels_preto) * 100
print("percentual pixels brancos:", percentual_pixels_brancos)
if(percentual_pixels_brancos >= 30):
  print('imagem com cancer ')
else:
    print('imagem sem cancer')