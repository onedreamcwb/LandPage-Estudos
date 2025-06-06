# Exemplo de aplicação 2: Elabore um programa que solicite ao usuário cinco números e exiba duas listas separadas: uma contendo somente números pares e outra contendo somente números ímpares. 

# Criação de duas listas vazias (Armaz os nºs Pares e impares)
pares = []
impares = []
#Entrada de um laço "for" que vai repetir 5 vezes (0 a 4).
for i in range(5):
# solicitar ao usuario um numero inteiro que será armazenadao em "num" "    
    num =int(input("Digite um Número: "))
# Verif se é Par ou ímpar    
    if num % 2 == 0:
# Se é par, adiciona 1        
        pares.append(num)
# Se Não, adiciona 1 
    else:
        impares.append(num)
print(f"Números pares: {pares}, - Números ímpares:,{impares}")

