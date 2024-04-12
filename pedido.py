from classes import Pedido
if __name__ == "_main_":
    pedido1 = Pedido()
    pedido1.adicionar_item("Hambúrguer", 10.0)
    pedido1.adicionar_item("Batata Frita", 5.0)
    pedido1.adicionar_item("Refrigerante", 3.0)
    
    print("Itens do Pedido:", pedido1.itens)
    print("Total a ser pago:", pedido1.calcular_total())
    
    novo_status = "Em Preparo"
    pedido1.alterar_status(novo_status)
    print("Status do Pedido:", pedido1.status)