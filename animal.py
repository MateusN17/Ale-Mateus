from classes import Animal
import os
os.system('cls')
if __name__=="__main__":
    animal1 = Animal(nome=input("Insira o nome do animal: "), idade=input("Insira a idade do animal: "), espécie=input("Insira a espécie do animal: "))
import os
os.system('cls')
animal1.informações()
animal1.emitir_som()