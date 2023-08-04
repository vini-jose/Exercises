# Classe "Pessoa"
# Crie uma classe chamada "Pessoa" que possua o método __init__
# para inicializar as propriedades "nome",  "idade" e "profissão"
# da pessoa. Em seguida, crie um objeto da classe "Pessoa" e
# imprima todas as suas informações (nome, idade e profissão)

class Pessoa:
    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

def criar_pessoa():
    nome = get_nome()
    idade = get_idade()
    profissao = get_profissao()
    
    pessoa = Pessoa(nome, idade, profissao)
    
    print(f"{nome} tem {idade} anos e trabalha como {profissao}")
    return pessoa
    
         
def get_nome():
    return input("Digite seu nome: ")

def get_idade():
    return int(input("Digite sua idade: "))

def get_profissao():
    return input("Digite sua profissão: ")

criar_pessoa()