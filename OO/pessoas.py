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
    """ metodo está sempre vinculado a 1 objeto
    sempre declarar 'self' em java é 'this'
    """
    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    renzo = Pessoa(nome='Renzo')
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
    Pessoa.olhos = 3
    del luciano.olhos
    print(Pessoa.olhos)
    print(renzo.olhos)
    print(id(Pessoa.olhos), id(luciano.olhos), id(renzo.olhos))
