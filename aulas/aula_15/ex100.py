# Desafio
# Crie uma classe VerificaCPF que possui um método da classe que 
# verifica e valida um cpf retornando True caso seja um CPF válido e False para um CPF inválido

class VerificaCPF:
    def __init__(self, cpf) -> None:
        self.cpf = cpf

    @classmethod
    def get(cls):
        cpf = float