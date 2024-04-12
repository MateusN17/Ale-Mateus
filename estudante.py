from classes import Estudante
if __name__ == "_main_":
    nome = "João"
    idade = 20
    notas = [7.5, 8.0, 6.5, 9.0]
    estudante1 = Estudante(nome, idade, notas)
    print("Nome:", estudante1.nome)
    print("Idade:", estudante1.idade)
    print("Notas:", estudante1.notas)
    print("Média das notas:", estudante1.calcular_media())
    print("Situação:", estudante1.verificar_aprovacao())