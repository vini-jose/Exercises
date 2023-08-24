# Crie um programa que receba o nome e as notas(2) de 3 
# disciplinas de um aluno.  Armazene essas informações 
# em um dicionario onde a chave é o nome da disciplina
# e o valor é sua nota. No final, calcule a média das notas
# e exiba o nome do aluno< as disciplinas com suas respectivas 
# notas e a média calculada

def get_disciplinas():
    disciplinas = {}

    nome_aluno = input("Digite o nome do aluno: ")

    for i in range(3):
        disciplina = input("Digite o nome da disciplina: ")
        nota1 = float(input("Digite a primeira nota: "))
        nota2 = float(input("Digite a segunda nota: "))
        disciplinas[disciplina] = [nota1, nota2]

    for disciplina, notas in disciplinas.items():
        media_disciplina = sum(notas) / len(notas)
        print(f"O aluno {nome_aluno} na materia de {disciplina} teve as notas {notas[0]} e {notas[1]} e a media das notas foi: {media_disciplina}") 
        

get_disciplinas()