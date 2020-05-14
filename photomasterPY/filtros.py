import cv2
import numpy as np
import math
import os
from time import sleep
import glob

os.system('cls')


def valorMenor():
    print("\nSuas imagens neste diretório do arquivo!!!")

    for i in glob.glob("*.*"):
        print(i)

    nome = str(input("\nDigite o nome da imagem.extensão ou diretório de outra"
                     + "(Ex.: C:\\Users\\myuser\\pasta\\imgs.bmp): "))

    imagem = cv2.imread(nome)

    imagemNova = cv2.imread(nome)

    colunas = imagem.shape[1]

    linhas = imagem.shape[0]

    auxBlue = 0
    auxGreen = 0
    auxRed = 0
    azul = 0
    verde = 0
    vermelho = 0
    valoresBlue = []
    valoresGreen = []
    valoresRed = []

    sizeMask = int(
        input('\nDigite o tamanho da máscara: '))

    if sizeMask > 0:
        flagStop = sizeMask**2
        if sizeMask % 2 == 0:
            tam = sizeMask
            for linha in range(0, linhas):
                for coluna in range(0, colunas):
                    if (coluna < colunas - tam and linha < linhas - tam):
                        for i in range(linha, (linha + tam)):
                            for j in range(coluna, (coluna + tam)):
                                auxBlue = imagem[i, j, 0]
                                valoresBlue.append(auxBlue)
                                auxGreen = imagem[i, j, 1]
                                valoresGreen.append(auxGreen)
                                auxRed = imagem[i, j, 2]
                                valoresRed.append(auxRed)
                                valoresBlue.sort()
                                valoresGreen.sort()
                                valoresRed.sort()
                        azul = min(valoresBlue, key=int)
                        verde = min(valoresGreen, key=int)
                        vermelho = min(valoresRed, key=int)
                        imagemNova.itemset((linha, coluna, 0), azul)
                        imagemNova.itemset((linha, coluna, 1), verde)
                        imagemNova.itemset((linha, coluna, 2), vermelho)
                        valoresBlue.clear()
                        valoresGreen.clear()
                        valoresRed.clear()

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

            cv2.imwrite("Imagem com MenorValor.bmp", imagemNova)

            cv2.imshow("Imagem com MenorValor", imagemNova)

        else:
            tam = int(sizeMask - 1)/2
            for linha in range(0, linhas):
                for coluna in range(0, colunas):
                    if ((coluna > tam and linha > tam)
                            and (coluna < colunas - tam and linha < linhas - tam)):
                        ct = int(coluna - tam)
                        cT = int(coluna + tam + 1)
                        lt = int(linha - tam)
                        lT = int(linha + tam + 1)
                        for i in range(lt, lT):
                            for j in range(ct, cT):
                                auxBlue = imagem[i, j, 0]
                                valoresBlue.append(auxBlue)
                                auxGreen = imagem[i, j, 1]
                                valoresGreen.append(auxGreen)
                                auxRed = imagem[i, j, 2]
                                valoresRed.append(auxRed)
                                valoresBlue.sort()
                                valoresGreen.sort()
                                valoresRed.sort()
                        azul = min(valoresBlue, key=int)
                        verde = min(valoresGreen, key=int)
                        vermelho = min(valoresRed, key=int)
                        imagemNova.itemset((linha, coluna, 0), azul)
                        imagemNova.itemset((linha, coluna, 1), verde)
                        imagemNova.itemset((linha, coluna, 2), vermelho)
                        valoresBlue.clear()
                        valoresGreen.clear()
                        valoresRed.clear()
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

                    imagemNova.itemset((linha, coluna, 0), azul)
                    imagemNova.itemset((linha, coluna, 1), verde)
                    imagemNova.itemset((linha, coluna, 2), vermelho)

            cv2.imwrite("Imagem com MenorValor.bmp", imagemNova)

            cv2.imshow("Imagem com MenorValor", imagemNova)
    else:
        print("Valo Inválido para a máscara!!!")


