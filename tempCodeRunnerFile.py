     while True: 
            for i in range(len(clientes)):
                if cpf == clientes[i]['CPF']:
                    print("O cpf já existe no nosso sistema.")
                    cpf = input("Digite seu CPF: ")
                    break
            else:
                break