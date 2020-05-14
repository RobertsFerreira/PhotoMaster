import cv2
import numpy as np
import math
import os
from time import sleep


def logInverso(constante, nome):

    imagem = cv2.imread(nome)

    imagemNova = cv2.imread(nome)

    colunas = imagem.shape[1]

    linhas = imagem.shape[0]

    for coluna in range(0, colunas):
        for linha in range(0, linhas):
            auxBlue = imagem[linha, coluna, 0]
            auxGreen = imagem[linha, coluna, 1]
            auxRed = imagem[linha, coluna, 2]
            azul = 10 ** (auxBlue/constante)
            azul = float("%.0f" % azul)
            verde = 10 ** (auxGreen/constante)
            verde = float("%.0f" % verde)
            vermelho = 10 ** (auxRed/constante)
            vermelho = float("%.0f" % vermelho)
            imagemNova.itemset((linha, coluna, 0), azul)
            imagemNova.itemset((linha, coluna, 1), verde)
            imagemNova.itemset((linha, coluna, 2), vermelho)

    cv2.imwrite("ImagemcomLogInverso.png", imagemNova)


def logaritmo(constante, nome):

    imagem = cv2.imread(nome)

    imagemNova = cv2.imread(nome)

    colunas = imagem.shape[1]

    linhas = imagem.shape[0]

    for coluna in range(0, colunas):
        for linha in range(0, linhas):
            auxBlue = imagem[linha, coluna, 0]
            auxGreen = imagem[linha, coluna, 1]
            auxRed = imagem[linha, coluna, 2]
            azul = constante * (math.log10(1 + auxBlue))
            verde = constante * (math.log10(1 + auxGreen))
            vermelho = constante * (math.log10(1 + auxRed))
            azul = float("%.0f" % azul)
            verde = float("%.0f" % verde)
            vermelho = float("%.0f" % vermelho)
            imagemNova.itemset((linha, coluna, 0), azul)
            imagemNova.itemset((linha, coluna, 1), verde)
            imagemNova.itemset((linha, coluna, 2), vermelho)

    cv2.imwrite("ImagemComLogaritmo.png", imagemNova)


def negativo(nivelDeCinza, nome):

    imagem = cv2.imread(nome)

    imagemNova = cv2.imread(nome)

    colunas = imagem.shape[1]

    linhas = imagem.shape[0]

    for coluna in range(0, colunas):
        for linha in range(0, linhas):
            auxBlue = imagem[linha, coluna, 0]
            auxGreen = imagem[linha, coluna, 1]
            auxRed = imagem[linha, coluna, 2]
            azul = nivelDeCinza - auxBlue
            verde = nivelDeCinza - auxGreen
            vermelho = nivelDeCinza - auxRed
            imagemNova.itemset((linha, coluna, 0), azul)
            imagemNova.itemset((linha, coluna, 1), verde)
            imagemNova.itemset((linha, coluna, 2), vermelho)

    cv2.imwrite("ImagemNegativada.png", imagemNova)


def changefiltro(filtronome, nomefoto):
    if filtronome == 'negativo':
        negativo(256, nomefoto)
    elif filtronome == 'logaritmo':
        logaritmo(105.88, nomefoto)
    elif filtronome == 'logInverso':
        logInverso(105.88, nomefoto)
    else:
        print("nada")
