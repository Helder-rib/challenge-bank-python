# Desafio da dio - Sistema bancário em Python
![Status](https://img.shields.io/badge/Status-em%20desenvolvimento-purple)					  ![Language](https://img.shields.io/badge/Language-Python%203-purple)	![Version](https://img.shields.io/badge/version-1.0-purple)

Este é um projeto que consiste em um sistema bancário simples com as operações de depósito, saque e extrato.
## Descrição
### Sobre o projeto
O intuito desse projeto é a criação de um sistema bancário que possua algumas funcionalidades específicas: Depositar, Sacar e visualizar o Extrato. O sistema possibilita que o usuário escolha qualquer uma das operações e realize a interação com elas. Esse sistema possui o saldo que é aumentado de acordo com as operações de depósito do usuário e é subtraído mediante as operações de saque.

### Funcionalidade das operações
O sistema bancário possui três tipos de operações:
- **Depósito** - O usuário escolhe o valor do depósito que irá ser adicionado a conta e então incrementado ao saldo atual. Não é aceito valores negativos.
- **Saque** - O usuário escolhe o valor de saque que será subtraído do saldo da conta. O valor de saque não pode ser maior que o saldo atual e também não pode exceder R$ 500 por operação. Há um limite três operações de saque, logo o sistema não aceitará mais que três operações.
- **Extrato** - Quando o usuário seleciona essa opção, é mostrado na tela todas as operações realizadas juntamente com o valor de cada uma e ao final aparece o saldo atual da conta.

### Rodando o sistema
Logo após rodar o programa é exibido um menu com quatro opções possíveis: 

![menu_sistema_bancario](https://github.com/Helder-rib/challenge-bank-python/assets/124646211/957f165a-ccc7-4958-be37-df54603fbbcf)

Caso escolha a opção de depósito **(1)** o sistema espera um valor para ser depósitado na conta. Se o valor for válido a operação é realizada e o valor é acrescido ao saldo da conta, caso contrário o sistema insiste até receber um valor válido.

Se a opção de saque **(2)** for escolhida o sistema espera um valor para ser sacado da conta. Se o valor for válido a operação é realizada e o valor é deduzido do saldo, caso contrário se o valor for inválido o sistema insiste até receber um valor válido. Caso o usuário já tenha realizado três operações de saque, o sistema retorna ao menu novamente.

Por outro lado, se a opção de extrato **(3)** for selecionada o sistema irá apresentar na tela o registro de todas as operações realizadas durante a sessão mostrando o tipo da operação e o valor dela em R$, no fim do extrato irá aparecer o saldo atual da conta.

Por fim, caso o usuário queira sair do sistema, basta digitar a opção sair **(4)** que então irá aparecer uma mensagem e o programa será encerrado.



## Como usar
1. Certifique-se de ter o Python instalado na sua máquina.
2. Clone este repositório para a sua máquina ou então faça download dos arquivos.
3. Use um editor de códigos que tenha suporte a python e abra a pasta que contém o arquivo do sistema bancário .py.
3. Execute o programa na sua máquina.

Desenvolvido por [Hélder Ribeiro](https://github.com/helder-rib)

