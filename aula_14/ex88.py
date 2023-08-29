# Crie uma classe de "Estudante". A classe deve conter os atributos 
# "name", "age" e "grade". Depois, instancie um objeto a esta classe 
# e por fim crie um método para printar na tela esses atributos criados

class Estudante:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def pessoa(self):
        return f"O nome do aluno é {self.name} ele tem {self.age} anos e a nota dele é {self.grade}"

aluno_1 = Estudante("José", 19, 10)

print(aluno_1.pessoa())