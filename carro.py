from classes import Carro

if __name__=="__main__":
    carro1=Carro(marca=input("Insira a marca: "), modelo=input("Insira o modelo: "), ano=input("Insira o ano: "), cor=input("Insira a cor do carro: "))
    y=input("Insira quantos quilometros você quer percorrer até parar: ")
    z=input("Insira a velocidade que você deseja alcançar: ")
carro1.ligar_carro()
carro1.acelerar(z)
carro1.desligar_carro(y)