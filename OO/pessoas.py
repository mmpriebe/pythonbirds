class Pessoa:
    """ metodo está sempre vinculado a 1 objeto
    sempre declarar 'self' em java é 'this'
    """
    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    p = Pessoa()
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
