"""
Devemos desenvolver uma aplicação onde ao ser inicializada solicite ao usuário escolher o nível de dificuldade do jogo e
após isso gera e apresenta, de forma aleatória, um cálculo para que possamos informar o resultado.
Iremos limitar as operações em somar, diminuir e multiplicar.
Se o usuário acertar a resposta, somará um ponto ao seu socre.
Acertando ou errando ele poderá ou não continuar no jogo.
"""
from random import randint


class Extrutura:

    def __init__(self, dificuldade):
        self.__dificuldade = dificuldade
        self.__valor01 = self.gerar_valor()
        self.__valor02 = self.gerar_valor()
        self.__sinal = randint(1, 3)
        self.__resultado = self.gerar_resultado()

    @property
    def retorna_dificuldade(self):
        return self.__dificuldade

    @property
    def retorna_valor01(self):
        return self.__valor01

    @property
    def retorna_valor02(self):
        return self.__valor02

    def gerar_valor(self):
        if self.__dificuldade == 1:
            return randint(0, 10)
        elif self.__dificuldade == 2:
            return randint(0, 100)
        elif self.__dificuldade == 3:
            return randint(0, 1_000)
        elif self.__dificuldade == 4:
            return randint(0, 10_000)
        else:
            return 'Dificuldade inválida'

    def gerar_sinal(self):
        if self.__sinal == 1:
            return '+'
        elif self.__sinal == 2:
            return '-'
        else:
            return '*'

    def gerar_conta(self):
        if self.__sinal == 1:
            return f'{self.__valor01} + {self.__valor02} = ?'
        elif self.__sinal == 2:
            return f'{self.__valor01} - {self.__valor02} = ?'
        else:
            return f'{self.__valor01} * {self.__valor02} = ?'

    def gerar_resultado(self):
        if self.__sinal == 1:
            return self.__valor01 + self.__valor02
        elif self.__sinal == 2:
            return self.__valor01 - self.__valor02
        else:
            return self.__valor01 * self.__valor02