def valorMaior():
    print("\nSuas imagens neste diretório do arquivo!!!")

    for i in glob.glob("*.*"):
        print(i)

    nome = str(input("\nDigite o nome da imagem.extensão ou diretório de outra"
                     + "(Ex.: C:\\Users\\myuser\\pasta\\imgs.bmp): "))

    imagem = cv2.imread(nome)

    imagemNova = cv2.imread(nome)

    colunas = imagem.shape[1]

    linhas = imagem.shape[0]

    auxBlue = 0
    auxGreen = 0
    auxRed = 0
    azul = 0
    verde = 0
    vermelho = 0
    valoresBlue = []
    valoresGreen = []
    valoresRed = []

    sizeMask = int(
        input('\nDigite o tamanho da máscara: '))

    if sizeMask > 0:
        flagStop = sizeMask**2
        if sizeMask % 2 == 0:
            tam = sizeMask
            for linha in range(0, linhas):
                for coluna in range(0, colunas):
                    if (coluna < colunas - tam and linha < linhas - tam):
                        for i in range(linha, (linha + tam)):
                            for j in range(coluna, (coluna + tam)):
                                auxBlue = imagem[i, j, 0]
                                valoresBlue.append(auxBlue)
                                auxGreen = imagem[i, j, 1]
                                valoresGreen.append(auxGreen)
                                auxRed = imagem[i, j, 2]
                                valoresRed.append(auxRed)
                                valoresBlue.sort()
                                valoresGreen.sort()
                                valoresRed.sort()
                        azul = max(valoresBlue, key=int)
                        verde = max(valoresGreen, key=int)
                        vermelho = max(valoresRed, key=int)
                        imagemNova.itemset((linha, coluna, 0), azul)
                        imagemNova.itemset((linha, coluna, 1), verde)
                        imagemNova.itemset((linha, coluna, 2), vermelho)
                        valoresBlue.clear()
                        valoresGreen.clear()
                        valoresRed.clear()

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

            cv2.imwrite("Imagem com MaiorValor.bmp", imagemNova)

            cv2.imshow("Imagem com MaiorValor", imagemNova)

        else:
            tam = int(sizeMask - 1)/2
            for linha in range(0, linhas):
                for coluna in range(0, colunas):
                    if ((coluna > tam and linha > tam)
                            and (coluna < colunas - tam and linha < linhas - tam)):
                        ct = int(coluna - tam)
                        cT = int(coluna + tam + 1)
                        lt = int(linha - tam)
                        lT = int(linha + tam + 1)
                        for i in range(lt, lT):
                            for j in range(ct, cT):
                                auxBlue = imagem[i, j, 0]
                                valoresBlue.append(auxBlue)
                                auxGreen = imagem[i, j, 1]
                                valoresGreen.append(auxGreen)
                                auxRed = imagem[i, j, 2]
                                valoresRed.append(auxRed)
                                valoresBlue.sort()
                                valoresGreen.sort()
                                valoresRed.sort()
                        azul = max(valoresBlue, key=int)
                        verde = max(valoresGreen, key=int)
                        vermelho = max(valoresRed, key=int)
                        imagemNova.itemset((linha, coluna, 0), azul)
                        imagemNova.itemset((linha, coluna, 1), verde)
                        imagemNova.itemset((linha, coluna, 2), vermelho)
                        valoresBlue.clear()
                        valoresGreen.clear()
                        valoresRed.clear()
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

                    imagemNova.itemset((linha, coluna, 0), azul)
                    imagemNova.itemset((linha, coluna, 1), verde)
                    imagemNova.itemset((linha, coluna, 2), vermelho)

            cv2.imwrite("Imagem com MaiorValor.bmp", imagemNova)

            cv2.imshow("Imagem com MaiorValor", imagemNova)
    else:
        print("Valo Inválido para a máscara!!!")


