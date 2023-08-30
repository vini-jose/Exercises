# Desenvolva uma classe Book com atributos title, author e year. Implemente um método 
# get_age que retorna quantos anos o livro tem desde o ano atual.

class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def get_ano(self):
        anos_livro = 2023 - self.ano
        print(f"O livro {self.titulo} do autor {self.autor} lançado no ano {self.ano}, atualmente tem {anos_livro} anos")

titulo_1 = input("Digite o nome do livro: ")
autor_1 = input("Digite o nome do autor do livro: ")
ano_1 = int(input("Digite o ano do livro: "))

livro = Livro(titulo_1, autor_1, ano_1)
livro.get_ano()