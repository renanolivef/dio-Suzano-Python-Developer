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
extrato_conta = []
opcao = "E"
transacao_dia = 0

def contador_transacao():
    global extrato_conta
    global transacao_dia
    hoje = datetime.now().strftime("%d/%m/%Y")
    aux=0

    for item in extrato_conta:     #@ vai varrer a lista e manter só as datas para leitura e comparação
        data_movimentacao = item.split(" ")[0]  #@ como a data está seguida de um espaço ele está compiando até o primeiro espaço
        if data_movimentacao == hoje:
            aux += 1 #% acho que isso aqui dava para ser simplificado 
    transacao_dia = aux

def deposito(valor_deposito):
    global saldo
    global extrato_conta

    if valor_deposito > 0:
        saldo += valor_deposito
        extrato_conta.append(f"{data_trasacao} - Deposito - R$ {valor_deposito:.2f} ")
        print(f"O valor de R${valor_deposito} foi depositado na conta com sucesso!")
        contador_transacao()
    else:
        print("Valor inválido, tente novamente!")

def saque(valor_saque):
    global saldo
    global extrato_conta

    if valor_saque > 0:
        if valor_saque > 500 and valor_saque < saldo:
            msg = "Valor informado é maior que o valor limite por operação."
                
        elif valor_saque < 500 and valor_saque > saldo:
            msg = "Valor informado é maior que o valor disponível na conta."
                
        else:
            saldo -= valor_saque
            msg = f"O valor de R${valor_saque} foi retirado da conta com sucesso!"
            extrato_conta.append(f"{data_trasacao} -  Saque   - R$ {valor_saque:.2f}")
            contador_transacao()
    else:
        msg = "Valor inválido, tente novamente!"
    return print(msg)

def extrato():
    global extrato_conta

    if not extrato_conta:
        print("Não foram realizadas movimentações na conta." )
    else:
        print("\n---------------------------------------------")
        print("     Extrato da conta bancária:\n")
        print("  Data         Hora       Tipo        Valor")
        for movimentacao in extrato_conta:
            print(movimentacao)
        print(f"\n         Saldo da conta: R$ {saldo:.2f}")
        print("---------------------------------------------")

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

    if opcao == "s" and transacao_dia <10 :
        saque(float(input("Informe o valor que deseja ser sacado:")))
    
    elif opcao == "d" and transacao_dia <10 :
        deposito(float(input("Informe o valor a ser depositado:")))

    elif opcao == "e":
        extrato()

    elif opcao == "x":
        print("Obrigado por usar nosso sistema. Até a proxima!")
        break

    elif transacao_dia >= 10:
        print("Número máximo de transações por dia atingido, por favor tente novamente amanhã. ")

    else: print("Opção inválida! Por favor tente novamente.")