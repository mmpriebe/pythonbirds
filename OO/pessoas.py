class Pessoa:
    """Atributos de um objeto, __init__ metodo contrutor
    da classe.
    """
    def __init__(self, nome=None, idade=35):
        self.nome = nome
        self.idade = idade
    """ metodo está sempre vinculado a 1 objeto
    sempre declarar 'self' em java é 'this'
    """
    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    p = Pessoa('Marciano')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'Marciano'
    print(p.nome)
    print(p.idade)