def média():

    print("\nSuas imagens neste diretório do arquivo!!!")

    for i in glob.glob("*.*"):
        print(i)

    nome = str(input("\nDigite o nome da imagem.extensão ou diretório de outra"
                     + "(Ex.: C:\\Users\\myuser\\pasta\\imgs.bmp): "))

    imagem = cv2.imread(nome)

    imagemNova = cv2.imread(nome)

    colunas = imagem.shape[1]

    linhas = imagem.shape[0]

    auxBlue = 0
    auxGreen = 0
    auxRed = 0

    sizeMask = int(
        input('\nDigite o tamanho da máscara: '))

    if sizeMask > 0:
        flagStop = sizeMask**2
        if sizeMask % 2 == 0:
            tam = sizeMask
            for linha in range(0, linhas):
                for coluna in range(0, colunas):
                    if (coluna < colunas - tam and linha < linhas - tam):
                        for i in range(linha, (linha + tam)):
                            for j in range(coluna, (coluna + tam)):
                                auxBlue += imagem[i, j, 0]
                                auxGreen += imagem[i, j, 1]
                                auxRed += imagem[i, j, 2]
                        azul = auxBlue/flagStop
                        azul = float("%.0f" % azul)
                        verde = auxGreen/flagStop
                        verde = float("%.0f" % azul)
                        vermelho = auxRed/flagStop
                        vermelho = float("%.0f" % azul)
                    else:
                        auxBlue = imagem[linha, coluna, 0]
                        auxGreen = imagem[linha, coluna, 1]
                        auxRed = imagem[linha, coluna, 2]
                        azul = auxBlue
                        azul = float("%.0f" % azul)
                        verde = auxGreen
                        verde = float("%.0f" % azul)
                        vermelho = auxRed
                        vermelho = float("%.0f" % azul)
                    auxBlue = 0
                    auxGreen = 0
                    auxRed = 0

                    imagemNova.itemset((linha, coluna, 0), azul)
                    imagemNova.itemset((linha, coluna, 1), verde)
                    imagemNova.itemset((linha, coluna, 2), vermelho)

            cv2.imwrite("Imagem com Media", imagemNova)

            cv2.imshow("Imagem com Media", imagemNova)

        else:
            tam = int(sizeMask - 1)/2
            for linha in range(0, linhas):
                for coluna in range(0, colunas):
                    if ((coluna > tam and linha > tam)
                            and (coluna < colunas - tam and linha < linhas - tam)):
                        ct = int(coluna - tam)
                        cT = int(coluna + tam + 1)
                        lt = int(linha - tam)
                        lT = int(linha + tam + 1)
                        for i in range(lt, lT):
                            for j in range(ct, cT):
                                auxBlue += imagem[i, j, 0]
                                auxGreen += imagem[i, j, 1]
                                auxRed += imagem[i, j, 2]
                        azul = auxBlue/flagStop
                        azul = float("%.0f" % azul)
                        verde = auxGreen/flagStop
                        verde = float("%.0f" % azul)
                        vermelho = auxRed/flagStop
                        vermelho = float("%.0f" % azul)
                    else:
                        auxBlue = imagem[linha, coluna, 0]
                        auxGreen = imagem[linha, coluna, 1]
                        auxRed = imagem[linha, coluna, 2]
                        azul = auxBlue
                        azul = float("%.0f" % azul)
                        verde = auxGreen
                        verde = float("%.0f" % azul)
                        vermelho = auxRed
                        vermelho = float("%.0f" % azul)
                    auxBlue = 0
                    auxGreen = 0
                    auxRed = 0

                    imagemNova.itemset((linha, coluna, 0), azul)
                    imagemNova.itemset((linha, coluna, 1), verde)
                    imagemNova.itemset((linha, coluna, 2), vermelho)

            cv2.imwrite("Imagem com Media.bmp", imagemNova)

            cv2.imshow("Imagem com Media", imagemNova)
    else:
        print("Valo Inválido para a máscara!!!")


