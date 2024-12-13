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


class cachorro:
    def __init__(self, nome, raça, idade, comer = False, brincar  = False, latir = False):
        self.nome = nome
        self.raça = raça
        self.idade = idade
        self.comer = comer
        self.brincar = brincar
        self.latir = latir

    def comendo(self):
        if self.comer:
            print (f'{self.nome} já está comendo')
            return
        if self.brincar:
            print (f'{self.nome} está brincando, ele não pode comer agora')
            return
        if self.latir:
            print (f'{self.nome} parou de latir e foi comer')
            self.latir = False
            return
        self.comer = True
        print (f'{self.nome} está comendo')

    def parar_comer(self):
        if not self.comer:
            print (f'{self.nome} não está comendo')
            return
        self.comer = False
        print (f'{self.nome} parou de comer')

    def brincando(self):
        if self.brincar:
             print (f'{self.nome} já está brincando')
             return
        if self.comer:
            print (f'{self.nome} está comendo, não pode brincar agora')
            return
        if self.latir:
            print (f'{self.nome} parou de latir e foi brincar')
            self.latir = False
        self.brincar = True
        print (f'{self.nome} está brincando')

    def parar_brincar(self):
        if not self.brincar:
            print (f'{self.nome} não está brincando')
            return
        self.brincar = False
        print (f'{self.nome} parou de brincar')

    def latindo(self):
        print ('au au')
        self.latir = True
            