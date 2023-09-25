import cv2
import numpy as np


# Função com a matemática utilizada no método do OpenCV
def rgb_para_hsi(original_rgb):

    B, G, R = cv2.split(original_rgb)

    # Cálculo de H
    numerador = 0.5 * ((R - G) + (R - B))
    denominador = np.sqrt((R - G)**2 + (R - B) * (G - B))
    # Fazendo o denominador ser um número pequeno quando R=G=B, evitando divisão por zero.
    denominador[denominador == 0] = 1e-10  
    theta = np.arccos(np.clip(numerador / denominador, -1, 1))

    H = np.degrees(theta)
    H[B > G] = 360 - H[B > G]

    # Normalização para o intervalo [0, 1]
    H = H/360
    print(f'Minimo, máximo de H: {H.min()}, {H.max()}')

    # Cálculo de S
    valor_minimo_rgb = np.minimum.reduce([R, G, B])
    soma_canais = R + G + B
    S = 1 - 3 * (valor_minimo_rgb / soma_canais)
    S[soma_canais == 0] = 0  # Evitando divisão por zero

    # S não precisa normalizar porque RGB de entrada já estava normalizado para [0, 1]
    print(f'Minimo, máximo de S: {S.min()}, {S.max()}')

    # Cálculo de I
    I = (soma_canais) / 3

    # I não precisa normalizar porque RGB de entrada já estava normalizado para [0, 1]
    print(f'Minimo, máximo de I: {I.min()}, {I.max()}')

    # Concatenando os canais HSI para formar imagem de retorno
    convertida_hsi = cv2.merge([H, S, I])
    # convertida_hsi = np.dstack((H, S, I)).astype(np.uint8)

    return convertida_hsi


# Leitura da Imagem
img_rgb = cv2.imread(r'ppgee\PDI_20232_GrpJNS\aula04\imagens\pexels-efrem-efre-18185921.jpg')

# Normalização da Imagem
img_rgb_normalizada = cv2.normalize(img_rgb, None, 0, 1.0, cv2.NORM_MINMAX, dtype=cv2.CV_32F)
print(f'Minimo e Maximo imagem original: {img_rgb.min()}, {img_rgb.max()}')
print(f'Minimo e Maximo imagem normalizada: {img_rgb_normalizada.min()}, {img_rgb_normalizada.max()}')

# Conversões RGB para HSI
img_hsi = rgb_para_hsi(img_rgb_normalizada)

# img_hsi_desnormalizada = cv2.normalize(img_hsi, None, 0, 255, cv2.NORM_MINMAX)
# print(f'Minimo e Maximo imagem desnormalizada: {img_hsi_desnormalizada.min()}, {img_hsi_desnormalizada.max()}')

# Apresentação das Imagens
cv2.imshow('Imagem original', img_rgb)
cv2.imshow('Imagem normalizada', img_rgb_normalizada)
cv2.imshow('Imagem convertida para HSI', img_hsi)
# cv2.imshow('Imagem HSI desnormalizada', img_hsi_desnormalizada)

cv2.waitKey(0)
cv2.destroyAllWindows()