def raizquadrada():

    print("\nSuas imagens neste diretório do arquivo!!!")

    for i in glob.glob("*.*"):
        print(i)

    nome = str(input("\nDigite o nome da imagem.extensão ou diretório de outra"
                     + "(Ex.: C:\\Users\\myuser\\pasta\\imgs.bmp): "))

    imagem = cv2.imread(nome)

    imagemNova = cv2.imread(nome)

    colunas = imagem.shape[1]

    linhas = imagem.shape[0]

    valorGama = float(
        input('\nDigite o valor do Gama desejado (Entre 0 à 1): '))

    for coluna in range(0, colunas):
        for linha in range(0, linhas):
            auxBlue = imagem[linha, coluna, 0]
            auxGreen = imagem[linha, coluna, 1]
            auxRed = imagem[linha, coluna, 2]
            azul = ((auxBlue/256) ** (1/valorGama)) * 256
            verde = ((auxGreen/256) ** (1/valorGama)) * 256
            vermelho = ((auxRed/256) ** (1/valorGama)) * 256
            azul = float("%.0f" % azul)
            verde = float("%.0f" % verde)
            vermelho = float("%.0f" % vermelho)
            imagemNova.itemset((linha, coluna, 0), azul)
            imagemNova.itemset((linha, coluna, 1), verde)
            imagemNova.itemset((linha, coluna, 2), vermelho)

            cv2.imwrite("Imagem com Raiz.bmp", imagemNova)

            cv2.imshow("Imagem com Raiz", imagemNova)


def potencia(nivelDeCinza):

    print("\nSuas imagens neste diretório do arquivo!!!")

    for i in glob.glob("*.*"):
        print(i)

    nome = str(input("\nDigite o nome da imagem.extensão ou diretório de outra"
                     + "(Ex.: C:\\Users\\myuser\\pasta\\imgs.bmp): "))

    imagem = cv2.imread(nome)

    imagemNova = cv2.imread(nome)

    colunas = imagem.shape[1]

    linhas = imagem.shape[0]

    valorGama = float(
        input('\nDigite o valor do Gama desejado (Entre 0 à 1): '))

    for coluna in range(0, colunas):
        for linha in range(0, linhas):
            auxBlue = imagem[linha, coluna, 0]
            auxGreen = imagem[linha, coluna, 1]
            auxRed = imagem[linha, coluna, 2]
            azul = ((auxBlue/256)
                    ** valorGama) * 256
            verde = ((auxGreen/256)
                     ** valorGama) * 256
            vermelho = ((auxRed/256)
                        ** valorGama) * 256
            azul = float("%.0f" % azul)
            verde = float("%.0f" % verde)
            vermelho = float("%.0f" % vermelho)
            imagemNova.itemset((linha, coluna, 0), azul)
            imagemNova.itemset((linha, coluna, 1), verde)
            imagemNova.itemset((linha, coluna, 2), vermelho)

            cv2.imwrite("Imagem Potecializada.bmp", imagemNova)

            cv2.imshow("Imagem Potencializada", imagemNova)


def logInverso(constante):

    print("\nSuas imagens neste diretório do arquivo!!!")

    for i in glob.glob("*.*"):
        print(i)

    nome = str(input("\nDigite o nome da imagem.extensão ou diretório de outra"
                     + "(Ex.: C:\\Users\\myuser\\pasta\\imgs.bmp): "))

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

            cv2.imwrite("Imagem com Log Inverso.bmp", imagemNova)

            cv2.imshow("Imagem com Log Inverso", imagemNova)


def logaritmo(constante):

    print("\nSuas imagens neste diretório do arquivo!!!")

    for i in glob.glob("*.*"):
        print(i)

    nome = str(input("\nDigite o nome da imagem.extensão ou diretório de outra"
                     + "(Ex.: C:\\Users\\myuser\\pasta\\imgs.bmp): "))

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

    cv2.imwrite("Imagem Com Logaritmo.bmp", imagemNova)

    cv2.imshow("Imagem Logaritmada", imagemNova)


