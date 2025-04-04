#Desafio: Data e hora
#
#Você foi encarregado de implementar as seguintes funcionalidades no sistema da empresa bancária:
#
#-Estabelecer um limite de 10 transações diárias para uma conta
#-Se o usuário tentar fazer uma transação após atingir o limite, deve ser informado que ele excedeu o número de transações permitidas para aquele dia.
#-Mostre no extrato, a data e hora de todas as transações.
#
#---------------------------------------------------------------------------------------------------
from datetime import datetime

saldo = 0
extrato = ""
opcao = "E"
contador_saque = 0
transasao_dia = 0


def deposito(valor_deposito):
    global saldo
    global extrato

    if valor_deposito > 0:
        saldo += valor_deposito
        extrato += f"Deposito - R$ {valor_deposito:.2f} em {data_trasacao}\n "
        print(f"O valor de R${valor_deposito} foi depositado na conta com sucesso!")
    else:
        print("Valor inválido, tente novamente!")

def saque(valor_saque):
    global saldo
    global extrato
    global contador_saque

    if valor_saque > 0:
        if valor_saque > 500 and valor_saque < saldo:
            msg = "Valor informado é maior que o valor limite por operação."
                
        elif valor_saque < 500 and valor_saque > saldo:
            msg = "Valor informado é maior que o valor disponível na conta."
                
        else:
            saldo -= valor_saque
            msg = f"O valor de R${valor_saque} foi retirado da conta com sucesso!"
            contador_saque +=1
            extrato += f"Saque - R$ {valor_saque:.2f} em {data_trasacao}\n "
    else:
        msg = "Valor inválido, tente novamente!"
    return print(msg)

#Vai precisar transformar esse extrato em um novo objeto, talvez lista 
def estrato():
        print("\n ===================================")
        print("Extrato da conta bancária:")
        print("Não foram realizadas movimentações na conta." if not extrato else extrato) #@ Esse if serve para verificar se extrato está vazio (se tiver mostra a frase se não mostra extrato )
        print(f"\nSaldo da conta: R$ {saldo:.2f}")
        print("===================================\n")

#def contador_transacao():


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
    data_trasacao = datetime.now().strftime("%d/%m/%Y - %H:%M:%S")

    if opcao == "s" and transasao_dia < 10:
        if contador_saque < 3:
            saque(float(input("Informe o valor que deseja ser sacado:")))
        else:
            print("Número máximo de saques por dia atingido, por favor tente novamente amanhã. ")
    
    elif opcao == "d" and transasao_dia < 10:
        deposito(float(input("Informe o valor a ser depositado:")))

    elif opcao == "e":
        estrato()

    elif opcao == "x":
        print("Obrigado por usar nosso sistema. Até a proxima!")
        break

    else: print("Opção inválida! Por favor tente novamente.")