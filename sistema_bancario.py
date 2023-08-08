saldo = 0.0
extrato = '''Extrato de hoje: \n'''
qtde_saque = 0
VALOR_LIMITE_SAQUE = 500
QTDE_LIMITE_SAQUE = 3
MENU = """
=================================
-----------MENU------------------

Escolha uma das operações:

    [1] - Depositar
    [2] - Sacar
    [3] - Extrato
    [4] - Sair

=================================
"""
while True:
    option = int(input(MENU))
    if option == 1:
        deposito = 0.0
        while deposito <= 0:
            deposito = float(input("Insira o valor do depósito: "))
            if deposito > 0:
                saldo += deposito
                extrato += f"\n     Depósito realizado no valor de R$ {deposito: .2f}\n------------------------------------------------------------"
                print("Valor depositado!")
            else:
                print("Valor inválido. O valor do depósito precisa ser maior que R$ 0")

    elif option == 2:
        while True:
            print("Saldo atual: R$ " , saldo)
            saque = 0
            while saque <= 0:
                saque = float(input("Insira o valor do saque: "))
                if saque < 0:
                    print("O valor do saque não pode ser negativo!")
            if saque > saldo:
                print("O valor do saque é maior que o saldo disponível!")
            elif saque > 500:
                print("O valor do saque não pode ser maior que R$ 500.")
            elif qtde_saque == QTDE_LIMITE_SAQUE:
                print("Você já alcançou o limite de saque diário!")
                break
            else:
                qtde_saque += 1
                saldo -= saque
                print("Saque realizado!")
                extrato += f"\n     Saque realizado no valor de R$ {saque: .2f}\n------------------------------------------------------------"
                break
    elif option == 3:
        extrato += f"\n     Saldo atual da conta: R$ {saldo: .2f} \n------------------------------------------------------------" 
        print(extrato)
    elif option == 4:
        print("Obrigado pela preferência!\nSaindo do programa!")
        exit()
    else: 
        print("Escolha uma opção válida!")


