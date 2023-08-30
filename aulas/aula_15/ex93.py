# Crie uma classe Student com atributos name, age e grades (uma lista). 
# Adicione métodos para adicionar notas, calcular a média das notas e exibir as informações do aluno.

class Estudante:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nota = []
    
    def add_nota(self, nota):
        self.nota.append(nota)
    
    def calculando_media(self):
        total = sum(self.nota)
        media = total / len(self.nota)
        print(f"A média das notas é: {media}")
    
    def info(self):
        print("Aluno:", self.nome)
        print("Idade:", self.idade)
        print("Notas:", self.nota)

nome_1 = input("Digite seu nome: ")
idade_1 = int(input("Digite sua idade: "))

aluno = Estudante(nome_1, idade_1)

for i in range(0, 5):
    nota_1 = float(input("Digite a nota: "))
    aluno.add_nota(nota_1)

aluno.info()
aluno.calculando_media()