def negativo(nivelDeCinza):

    print("\nSuas imagens neste diretório do arquivo!!!")

    for i in glob.glob("*.*"):
        print(i)

    nome = str(input("\nDigite o nome da imagem.extensão ou diretório de outra"
                     + "(Ex.: C:\\Users\\myuser\\pasta\\imgs.bmp): "))

    imagem = cv2.imread(nome)

    imagemNova = cv2.imread(nome)

    # shape --> retorna as dimensoes da imagem e o numero de canais.
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
            # itemset -> altera o valor do canal do pixel.
            imagemNova.itemset((linha, coluna, 0), azul)
            imagemNova.itemset((linha, coluna, 1), verde)
            imagemNova.itemset((linha, coluna, 2), vermelho)

    cv2.imwrite("Imagem Negativada.bmp", imagemNova)

    cv2.imshow("Imagem Negativada", imagemNova)


def menu():

    constante = 105.88

    nivelDeCinza = 255

    while True:

        os.system('cls')

        print(
            '\n\n[1] Filtro Negativo\n[2] Filtro Logaritmo\n'
            + '[3] Filtro Log Inverso\n[4] Filtro Potência\n'
            + '[5] Filtro Raiz\n[6] Filtro Média\n'
            + '[7] Filtro Maior Valor\n[8] Filtro Menor Valor\n'
            + '[9] Sair\n')

        opção = int(input('Qual é a sua escolha: '))

        if opção == 1:

            negativo(nivelDeCinza)

            cv2.waitKey(0)

            cv2.destroyAllWindows()

            resp = int(input('\nDeseja usar novamente?\n(1) Sim - (2) Não: '))

            if resp == 2:

                print('\nObrigado por utilizar!!!\n')

                sleep(2)

                break

        elif opção == 2:

            logaritmo(constante)

            cv2.waitKey(0)

            cv2.destroyAllWindows()

            resp = int(input('\nDeseja usar novamente?\n(1) Sim - (2) Não: '))

            if resp == 2:

                print('\nObrigado por utilizar!!!\n')

                sleep(2)

                break

        elif opção == 3:

            logInverso(constante)

            cv2.waitKey(0)

            cv2.destroyAllWindows()

            resp = int(input('\nDeseja usar novamente?\n(1) Sim - (2) Não: '))

            if resp == 2:

                print('\nObrigado por utilizar!!!\n')

                sleep(2)

                break

        elif opção == 4:

            potencia(nivelDeCinza)

            cv2.waitKey(0)

            cv2.destroyAllWindows()

            resp = int(input('\nDeseja usar novamente?\n(1) Sim - (2) Não: '))

            if resp == 2:

                print('\nObrigado por utilizar!!!\n')

                sleep(2)

                break

        elif opção == 5:

            raizquadrada()

            cv2.waitKey(0)

            cv2.destroyAllWindows()

            resp = int(input('\nDeseja usar novamente?\n(1) Sim - (2) Não: '))

            if resp == 2:

                print('\nObrigado por utilizar!!!\n')

                sleep(2)

                break

        elif opção == 6:

            média()

            cv2.waitKey(0)

            cv2.destroyAllWindows()

            resp = int(input('\nDeseja usar novamente?\n(1) Sim - (2) Não: '))

            if resp == 2:

                print('\nObrigado por utilizar!!!\n')

                sleep(2)

                break

        elif opção == 7:

            valorMaior()

            cv2.waitKey(0)

            cv2.destroyAllWindows()

            resp = int(input('\nDeseja usar novamente?\n(1) Sim - (2) Não: '))

            if resp == 2:

                print('\nObrigado por utilizar!!!\n')

                sleep(2)

                break

        elif opção == 8:

            valorMenor()

            cv2.waitKey(0)

            cv2.destroyAllWindows()

            resp = int(input('\nDeseja usar novamente?\n(1) Sim - (2) Não: '))

            if resp == 2:

                print('\nObrigado por utilizar!!!\n')

                sleep(2)

                break

        elif opção == 9:

            print('\nObrigado por utilizar!!!\n')

            sleep(2)

            break

        else:

            print("\nOpção Inválida!!!\n")

            sleep(1)


def main():

    menu()


main()
