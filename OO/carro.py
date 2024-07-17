"""
Voce deve criar uma classe carro que vai possuir
dois atributos compostos por outras duas classes:

Motor
Direcao

O Motor tera a responsabilidade de controlar a velocidade.
Ele oferece os seguintes atributos:

Atributo de dado velocidade
Matodo acelerar, que devera incremetar a velocidade de uma unidade
Matodo frear que devera decrementar a velocidade em duas unidades
A Direcao tera a responsabilidade de controlar a direcao. Ela oferece
os seguintes atributos:

Valor de direcao com valores possiveis: Norte, Sul, Leste, Oeste.
Metodo girar_a_direita
Metodo girar_a_esquerda

       N
    O     L
       S

Exemplo:
    >>> # Testando motor
    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.acelerar()
    >>> motor.velocidade
    3
    >>> motor.frear()
    >>> motor.velocidade
    1
    >>> motor.frear()
    >>> motor.velocidade
    0
    >>> # Testando Direcao
    >>> direcao = Direcao()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Norte'
    >>> carro = Carro(direcao, motor)
    >>> carro.calcular_velocidade()
    0
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    1
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    2
    >>> carro.frear()
    >>> carro.calcular_velocidade()
    0
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_direita()
    >>> carro.calcular_direcao()
    'Leste'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Oeste'
"""
NORTE = 'Norte'
SUL = 'Sul'
LESTE = 'Leste'
OESTE = 'Oeste'

class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        if self.velocidade < 2:
            self.velocidade = 1
        else:
            self.velocidade -= 2
            self.velocidade = max(0, self.velocidade)

class Direcao:

    rotacao_a_direita_dict = {
        NORTE: LESTE, LESTE: SUL, SUL: OESTE, OESTE: NORTE
    }

    rotacao_a_esquerda_dict = {
        NORTE: OESTE, OESTE: SUL, SUL: LESTE, LESTE: NORTE
    }

    def __init__(self):
        self.valor = NORTE

    def girar_a_direita(self):
        self.valor = self.rotacao_a_direita_dict[self.valor]

        # if self.valor == 'Norte':
        #     self.valor = 'Leste'
        # elif self.valor == 'Leste':
        #     self.valor = 'Sul'
        # elif self.valor == 'Sul':
        #     self.valor = 'Oeste'
        # else:
        #     self.valor = 'Norte'

    def girar_a_esquerda(self):
        self.valor = self.rotacao_a_esquerda_dict[self.valor]
        # if self.valor == 'Norte':
        #     self.valor = 'Oeste'
        # elif self.valor == 'Oeste':
        #     self.valor = 'Sul'
        # elif self.valor == 'Sul':
        #     self.valor = 'Leste'
        # else:
        #     self.valor = 'Norte'


class Carro:

    def __init__(self, direcao, motor):
        self.motor = motor
        self.direcao = direcao

    def acelerar(self):
        return self.motor.acelerar()

    def frear(self):
        return self.motor.frear()

    def calcular_velocidade(self):
        return self.motor.velocidade

    def girar_a_direita(self):
        self.direcao.girar_a_direita()

    def girar_a_esquerda(self):
        self.direcao.girar_a_esquerda()

    def calcular_direcao(self):
        return self.direcao.valor


if __name__ == '__main__':
    motor = Motor()
    direcao = Direcao()
    carro = Carro(motor, direcao)
    print(carro.calcular_velocidade())
    carro.acelerar()
    print(carro.calcular_velocidade())
    carro.acelerar()
    print(carro.calcular_velocidade())
    carro.frear()
    print(carro.calcular_velocidade())
    carro.frear()
    print(carro.calcular_velocidade())
    print(carro.direcao.valor)
    carro.girar_a_esquerda()
    print(carro.direcao.valor)
    carro.girar_a_esquerda()
    print(carro.direcao.valor)
    carro.girar_a_esquerda()
    print(carro.direcao.valor)
    carro.girar_a_esquerda()

    carro.calcular_direcao()
    carro.girar_a_direita()
    carro.calcular_direcao()
    carro.girar_a_direita()
    carro.calcular_direcao()
    carro.girar_a_direita()
    carro.calcular_direcao()
    carro.girar_a_direita()
    carro.calcular_direcao()
