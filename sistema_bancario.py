saldo = 0.0
extrato = '''Extrato de hoje: \n'''
qtde_saque = 0
lista_clientes = []
contas_existentes = []

def format_output(valor):
    print("\n" + "RESULTADO DA OPERACAO".center(70, " "))
    print("-" * 70)
    print(" ==>", valor)
    print("-" * 70)

def sacar(*, valor, saques_feitos, saldo, extrato):
    VALOR_LIMITE_SAQUE = 500
    QTDE_LIMITE_SAQUE = 3
    if valor > saldo:
         format_output("O valor do saque é maior que o saldo disponível") 
    elif valor > VALOR_LIMITE_SAQUE:
        format_output(f"O valor não pode ser maior que o limite de saque: {VALOR_LIMITE_SAQUE}")
    elif saques_feitos == QTDE_LIMITE_SAQUE:
        format_output("Limites de saque diário atingido") 
    else:
        saques_feitos += 1
        saldo -= valor
        extrato += f"\n     Saque realizado no valor de R$ {saque: .2f}\n==================================================="
        format_output("Saque realizado!")
    return saldo, extrato, saques_feitos
    
def depositar(valor, extrato, saldo, /):
    if deposito > 0:
        saldo += valor
        extrato += f"\n     Depósito realizado no valor de R$ {deposito: .2f}\n==================================================="
        format_output("Depósito realizado!")
    else:
        format_output("Valor inválido! Tente novamente.")
    return saldo, extrato

def exibir_extrato(extrato,/,*, saldo):
    extrato += f"\n     Saldo atual da conta: R$ {saldo: .2f} \n===================================================" 
    return extrato

def criar_usuario(clientes):
    nome = input("Digite o seu nome: ")
    nascimento = input("Digite a data de nascimento(ex: xx/xx/xxxx): ")
    cpf = "."
    while 1 == 1:
        cpf = input("Digite seu CPF: ")
        if "." not in cpf and "-" not in cpf:
            break
        print("O cpf só deve conter numeros.")
            

    if len(clientes) >= 1:
        while True: 
            for i in range(len(clientes)):
                if cpf == clientes[i]['CPF']:
                    print("O cpf já existe no nosso sistema.")
                    cpf = input("Digite seu CPF: ")
                    break
            else:
                break
    endereco = [input("Digite o seu logradouro: ")]
    endereco.append(input("Digite o numero do seu endereco: "))
    endereco.append(input("Digite o seu bairro: ")) 
    endereco.append(input("Digite a sua cidade: ")) 
    endereco.append(input("Digite o seu estado: "))
    endereco_formatado = f"{endereco[0]}, {endereco[1]} - {endereco[2]} - {endereco[3]}/{endereco[4]}" 
    clientes.append({"nome": f"{nome}", "nascimento": f"{nascimento}", "CPF": f"{cpf}", "Endereco": f"{endereco_formatado}"})
    format_output("Usuário adicionado!")
    return clientes

def criar_conta(lista_clientes, contas_existente, cpf):
    for i in range(len(lista_clientes)):
        if lista_clientes[i]['CPF'] == cpf:
            nome_usuario = lista_clientes[i]['nome']
            break
    else:
        format_output("CPF não encontrado no nosso banco de dados. Faço o cadastro para criar uma conta.")
        return 1
    if bool(contas_existente) == True:
        last_item = len(contas_existente) - 1 
        number = contas_existente[last_item][1] + 1
        contas_existente.append(("0001", number, nome_usuario))

    else:
        contas_existente.append(("0001", 1, nome_usuario))
    return contas_existente
        
        


MENU = """
=================================
-----------MENU------------------

Escolha uma das operações:

    [1] - Depositar
    [2] - Sacar
    [3] - Extrato
    [4] - Criar Usuário
    [5] - Criar Conta
    [6] - Exibir Usuários Cadastrados
    [7] - Exibir Contas Cadastradas
    [8] - Sair

=================================
===> """
while True:
    option = int(input(MENU))
    if option == 1:
        deposito = 0.0
        while deposito <= 0:
            deposito = float(input("Insira o valor do depósito: "))
            resultado_deposito = depositar(deposito, extrato, saldo)
            saldo = resultado_deposito[0]
            extrato = resultado_deposito[1]
            # format_output(resultado_deposito)
    elif option == 2:
        while True:
            if saldo == 0.0:
                print("Você não possui saldo disponível na conta.")
                break
            print("Saldo atual: R$ " , saldo)
            saque = 0
            while saque <= 0:
                saque = float(input("Insira o valor do saque: "))
                if saque < 0:
                    print("O valor do saque não pode ser negativo!")
            resultado_saque = sacar(saques_feitos=qtde_saque, valor=saque, saldo=saldo, extrato=extrato)
            saldo = resultado_saque[0]
            extrato = resultado_saque[1]
            qtde_saque = resultado_saque[2]
            break

    elif option == 3:
        resultado_extrato = exibir_extrato(extrato, saldo=saldo)
        format_output(resultado_extrato)

    elif option == 4:
        resultado_usuario = criar_usuario(lista_clientes)
        lista_clientes = resultado_usuario

    elif option == 5:
        recebe_cpf = input("Insira seu CPF: ")
        resultado_criar_conta = criar_conta(lista_clientes=lista_clientes, contas_existente=contas_existentes, cpf=recebe_cpf)
        if resultado_criar_conta != 1:
            contas_existentes = resultado_criar_conta

    elif option == 6:
        for numero in range(len(lista_clientes)):
            for chave, valor in lista_clientes[numero].items():
                print(f"{chave}: {valor}")
            print("=" * 100)   
       
    elif option == 7:
        for tup in contas_existentes:
            print("Conta: ", *tup)

    elif option == 8:
        print("Obrigado pela preferência!\nSaindo do programa!")
        exit()
    else: 
        print("Escolha uma opção válida!")
