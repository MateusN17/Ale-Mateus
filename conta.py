from classes import ContaBancária

if __name__ == "_main":
    conta = ContaBancária("0987656",11,"pessoa humana")
    print(conta.depositar(100))
    print(conta.sacardinheiro(100))