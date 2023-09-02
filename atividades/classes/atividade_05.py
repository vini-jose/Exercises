# Classe TV: Faça um programa que simule um televisor criando-o como um objeto. 
# O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume. 
# Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas

class Televisor:
    def __init__(self):
        self.canal = 1
        self.volume = 50
        
    def alterar_canal(self, novo_canal):
        if 1 <= novo_canal <= 100:
            self.canal = novo_canal
            return f"Canal alterado para {novo_canal}"
        else:
            return "Canal inválido"
        
    def aumentar_volume(self):
        if self.volume < 100:
            self.volume += 1
            return f"Volume aumentado para {self.volume}"
        else:
            return "Volume máximo atingido"
        
    def diminuir_volume(self):
        if self.volume > 0:
            self.volume -= 1
            return f"Volume diminuído para {self.volume}"
        else:
            return "Volume mínimo atingido"
        
def main():
    tv = Televisor()
    print(f"Canal atual: {tv.canal}")
    print(f"Volume atual: {tv.volume}")
    
    novo_canal = int(input("Informe o número do canal: "))
    resultado = tv.alterar_canal(novo_canal)
    print(resultado)
    
    opcao = input("Deseja aumentar ou diminuir o volume? (a/d): ")
    if opcao == "a":
        resultado = tv.aumentar_volume()
        print(resultado)
    elif opcao == "d":
        resultado = tv.diminuir_volume()
        print(resultado)
    else:
        print("Opção inválida")

main()