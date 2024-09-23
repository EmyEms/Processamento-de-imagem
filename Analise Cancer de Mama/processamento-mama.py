from PIL import Image, ImageDraw, ImageEnhance
from skimage import measure
import numpy as np

imagem = Image.open('Analise Cancer de Mama/mama.jpg')

# Convertendo a imagem para escala de cinza
imagem_cinza = imagem.convert('L')

# Convert image to numpy array
matriz_imagem = np.array(imagem_cinza)

# Encontrando contornos na imagem
contornos = measure.find_contours(matriz_imagem, 0.8)

# Criando uma nova imagem para desenhar os contornos
desenhar = ImageDraw.Draw(imagem)

# Loop de contornos e desenho de linhas entre os pontos de contorno
for contorno in contornos:
    for i in range(len(contorno) - 1):
        desenhar.line(
            (
                contorno[i][1],
                contorno[i][0],
                contorno[i + 1][1],
                contorno[i + 1][0],
            ),
            fill=255,
        )

# Adicionando realce de contraste
realce = ImageEnhance.Contrast(imagem)
imagem_realce = realce.enhance(15.5)

# Salvando a imagem
imagem_realce.save('Analise Cancer de Mama/mama_contornos.jpg')
