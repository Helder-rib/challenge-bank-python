def format_output(valor):
    print("\n" + "RESULTADO DA OPERACAO".center(70, " "))
    print("-" * 70)
    print(" ==>", valor)
    print("-" * 70)

def sacar(*, saques_feitos, saldo, extrato, valor_limite_saque, qtde_limite_saque):
    saque = 0
    if saques_feitos == qtde_limite_saque:
        format_output("Limite de saque diário atingido") 
        return saldo, extrato, saques_feitos
    print(f"Saldo atual: R$ {saldo:.2f}")
    while saque <= 0:
        saque = float(input("Insira o valor do saque: "))
        if saque < 0:
            format_output("O valor do saque não pode ser negativo!")
    if saque > saldo:
         format_output("O valor do saque é maior que o saldo disponível") 
    elif saque > valor_limite_saque:
        format_output(f"O valor não pode ser maior que o limite de saque: {valor_limite_saque}")
    else:
        saques_feitos += 1
        saldo -= saque
        extrato += f"\n\tSaque: R$ {saque: .2f}\n==================================================="
        format_output("Saque realizado!")
    return saldo, extrato, saques_feitos
    
def depositar(valor, extrato, saldo, /):
    if valor > 0:
        saldo += valor
        extrato += f"\n\tDepósito: R$ {valor: .2f}\n==================================================="
        format_output("Depósito realizado!")
    else:
        format_output("Valor inválido! Tente novamente.")
    return saldo, extrato

def exibir_extrato(extrato,/,*, saldo):
    extrato += f"\n\tSaldo atual: R$ {saldo: .2f} \n===================================================" 
    return extrato

def existe_cpf(lista_clientes):
    while True:
        cpf = input("Digite seu CPF: ")
        if "." not in cpf and "-" not in cpf:
            break
        print("O cpf só deve conter numeros.")
    if lista_clientes:
        for dicionario in lista_clientes:
            if dicionario["CPF"] == cpf:
                return True, dicionario
    return False, cpf

def remove_espacos(list):
    for indice, item in enumerate(list):
        list[indice] = item.strip()
    return list

def criar_usuario(clientes):
    resultado, cpf = existe_cpf(clientes)
    if resultado == False:
        nome = input("Insira seu nome completo: ")
        nascimento = input("Digite a data de nascimento(ex: xx/xx/xxxx): ")
        endereco = input("Digite seu endereço(ex: logradrouro, nro, bairro, cidade, estado): ")
        endereco = endereco.split(",")
        endereco = remove_espacos(endereco)
        endereco = f"{endereco[0]}, {endereco[1]} - {endereco[2]} - {endereco[3]}/{endereco[4]}" 
        clientes.append({"nome": f"{nome}", "nascimento": f"{nascimento}", "CPF": f"{cpf}", "Endereco": f"{endereco}"})
        format_output("Usuário adicionado!")
        return clientes
    else:
        format_output("Esse CPF já está cadastrado.")
        return None

def criar_conta(lista_clientes, contas_existente):
    resultado, usuario = existe_cpf(lista_clientes)
    if resultado != True:
        format_output("O CPF não existe no banco de dados.")
        return None
    else:
        format_output("Conta criada!")
        if bool(contas_existente) == True:
            last_item = len(contas_existente) - 1 
            number = contas_existente[last_item][1] + 1
            contas_existente.append(("0001", number, usuario["nome"]))
        else:
            contas_existente.append(("0001", 1, usuario["nome"]))
        return contas_existente
        2
def menu():
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

    ================================="""
    return print(MENU)

def main():
    VALOR_LIMITE_SAQUE = 500
    QTDE_LIMITE_SAQUE = 3
    saldo = 0.0
    extrato = '''Extrato de hoje: \n'''
    qtde_saque = 0
    lista_clientes = []
    contas_existentes = []

    while True:
        menu()
        option = int(input("===> "))
        if option == 1:
            deposito = 0.0
            while deposito <= 0:
                deposito = float(input("Insira o valor do depósito: "))
                saldo, extrato = depositar(deposito, extrato, saldo)

        elif option == 2:
            while True:
                if saldo == 0.0:
                    format_output("Você não possui saldo disponível na conta.")
                    break
                saldo, extrato, qtde_saque = sacar(saques_feitos=qtde_saque, saldo=saldo, extrato=extrato, valor_limite_saque=VALOR_LIMITE_SAQUE, qtde_limite_saque=QTDE_LIMITE_SAQUE)
                break

        elif option == 3:
            resultado_extrato = exibir_extrato(extrato, saldo=saldo)
            format_output(resultado_extrato)

        elif option == 4:
            resultado_usuario = criar_usuario(lista_clientes)
            if resultado_usuario != None:
                lista_clientes = resultado_usuario

        elif option == 5:
            resultado_criar_conta = criar_conta(lista_clientes=lista_clientes, contas_existente=contas_existentes)
            if resultado_criar_conta != None:
                contas_existentes = resultado_criar_conta

        elif option == 6:
            if not lista_clientes:
                format_output("Não há clientes cadastrados.")
            for numero in range(len(lista_clientes)):
                for chave, valor in lista_clientes[numero].items():
                    print(f"{chave}: {valor}")
                print("=" * 100)   
        
        elif option == 7:
            if not contas_existentes:
                format_output("Não há contas cadastradas.")
            print("CONTAS CADASTRADAS".center(50))
            for tup in contas_existentes:
                print(f"=================================================\nAgência: {tup[0]}\nNúmero: {tup[1]}\nTitular: {tup[2]}")

        elif option == 8:
            format_output("Fechando o sistema.\n\tVolte sempre!")
            exit()
        else: 
            format_output("Escolha uma opção válida!")

main()
