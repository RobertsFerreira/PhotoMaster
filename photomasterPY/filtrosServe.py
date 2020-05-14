import cv2
import numpy as np
import math
import os
from time import sleep


def prewitt(nome):

    imagem = cv2.imread(nome)

    imagemNova = cv2.imread(nome)

    colunas = imagem.shape[1]

    linhas = imagem.shape[0]

    sizeMask = 3

    flagStop = sizeMask**2

    pixelB = 0
    pixelG = 0
    pixelR = 0
    pixelB2 = 0
    pixelG2 = 0
    pixelR2 = 0
    cont = 0

    tam = int(sizeMask - 1)/2
    for linha in range(0, linhas):
        for coluna in range(0, colunas):
            if ((coluna > tam and linha > tam)
                    and (coluna < colunas - tam and linha < linhas - tam)):

                ct = int(coluna - tam)
                cT = int(coluna + tam+1)
                lt = int(linha - tam)
                lT = int(linha + tam+1)
                for i in range(lt, lT):
                    for j in range(ct, cT):
                        if cont < 3:

                            pixelB -= imagem[i, j, 0]
                            pixelG -= imagem[i, j, 1]
                            pixelR -= imagem[i, j, 2]

                        elif cont > 5:

                            pixelB += imagem[i, j, 0]
                            pixelG += imagem[i, j, 1]
                            pixelR += imagem[i, j, 2]

                        cont += 1

                cont = 0

                for j in range(ct, cT):
                    for i in range(lt, lT):

                        if cont < 3:

                            pixelB2 -= imagem[i, j, 0]
                            pixelG2 -= imagem[i, j, 1]
                            pixelR2 -= imagem[i, j, 2]

                        elif cont > 5:

                            pixelB2 += imagem[i, j, 0]
                            pixelG2 += imagem[i, j, 1]
                            pixelR2 += imagem[i, j, 2]

                        cont += 1

                auxBlue = (np.abs(pixelB) + np.abs(pixelB2))

                auxGreen = (np.abs(pixelG) + np.abs(pixelG2))

                auxRed = (np.abs(pixelR) + np.abs(pixelR2))

                if auxBlue > 255:
                    auxBlue = 255
                elif auxBlue < 0:
                    auxBlue = 0

                if auxGreen > 255:
                    auxGreen = 255
                elif auxGreen < 0:
                    auxGreen = 0

                if auxRed > 255:
                    auxRed = 255
                elif auxRed < 0:
                    auxRed = 0

                imagemNova.itemset((linha, coluna, 0), auxBlue)
                imagemNova.itemset((linha, coluna, 1), auxGreen)
                imagemNova.itemset((linha, coluna, 2), auxRed)

                pixelB = 0
                pixelG = 0
                pixelR = 0
                pixelB2 = 0
                pixelG2 = 0
                pixelR2 = 0
                cont = 0

            else:
                auxBlue = imagem[linha, coluna, 0]
                auxGreen = imagem[linha, coluna, 1]
                auxRed = imagem[linha, coluna, 2]
                azul = auxBlue
                verde = auxGreen
                vermelho = auxRed
                imagemNova.itemset((linha, coluna, 0), azul)
                imagemNova.itemset((linha, coluna, 1), verde)
                imagemNova.itemset((linha, coluna, 2), vermelho)

    cv2.imwrite("ImagemcomPrewitt", imagemNova)


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
    elif filtronome == 'prewitt':
        prewitt(nomefoto)
    else:
        print("nada")
