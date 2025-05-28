# Antes de avançarmos, gostaria que você testasse a lógica acima com alguns exemplos:

#Data de nascimento: 05/06/2000. Data atual: 05/06/2023.
#Data de nascimento: 01/06/2000. Data atual: 05/06/2023.
#Data de nascimento: 25/06/2000. Data atual: 05/06/2023.
#Data de nascimento: 01/01/2000. Data atual: 05/06/2023.
#Data de nascimento: 05/12/2000. Data atual: 05/06/2023.

# entrada de Dados

data_nascimento = input("Digite sua data de Nascimento\n dd/mm/aaaa: " )
#Obtem a data atual
data_atual = input("Digite o dia de hoje\n dd/mm/aaaa: ")

# Separa a data de Nascimento 
dia_nascimento = int(data_nascimento[:2])
mes_nascimento = int(data_nascimento[3:5])
ano_nascimento = int(data_nascimento[6:])

#Separa a data atual em dia, mês ano
dia_atual = int(data_atual[:2])
mes_atual = int(data_atual[3:5])
ano_atual = int(data_atual[6:])

#Calcula a idade em anos
idade = ano_atual - ano_nascimento

# Verifica se já fez aniversário esse ano

if mes_nascimento > mes_atual:
    idade -= 1
elif mes_nascimento == mes_atual and dia_nascimento > dia_atual:
    idade -= 1

#Exibe a idade
print("sua idade é: ", idade, "anos")

