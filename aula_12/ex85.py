# Crie um programa que receba o nome e as notas(2) de 3 
# disciplinas de um aluno.  Armazene essas informações 
# em um dicionario onde a chave é o nome da disciplina
# e o valor é sua nota. No final, calcule a média das notas
# e exiba o nome do aluno< as disciplinas com suas respectivas 
# notas e a média calculada

disciplinas = {
    "Historia": [6, 4],
    "Geografia": [8, 10],
    "Matematica": [9, 8]
}

for disciplina, notas in disciplinas.items():
    print(disciplina, notas[0], notas[1])