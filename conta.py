<<<<<<< HEAD
class ContaBancária:
    def __init__(self, númerodeconta, saldo, titular):
        self.númerodeconta = númerodeconta
        self.saldo = saldo
        self.titular = titular

    def depositar(self, valor):
         self.total=self.saldo+valor
         return f"{self.titular} está depositando R$ {valor}.\n Saldo atual de R$ {self.total}"
    
    def sacardinheiro(self,valor):
        self.total=self.saldo-valor
        return f"{self.titular} está sacando R$ {valor}.\n Saldo atual de R$ {self.saldo}"
=======
from classes import ContaBancária
>>>>>>> 71fe917cf7842161f2b83b6cab73f66060855206

if __name__ == "_main":
    conta = ContaBancária("0987656",11,"pessoa humana")
    print(conta.depositar(100))
<<<<<<< HEAD
    print(conta.sacardinheiro(100))
    

class Triângulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def perimetro(self):
        todos = self.lado1 + self.lado2 + self.lado3 
        return f"o primeiro e igual: {todos}"
    
    def área(self):
        todos = self.lado1 + self.lado2 + self.lado3
        return f"o primeiro e igual:{todos}"
    
if __name__ == "main":
    lados = Triângulo(13,11,15)
    print(lados.perimetro())
    print(lados.área())

    
=======
    print(conta.sacardinheiro(100))
>>>>>>> 71fe917cf7842161f2b83b6cab73f66060855206
