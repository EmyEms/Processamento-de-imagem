import cv2
import numpy as np
import os

# Verificar o diretório de trabalho atual
print("Diretório de trabalho atual:", os.getcwd())

# Carregar a imagem com o caminho correto
imagem = cv2.imread('Cavalo/cavalo.jpg')
if imagem is None:
    print("Erro: A imagem 'cavalo.jpg' não foi encontrada ou não pode ser carregada.")
    exit()

# Separar os canais de cor em azul, verde e vermelho
azul, verde, vermelho = cv2.split(imagem)

# Mesclar os canais de cor na ordem BGR (reconstruir a imagem original)
imagem_mesclada = cv2.merge((azul, verde, vermelho))

# Inverter os canais de cor (de BGR para RGB)
imagem_invertida = cv2.merge((vermelho, verde, azul))

# Criar uma imagem em branco (preta) com as mesmas dimensões da imagem original
blank = np.zeros(imagem.shape[:2], dtype='uint8')

# Criar imagens destacando cada canal de cor
canal_azul = cv2.merge([azul, blank, blank])         # Canal azul
canal_verde = cv2.merge([blank, verde, blank])       # Canal verde
canal_vermelho = cv2.merge([blank, blank, vermelho]) # Canal vermelho

# Salvar as imagens
cv2.imwrite('Cavalo/azul.png', canal_azul)
cv2.imwrite('Cavalo/verde.png', canal_verde)
cv2.imwrite('Cavalo/vermelho.png', canal_vermelho)
cv2.imwrite('Cavalo/imagem_mesclada.png', imagem_mesclada)
cv2.imwrite('Cavalo/imagem_invertida.png', imagem_invertida)

print("As imagens foram salvas com sucesso.")
