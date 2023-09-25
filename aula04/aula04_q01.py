import cv2
import numpy as np


# Função com a matemática utilizada no método do OpenCV
def rgb_para_gray_cv(original_rgb):
    """
    Fórmula do OpenCV para conversão RGB-Gray

    RGB[A] to Gray:Y←0.299⋅R+0.587⋅G+0.114⋅B
    """

    B, G, R = cv2.split(original_rgb)

    convertida_gray = np.empty_like(original_rgb[:, :, 0])
    
    for i in range(convertida_gray.shape[0]):
        for j in range(convertida_gray.shape[1]):
            convertida_gray[i, j] = 0.299*R[i, j] + 0.587*G[i, j] + 0.114*B[i, j]

    return convertida_gray


# Função aplicando a média entre os canais RGB
def rgb_para_gray_media(original_rgb):

    convertida_gray = np.empty_like(original_rgb[:, :, 0])
    
    for i in range(convertida_gray.shape[0]):
        for j in range(convertida_gray.shape[1]):
            convertida_gray[i, j] = original_rgb[i, j].mean()

    return convertida_gray


# Leitura da Imagem
img_rgb = cv2.imread(r'ppgee\PDI_20232_GrpJNS\aula04\imagens\pexels-jared-vandermeer-3744703.jpg')

# Normalização da Imagem
img_rgb_normalizada = cv2.normalize(img_rgb, None, 0, 1.0, cv2.NORM_MINMAX, dtype=cv2.CV_32F)
print(f'Minimo e Maximo imagem original: {img_rgb.min()}, {img_rgb.max()}')
print(f'Minimo e Maximo imagem normalizada: {img_rgb_normalizada.min()}, {img_rgb_normalizada.max()}')

# Conversões RGB para cinza
img_gray_cv = rgb_para_gray_cv(img_rgb_normalizada)
img_gray_media = rgb_para_gray_media(img_rgb_normalizada)

# Conversões RGB para HSI


# Apresentação das Imagens
cv2.imshow('Imagem original', img_rgb)
cv2.imshow('Imagem normalizada', img_rgb_normalizada)
cv2.imshow('Imagem convertida pela formula do CV', img_gray_cv)
cv2.imshow('Imagem convertida pela media dos canais', img_gray_media)

cv2.waitKey(0)
cv2.destroyAllWindows()

