class Pessoa:
    """Atribudo de classe (default) são definidos fora do __init__"""
    olhos = 2

    """Atributos de instancia, __init__ metodo contrutor
    da classe.
    """
    def __init__(self, *filhos, nome=None, idade=35):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)
    """ 
    metodo está sempre vinculado a 1 objeto
    sempre declarar 'self' em java é 'this'
    """
    def cumprimentar(self):
        return f'Olá, meu nome é {self.nome}'

    @classmethod
    def nome_e_atributos_de_class(cls):
        return f'{cls} - olhos {cls.olhos}'

    """ Metodo de classe, statico"""
    @staticmethod
    def metodo_estatico():
        return 42


class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe = super().cumprimentar()
        return f'{cumprimentar_da_classe}. Aperto de mão'


class Mutante(Pessoa):
    olhos = 1


if __name__ == '__main__':
    renzo = Homem(nome='Renzo')
    luciano = Pessoa(renzo, nome='Luciano')
    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.cumprimentar())
    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho)
    luciano.sobrenome = 'Ramalho'
    luciano.sobrenome
    del luciano.filhos
    luciano.olhos = 1
    """Atributo de instancia"""
    print(luciano.__dict__)
    print(renzo.__dict__)
    del luciano.olhos
    print(Pessoa.olhos)
    print(renzo.olhos)
    print(id(Pessoa.olhos), id(luciano.olhos), id(renzo.olhos))
    print(Pessoa.metodo_estatico(), luciano.metodo_estatico())
    print(
        Pessoa.nome_e_atributos_de_class(),
        luciano.nome_e_atributos_de_class()
    )

    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(renzo, Pessoa))
    print(isinstance(renzo, Homem))
    print(renzo.olhos)
    print(luciano.cumprimentar())
    print(renzo.cumprimentar())
