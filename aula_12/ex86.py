# Crie um programa para um sistema de reservas de quartos 
# de hotel, onde as chaves são números dos quartos 
# e os valores são booleanos para indicar se o quarto está 
# disponivel(True) ou ocupado(False). O programa deve 
# permitir que o usuario consulte wa disponibilidade de
# quartos, reserve um quarto específico e cancele uma reserva
# Ao realizar uma reserva< o etado do quarto deve ser atualizado
# no dicionario

quartos = {
        101: True,
        102: True,
        103: False,
        104: True,
        105: False}

def mostrar_disponibilidade():
    print("Disponibilidade dos quartos:")
    for quarto, disponivel in quartos.items():
        if disponivel:
            print(f"Quarto {quarto}: Disponível")
        else:
            print(f"Quarto {quarto}: Ocupado")

def fazer_reserva():
    quarto = int(input("Digite o número do quarto que deseja reservar: "))
    if quarto in quartos:
        if quartos[quarto]:
            quartos[quarto] = False
            print(f"Quarto {quarto} reservado com sucesso!")
        else:
            print(f"O quarto {quarto} já está ocupado.")
    else:
        print("Quarto inválido.")

def cancelar_reserva():
    quarto = int(input("Digite o número do quarto que deseja cancelar a reserva: "))
    if quarto in quartos:
        if not quartos[quarto]:
            quartos[quarto] = True
            print(f"Reserva do quarto {quarto} cancelada com sucesso!")
        else:
            print(f"O quarto {quarto} não está reservado.")
    else:
        print("Quarto inválido.")

while True:
    print("1 - Mostrar disponibilidade dos quartos")
    print("2 - Fazer reserva de um quarto")
    print("3 - Cancelar reserva de um quarto")
    print("0 - Sair")

    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        mostrar_disponibilidade()
    elif opcao == 2:
        fazer_reserva()
    elif opcao == 3:
        cancelar_reserva()
    elif opcao == 0:
        break
    else:
        print("Opção inválida. Digite novamente.")
