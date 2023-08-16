# Desafio da dio - Sistema bancário em Python
![Status](https://img.shields.io/badge/Status-em%20desenvolvimento-purple)					  ![Language](https://img.shields.io/badge/Language-Python%203-purple)	![Version](https://img.shields.io/badge/Version-2.0-purple)  [![License: MIT](https://img.shields.io/badge/License-MIT-purple.svg)](https://opensource.org/licenses/MIT)
	![Release](https://img.shields.io/badge/Latest_Release-08/23-purple)


Este é um projeto que consiste em um sistema bancário simples com as operações de depósito, saque e extrato. É possível também criar usuário e conta.
## Descrição
### Sobre o projeto
#### Versão 1
O intuito desse projeto é a criação de um sistema bancário que possua algumas funcionalidades específicas: Depositar, Sacar e visualizar o Extrato. O sistema possibilita que o usuário escolha qualquer uma das operações e realize a interação com elas. Esse sistema possui o saldo que é aumentado de acordo com as operações de depósito do usuário e é subtraído mediante as operações de saque.
##### Versão 2
Possui tudo que há na versão anterior com a adição de novas funcionalidades como a possibilidade de criação de usuário, criação de conta e exibição tanto de usuário como também de conta. Outras modificações foram a implementação das operações através de funções, tornando o código mais modularizado, com melhor legibilidade e fácil manutenabilidade.
### Funcionalidade das operações
O sistema bancário possui 7 tipos de operações:
- **Depósito** - O usuário escolhe o valor do depósito que irá ser adicionado a conta e então incrementado ao saldo atual. Não é aceito valores negativos.
- **Saque** - O usuário escolhe o valor de saque que será subtraído do saldo da conta. O valor de saque não pode ser maior que o saldo atual e também não pode exceder R$ 500 por operação. Há um limite três operações de saque, logo o sistema não aceitará mais que três operações.
- **Extrato** - Quando o usuário seleciona essa opção, é mostrado na tela todas as operações realizadas juntamente com o valor de cada uma e ao final aparece o saldo atual da conta.

**_Adicionadas na Versão 2:_**

- **Criar Usuário** - O usuário escolhe essa opção e em seguida ele preenche as informações que são solicitadas, após preencher as informações ele é cadastrado. 
- **Criar Conta** - Quando escolhida essa opção, o usuário informa o CPF e só caso este CPF exista no sistema é que ele poderá criar uma conta. Caso o sistema não encontre o CPF, é preciso que o usuário crie sua conta primeiro.
- **Exibir Usuários Cadastrados** - Essa opção exibe as informações de todos os usuários cadastrados.
- **Exibir Contas Cadastradas** - Após selecionada, exibe todas as contas criadas.


### Rodando o sistema
Logo após rodar o programa é exibido um menu com oito **(8)** opções possíveis: 

 ![menu_bank_system](https://github.com/Helder-rib/challenge-bank-python/assets/124646211/380a036c-a1cf-4b28-a41c-bb3121180eb5)

Caso escolha a opção de depósito **(1)** o sistema espera um valor para ser depósitado na conta. Se o valor for válido a operação é realizada e o valor é acrescido ao saldo da conta, caso contrário o sistema insiste até receber um valor válido.

Se a opção de saque **(2)** for escolhida o sistema espera um valor para ser sacado da conta. Se o valor for válido a operação é realizada e o valor é deduzido do saldo, caso contrário se o valor for inválido o sistema insiste até receber um valor válido. Caso o usuário já tenha realizado três operações de saque, o sistema retorna ao menu novamente.

Por outro lado, se a opção de extrato **(3)** for selecionada o sistema irá apresentar na tela o registro de todas as operações realizadas durante a sessão mostrando o tipo da operação e o valor dela em R$, no fim do extrato irá aparecer o saldo atual da conta.

Na operação **(4)**, é possível criar uma conta e para isso será pedidas informações, entre elas: Nome, Data de nascimento, CPF e Endereço. O CPF não pode conter traços **"-"** ou pontos **"."** e caso seja digitado um CPF já existente, será pedido que informe o CPF novamente.

Na opção **(5)** há a possibilidade de criar uma conta, mas para isso é preciso informar o CPF e se este estiver cadastrado no sistema através da opção **Criar Usuário** é criada a conta com êxito, caso contrário é preciso cadastrar o usuário antes. 

Quando selecionada a opção **(6)** é exibido na tela a lista com todos os usuários cadastrados no sistema.

Já na opção **(7)** temos a possibilidade de exibir todas as contas cadastradas até o momento.

E enfim, na opção **(8)** temos a operação que encerra o programa se for selecionada.

## Regras de negócio implementadas no programa
- O valor de depósito não pode ser negativo.
- O saque só será realizado caso o saldo seja menor que o saldo.
- Há um limite de saque por operação que é R$ 500, se esse limite for ultrapassado, o saque é negado.
- Há um limite de saque diário de 3 saques, alcançado esse limite, as operações de saque posteriores são negadas.
- O valor do saque precisa ser maior que **> 0**  e não pode ser negativo.
- Na criação de usuário, não são aceitos caracteres de ponto ou traço no CPF, caso seja encontrado, é pedido que digite novamente.
- Não é possível cadastrar mais de um usuário com um mesmo CPF.
- Só é permitido criar uma conta caso haja o cadastro no sistema previamente.

## Como usar
1. Certifique-se de ter o Python instalado na sua máquina.
	- Para checar se o Python esta instalado na sua máquina, você pode abrir o prompt no windows digitando "cmd" no menu de pesquisa e apertanto enter e depois digitando o seguinte na janela que irá abrir: `python --version`. Caso apareça a versão do pyhton, quer dizer que ele estaá instalado. Caso contrário, basta ir no site de download [clicando aqui](https://www.python.org/downloads/).
	
2. Clone este repositório para a sua máquina ou então faça download dos arquivos necessários.
	- Para clonar este repositótio você pode abrir o GitBash e digitar na linha de comando o seguinte código `git clone https://github.com/Helder-rib/challenge-bank-python.git`.
3. Use um editor de códigos que tenha suporte a python e abra a pasta que contém o arquivo do sistema bancário .py.
3. Execute o programa na sua máquina.

Desenvolvido por [Hélder Ribeiro](https://github.com/helder-rib)

