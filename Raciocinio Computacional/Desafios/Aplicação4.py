#Exemplo de aplicação 4: Elabore um programa que solicite ao usuário as notas de determinada disciplina 
#escolar e calcule a média. Se a média for maior ou igual a 7, deve mostrar que o estudante foi aprovado.
#Caso contrário (isto é, se a nota for menor do que 7), mostre uma mensagem ao estudante informando-o que foi reprovado.

# Solicita as notas do usuário

nota1 = float(input("Digite a primeira nota: "))

nota2 = float(input("Digite a segunda nota: "))

nota3 = float(input("Digite a terceira nota: "))

nota4 = float(input("Digite a quarta nota: "))

 

# Calcula a média das notas

media = (nota1 + nota2 + nota3 + nota4) / 4

 

# Verifica se o estudante foi aprovado

if media >= 7:

    print("O estudante foi aprovado.")

    print("Ainda estamos dentro do if.")

else:

    print("O estudante foi reprovado.")

 

 

# Exibe a média

print(f"A média do estudante é: {media:.2f}")