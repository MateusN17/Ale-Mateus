from classes import Livro
if __name__ == "_main_":
    livro1 = Livro("De Sangue e Cinzas", "Jennifer L", 593)
    livro1.mostrar_informacoes()
    total_palavras = 64000  # Exemplo de total de palavras no livro
    palavras_por_pagina = livro1.calcular_palavras_por_pagina(total_palavras)
    print("Palavras por página:", palavras_por_pagina)