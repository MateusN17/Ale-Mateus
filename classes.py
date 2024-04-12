class Aluno():
    def __init__ (self, nome, sexo, idade, matricula):
        self.nome=nome
        self.sexo=sexo
        self.idade=idade
        self.matricula=matricula
    def dizer_olá(self):
        print(f"Olá, meu nome é {self.nome}. Tenho {self.idade} "
              f"anos e minha matrícula é {self.matricula}. \nMe identifico como {self.sexo}.")
    def curso(self,curso:str):
        print(f"Estou cursando {curso}.")
    def salário(self,salario:float):
        print(f"Espero ganhar: R$ {salario}")

class Pessoa():
    def __init__(self,nome, sexo, cpf):
        self.nome=nome
        self.sexo=sexo
        self.cpf=cpf
    def dizer_olá(self):
        print(f"Olá, meu nome é {self.nome}."
              f" Meu cpf é: {self.cpf}. \nMe identifico como {self.sexo}.")
    def comer(self):
        return f"{self.nome} está comendo."
    def beber(self):
        return f"{self.nome} está bebendo."
    def falar(self, mensagem):
        return f"{self.nome} está falando: {mensagem}"
    def correr(self):
        return f"{self.nome} está correndo."    
class Carro:
    def __init__(self, marca, modelo, ano:int, cor):
        self.marca=marca
        self.modelo=modelo
        self.ano=ano
        self.cor=cor
    def ligar_carro(self):
        x=input("Digite 'sim' se deseja ligar o carro: ")
        if x=="Sim" or x=="sim":
            print(f"O {self.marca} está ligado.")
        else:
            print("Certo.")
    def desligar_carro(self,distância:float):
        return print(f"O {self.marca} está desligando, após percorrer {distância} Km.")
    def acelerar(self, velocidade:float):
        return print(f"O {self.marca} está acelerando em {velocidade}")
class Animal:
    def __init__(self, nome, idade, espécie):
        self.nome=nome
        self.idade=idade
        self.espécie=espécie
    def emitir_som(self):
        return print(f"{self.nome} está emitindo barulho.")
    def informações(self):
        return print(f"Informações sobre o animal: \n"
                     f"Nome: {self.nome}\n"
                     f"Idade: {self.idade} ano/anos\n"
                     f"Espécie: {self.espécie}")
class Produto:
    def __init__(self, nome, preço, estoque:int):
        self.nome = nome
        self.preço = preço
        self.estoque = estoque

    def atualizar_estoque(self, quantidade:int):
        return self.estoque+quantidade

    def calcular_preço_total(self, quantidade):
        return self.preço * quantidade