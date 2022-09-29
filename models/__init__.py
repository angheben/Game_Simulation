"""
Eu posso atribuir um método a um atributo, por exemplo
"""

from random import randint


class Jogo:
    def __init__(self):
        self.valor1 = gerar_valor()
        self.valor2 = gerar_valor()

    @property
    def gerar_valor(self):
        valor = randint(1, 60)
        return valor

