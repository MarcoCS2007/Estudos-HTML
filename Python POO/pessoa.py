class Pessoa:
    def __init__(self, nome, idade, comento = False, falando = False):
        self.nome = nome
        self.idade = idade
        self.comento = comento
        self.falando = falando

    def comer(self, alimento = ''):
        if self.comendo:
            print(f'{self.nome} já está comendo')
            return
        print(f'{self.nome} está comendo {alimento}')
        self.comendo=True

    def falando(self):
        print(f'{self.nome} está falando...')

    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo')
            return
        print(f'{self.nome} parou de comer')
        self.comendo=False