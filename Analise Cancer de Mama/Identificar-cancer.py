import cv2
import numpy as np

img = cv2.imread('Analise Cancer de Mama/mama_contornos.jpg')
numero_pixels_branco = np.sum(img == 255)
numero_pixels_preto = np.sum(img == 0)

print(f'Número de pixels brancos: {numero_pixels_branco}')
print(f'Número de pixels pretos: {numero_pixels_preto}')

percentual_pixels_branco = (numero_pixels_branco / (numero_pixels_branco + numero_pixels_preto)) * 100
print(f'Percentual de pixels brancos: {percentual_pixels_branco:.2f}%')

if (percentual_pixels_branco >- 30):
    print('Imagem com câncer de mama')
else:
    print('Imagem sem câncer de mama')