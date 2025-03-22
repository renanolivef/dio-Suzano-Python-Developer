#DESCRITIVO DO DESAFIO:
# Fomos contratados por um grande banco para desenvolver o seu novo sistema. Um banco deseja modernizar suas operações, para a primeira versão do sistema devemos implementar apenas 3 operações: depósito, saque e extrato.
#
#- Operação de depósito:
#Deve ser possível depositar valores positivos para a minha conta bancária. A v1 do projeto trabalha apenas com 1 usuário, dessa forma não precisamos nos preocupar em identificar qual é o número da agência e conta bancária. Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.
#
#- Operação de saque:
#O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque. Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.
#
#- Operação de extrato:
#Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta. Se o extrato estiver em branco, exibir a mensagem: Não foram realizadas movimentações.
#Os valores devem ser exibidos utilizando o formato R$ xxx.xx, exemplo: 1500.45 => R$ 1500.45

#--------------------------------------------------------------
saldo = 0
extrato = []
opcao = "S"
contador = 0

while opcao != "x" :
    opcao = input (""" 
********************************
    Bem Vindo ao Banco 24Hrs.
                   
    Tecle:
    S - para realizar saques
    D - para depositar
    E - para visualizar o extrato
    X - para sair
              
********************************
""")
    
    opcao = opcao.lower()

    if opcao == "s":
        if contador < 3:
            valor_saque = int(input("Informe o valor que deseja ser sacado:"))

            if valor_saque > 0:
                if valor_saque > 500 and valor_saque < saldo:
                    print("Valor informado é maior que o valor limite por operação.")
                
                elif valor_saque < 500 and valor_saque > saldo:
                    print("Valor informado é maior que o valor disponível na conta.")
                
                else:
                    saldo -= valor_saque
                    print(f"O valor de R${valor_saque} foi retirado da conta com sucesso!")
                    contador +=1
                    extrato += f"Saque - R$ {valor_saque:.2f}\n "
            else:
                print("Valor inválido, tente novamente!")
        else:
            print("Número máximo de saques por dia atingido, por favor tente novamente amanhã. ")
    
    elif opcao == "d":
        valor_deposito = int(input("Informe o valor a ser depositado:"))

        if valor_deposito > 0:
            saldo += valor_deposito
            print(f"O valor de R${valor_deposito} foi depositado na conta com sucesso!")
            extrato += f"Deposito - R$ {valor_deposito:}\n "
        
        else:
            print("Valor inválido, tente novamente!")

#    elif opcao == "e":  


    elif opcao == "x":
        print("Obrigado por usar nosso sistema. Até a proxima!")
        break

    else: print("Opção inválida! Por favor tente novamente.")
