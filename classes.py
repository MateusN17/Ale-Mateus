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
class ContaBancária:
    def _init_(self, númerodeconta, saldo, titular):
        self.númerodeconta = númerodeconta
        self.saldo = saldo
        self.titular = titular

    def depositar(self, valor):
        self.total=self.saldo+valor
        return f"{self.titular} está depositando R$ {valor}.\n Saldo atual de R$ {self.total}"
    
    def sacardinheiro(self,valor):
        self.total=self.saldo-valor
        return f"{self.titular} está sacando R$ {valor}.\n Saldo atual de R$ {self.saldo}"
class Triangulo:
    def _init_(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def perimetro(self):
        todos=self.lado1 + self.lado2 + self.lado3
        return f'o perimetro e igual: {todos}'

    def area(self):
        todos=self.lado1 + self.lado2 + self.lado3 / 2
        return f'o perimetro e igual: {todos}'
class Livro:
    def _init_(self, titulo, autor, num_paginas):
        self.titulo = titulo
        self.autor = autor
        self.num_paginas = num_paginas

    def mostrar_informacoes(self):
        print("Título:", self.titulo)
        print("Autor:", self.autor)
        print("Número de páginas:", self.num_paginas)

    def calcular_palavras_por_pagina(self, total_palavras):
        palavras_por_pagina = total_palavras / self.num_paginas
        return palavras_por_pagina
class Retangulo:
    def _init_(self, altura, largura):
        self.altura = altura
        self.largura = largura

    def calcular_area(self):
        return self.altura * self.largura

    def calcular_perimetro(self):
        return 2 * (self.altura + self.largura)
class Estudante:
    def _init_(self, nome, idade, notas):
        self.nome = nome
        self.idade = idade
        self.notas = notas

    def calcular_media(self):
        if len(self.notas) == 0:
            return 0
        else:
            return sum(self.notas) / len(self.notas)

    def verificar_aprovacao(self):
        media = self.calcular_media()
        if media >= 6.0:
            return "Aprovado"
        else:
            return "Reprovado"
class Pedido:
    def _init_(self):
        self.itens = {} 
        self.total = 0.0  
        self.status = "Pendente" 

    def adicionar_item(self, item, preco):
        self.itens[item] = preco
        self.total += preco

    def calcular_total(self):
        return self.total

    def alterar_status(self, novo_status):
        self.status = novo_status
