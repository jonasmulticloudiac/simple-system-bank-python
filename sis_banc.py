import sys

# Variáveis para armazenar saldo, depósitos e saques
saldo = 0.0
limite_saque = 500.0
saques_diarios = 3
saques_realizados = 0
extrato = []

def depositar(valor):
    global saldo
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
    else:
        print("O valor do depósito deve ser positivo!")

def sacar(valor):
    global saldo, saques_realizados
    if saques_realizados >= saques_diarios:
        print("Limite de saques diários atingido.")
    elif valor > limite_saque:
        print(f"O valor máximo para saque é R$ {limite_saque:.2f}")
    elif valor > saldo:
        print("Saldo insuficiente para realizar o saque.")
    else:
        saldo -= valor
        saques_realizados += 1
        extrato.append(f"Saque: R$ {valor:.2f}")
        print(f"Saque de R$ {valor:.2f} realizado com sucesso.")

def mostrar_extrato():
    print("\nExtrato:")
    if len(extrato) == 0:
        print("Nenhuma movimentação realizada.")
    else:
        for movimento in extrato:
            print(movimento)
    print(f"Saldo atual: R$ {saldo:.2f}\n")

def menu():
    print("""
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    """)

# Loop principal do sistema
while True:
    menu()
    opcao = input("Escolha uma opção: ").lower()

    if opcao == 'd':
        valor = float(input("Informe o valor do depósito: R$ "))
        depositar(valor)
    
    elif opcao == 's':
        valor = float(input("Informe o valor do saque: R$ "))
        sacar(valor)
    
    elif opcao == 'e':
        mostrar_extrato()
    
    elif opcao == 'q':
        print("Saindo do sistema. Até mais!")
        sys.exit()
    
    else:
        print("Opção inválida, tente novamente.")
