# Classe "Cachorro":
# Crie uma classe chamada "Cachorro" que possuem o métado
# __init__ para inicializar as propriedades "nome"  e "idade"
# do cachorro. Em seguida, crie um objeto da classse "Cachorro"
# e imprima o nome e a idade do cachorro

class Cachorro:
     def __init__(self, nome, idade):
         self.nome = nome
         self.idade = idade
         
         
def main():
    cachorro = get_cachorro()
    print(f"O cachorro {cachorro.nome} tem {cachorro.idade} anos")
    
    
def get_cachorro():
    nome = input("Nome: ").upper()
    idade = int(input("Idade: "))
    return Cachorro(nome, idade)
    
    
main()
