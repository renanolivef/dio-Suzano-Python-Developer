from datetime import date , datetime, timedelta # @ dessa forma eu importo o módulo data direto

## Chamando data/hora

data = date(2025,9,25)
#print(data)

hoje = date.today() # @ retorna a data no fusu atual da maquina
#print(hoje)

data = datetime.today() # @ retorna a data/hora no fusu atual da maquina, muito usado para registrar transações no sistema
#print(data)

## Realizando operações com datas

#'Ex01:
#tempo_pequeno = 30
#tempo_medio = 45
#tempo_grande = timedelta(minutes=60)  # !podemos chamar diretamente no calculo ou declarar numa var 
#data_atual = datetime.now() # @pega data/hora no momento da chamada (igual o .today)
#
#tipo_carro = input(""" 
#'LAVA JATO - TUDO LIMPO' 
#Informe o tamanho do seu carro (P, M ou G)
#""")
#if tipo_carro == "P":
#    data_estimada = data_atual + timedelta(minutes=tempo_pequeno)  # @time delta é a função que realiza o calculo, devemos informar qual valor do objeto a ser calculado (hora, minuto, segundo )
#    print(f"O carro chegou {data_atual} e ficará pronto às {data_estimada}")
#elif tipo_carro == "M":
#    data_estimada = data_atual + timedelta(minutes=tempo_medio)   # !podemos chamar diretamente no calculo ou declarar numa var 
#    print(f"O carro chegou {data_atual} e ficará pronto às {data_estimada}")
#else:
#    data_estimada = data_atual + tempo_grande
#    print(f"O carro chegou {data_atual} e ficará pronto às {data_estimada}")

#'Ex02:
#resultado = datetime(2025,12,25, 10,8,26)- timedelta(hours=2) #! para realizar calculos de tempo, precisamos declarar uma data qualquer. Caso não tenha uma data a operação vai falhar !
#print(resultado.time()) #@ depois de calcular o tempo, podemos plotar só ele usando .time

#print(datetime.now().date())#@ printa só a data


#'Ex03:
#data_hora_atual = datetime.now()
#data_hora_str = "2025-04-01 20:10"
#mascara_ptbr = "%d/%m/%Y"
#mascara_mentira = "%d/%m"
#mascara_en = "%Y-%m-%d %H:%M"
#
#print(data_hora_atual.strftime(mascara_ptbr)) #@ deixando a string no formato data/hora
#
#dia_mentira = data_hora_atual.strftime(mascara_mentira)
#if dia_mentira == "01/04":
#    print("É Mentiiraaa delaaa !!! ")
#else:
#    print("Nada como um dia normal ! ")
#
#print(datetime.strptime(data_hora_str, mascara_en)) #@muda o objeto para o tipo date/time
#print(type(datetime.strptime(data_hora_str, mascara_en)))

import pytz

data = datetime.now(pytz.timezone("Europe/Oslo"))

print(data)