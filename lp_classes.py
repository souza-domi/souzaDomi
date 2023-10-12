

class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material
    
    def trocaCor(self, nova_cor):
        self.cor = nova_cor
    
    def mostraCor (self):
        return self.cor
    
    
class Quadrado:
    def __init__(self, lado):
        self.lado = lado
    
    def mudaLado(self, novo_lado):
        self.lado = novo_lado
    
    def mostraLado(self):
        return self.lado
    
    def area (self):
        return pow(self.lado,2)
    

class Retangulo:

    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura
    
    def mudaLado(self, nova_largura, novo_comprimento): 
        self.largura = nova_largura
        self.comprimento = novo_comprimento
    
    def mudaBcomprimento(self, novo_comprimento):
        self.comprimento = novo_comprimento
    
    def mostraLargura (self):
        return self.largura
    
    def mostracomprimento(self):
        return self.comprimento
    
    def area(self):
        return self.largura * self.comprimento
    
    def perimetro(self):
        return 2*(self.largura + self.comprimento)

class Pessoa:

    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, anos):
        self.idade += anos
        if self.idade < 21:
            self.altura += anos * 0.5   
        
    def engordar(self, peso):
        self.peso += peso

    def emagerecer(self, peso):
        if peso >= self.peso:
            self.peso = 0
        else:
            self.peso -= peso

    def crescer(self, altura):
        self.altura += altura

class ContaCorrente:

    def __init__(self, numero, nome, saldo = 0):
        self.numero = numero
        self.nome = nome
        self.saldo = saldo
    
    def alterarNome(self, novo_nome):
        self.nome = novo_nome

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        if valor >= self.saldo:
            self.saldo = 0
        else:
            self.saldo -= valor

class TV:
    def __init__(self, canal, volume):
        self.canal = canal
        self.volume = volume
    
    def mudarCanal(self, novo_canal):
        self.canal = novo_canal
    
    def aumentarVolume (self):
        if self.volume < 100:
            self.volume += 1 

    def diminuirVolume (self):
        if self.volume > 0:
            self.volume -= 1
    
class Tamagushi:
    def __init__ (self, nome, fome, saude, idade):

        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade
    
    def mudarNome(self, novo_nome):
        self.nome = novo_nome
        return self.nome
    
    def getNome (self):
        return self.nome
    
    def fome (self):
        return self.fome

    def saude (self):
        return self.saude

    def idade (self):
        return self.idade

    def humor (self):
        return (self.fome + self.saude) / 2
    
class Macaco:
    def __init__ (self, nome):
        self.nome = nome
        self.bucho = []
        
    def comer(self, alimento):
        self.bucho.append(alimento)

    def verBucho(self):
        return self.bucho

    def digerir(self):
        list.clear(self.bucho)
'''
macaco01 = Macaco('abu')
macaco02 = Macaco('chico')

macaco01.comer('banana')
print(macaco01.verBucho())
macaco02.comer('melancia')
print(macaco02.verBucho())
macaco01.comer('laranja')
print(macaco01.verBucho())
macaco02.comer(macaco01)
print(macaco02.verBucho())
'''
class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getPontos (self):
        print(str.format('x = {} e y = {}',self.x,self.y))
    

class BombaCombustivel:
    def __init__(self, combustivel, valorLitro, quantidade = 0, capacidade = 1000):
        self.tipoCombustivel = combustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidade
        self.capacidade = capacidade

    def abastecerPorValor(self, valorAbastecido):
        self.quantidadeCombustivel = valorAbastecido / self.valorLitro
        BombaCombustivel.atualizaBomba()
        return self.quantidadeCombustivel

        
    def abastecerPorLitro (self):
        BombaCombustivel.atualizaBomba()
        return self.quantidadeCombustivel * self.valorLitro 

    def alterarValor(self, novo_valor):
        self.valorLitro = novo_valor

    def alterarCombustivel(self, novo_combustivel):
        self.tipoCombustivel = novo_combustivel
    
    def alterarQuantidadeCombustivel(self, nova_quantidade):
        self.quantidadeCombustivel = nova_quantidade
    
    def atualizaBomba(self):
        nova_capacidade = self.capacidade - self.quantidadeCombustivel
        self.capacidade = nova_capacidade

class Carro:

    def __init__(self, quilometrosLitro):
        self.quilometrosLitro = quilometrosLitro
        self.combustivel = 0

    def adicionarGasolina(self, quantidade):
        self.combustivel += float(quantidade)

    def andar(self, distancia):
        gasto = distancia / self.quilometrosLitro
        self.combustivel -= gasto

    def obterGasolina(self):
        print self.combustivel

class ContaInvestimento:

    def __init__(self, numero, nomeCorrentista, taxaJuros, saldo=0.0):
        self.numero = numero
        self.alterarNome(nomeCorrentista)
        self.taxaJuros = taxaJuros
        self.saldo = saldo

    def alterarNome(self, nomeCorrentista):
        self.nomeCorrentista = nomeCorrentista

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        self.saldo -= valor

    def adicionaJuros(self):
        self.saldo += (self.saldo * (self.taxaJuros / 100.0))

class Funcionario:

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = float(salario)

    def getNome(self):
        return self.nome
    
    def getSalario(self):
        return self.salario
    
    def aumentarSalario(self, percentualDeAumento):
        self.salario += self.salario * (percentualDeAumento / 100.0)
    
    




        
    
