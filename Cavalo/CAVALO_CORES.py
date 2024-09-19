import cv2 
import numpy as np 

#carregaer a imagem 
imagem = cv2.imread('cavalo.jpg')

#separando as camadas de cor em azul, verde e vermelho
azul, verde, vermelho = cv2.split(imagem)

#mesclando os canais de cor na ordem AVV
imagem_mesclada = cv2.merge ((azul, verde, vermelho))

#Invertendo os canais de cor
imagem_invertida = cv2.merge ((vermelho, verde, azul))
 
#criando uma imagem branca nas dimensoes da imagem lida
blank = np.zeros (imagem.shape[:2], dtype = 'uint8')

#abrindo as imagens por canais e mesclando com as matrizes de zeros 
canal_azul = cv2.merge([azul, blank, blank])
canal_verde = cv2.merge([blank,verde,blank])
canal_vermelho = cv2.merge([blank, blank,vermelho])

#visualizando 
cv2.imwrite ('azul.png', canal_azul)
cv2.imwrite ('verde.png', canal_verde)
cv2.imwrite ('vermelho.png',canal_vermelho)

cv2.imwrite ("imagem_mesclando.png", imagem_mesclada)

cv2.imwrite("imagem_invertida.png", imagem_invertida)