from classes import Retangulo
if __name__ == "_main_":
    altura = 5
    largura = 10
    retangulo1 = Retangulo(altura, largura)
    print("Área do retângulo:", retangulo1.calcular_area())
    print("Perímetro do retângulo:", retangulo1.calcular_perimetro())