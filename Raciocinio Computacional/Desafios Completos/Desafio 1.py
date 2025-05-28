#conferir data de nascimento
data_nascimento = input("Digite sua Data de Nascimento (12/12/1990: )")

#obtem a data atual
data_atual = input("Digite o dia de hoje (24/05/2025: )")

# separa a data de nascimento em dia, mês ano
dia_nascimento = int(data_nascimento[:2])
mes_nascimento = int(data_nascimento[3:5])
ano_nascimento = int(data_nascimento[6:])

# Separa a data atual em dia, mês, ano
dia_atual = int(data_atual[:2])
mes_atual = int(data_atual[3:5])
ano_atual = int(data_atual[6:])

# calcula a idade em anos
idade = ano_atual - ano_nascimento

# verifica se já fez aniversário no ano
if mes_nascimento > mes_atual:
    idade -= 1
elif mes_nascimento == mes_atual and dia_nascimento > dia_atual:
    idade -= 1
    
# exibe a idade
print("Sua idade é:", idade, "anos")

if idade >= 60:
    print("você é idoso")
elif idade >= 18:
    print("Você é maior de idade")
else:
    print("Você é menor de idades")


