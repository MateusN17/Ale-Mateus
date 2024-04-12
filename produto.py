from classes import Produto
# Exemplo de uso da classe Produto
produto1 = Produto(nome=input("Insira o nome do produto: "), preço=input("Insira o preço do produto: "), estoque=input("Insira a quantidade disponível no estoque: "))
print(f"Produto: {produto1.nome}, Preço: {produto1.preço}, Estoque: {produto1.estoque}")

# Atualizar estoque e calcular preço total
x=input("Insira a nova quantidade do estoque: ")
produto1.atualizar_estoque(x)
print(f"Novo estoque: {produto1.estoque}")

quantidade_desejada = input("Insira a quantidade desejada: ")
preço_total = produto1.calcular_preço_total(quantidade_desejada)
print(f"Preço total para {quantidade_desejada} unidades: {preço_total}") 