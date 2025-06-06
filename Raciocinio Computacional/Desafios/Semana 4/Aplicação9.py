# Exemplo de aplicação 9: Em uma competição de saltos ornamentais, são obtidas dos jurados sete notas, sendo eliminadas a maior e a menor. A nota final do salto é feita pela soma das demais notas. Crie um programa que receba as notas dos juízes, remova a maior e menor nota e some as demais, fazendo uso de métodos de listas e funções built in.

notas = []
for _ in range(7):
    nota = float(input("Entre com uma das notas: "))
    notas.append(nota)
menor = min(notas)
if notas.count(menor) == 1:
    notas.remove(menor)
else:
    indice = -1
    for i in range(len(notas)):
        if notas[i] == menor:
            indice = i
            break
    notas.pop(indice)
maior = max(notas)
if notas.count(maior) == 1:
    notas.remove(maior)
else:
    indice = -1
    for i in range(len(notas)):
        if notas[i] == maior:
            indice = i
            break
    notas.pop(indice)
soma = sum(notas)
print(f"A pontuação final do salto foi {soma:.1f}")

#Linha 1: Primeiro, criamos uma lista vazia chamada notas.
#Linhas 2, 3 e 4: Depois, entramos em um laço "for" que pede ao usuário para inserir sete notas, uma de cada vez. Cada nota é adicionada à lista notas.
#Linha 5: Em seguida, encontramos a nota mais baixa (menor) usando a função min(notas).
#Linha 6: Se a nota mais baixa aparece apenas uma vez na lista:
#Linha 7: A removemos com notas.remove(menor).
#3Linhas 8 a 14: Caso contrário, encontramos a primeira ocorrência da nota mais baixa e a removemos usando o método pop().
#Linhas 15 a 24: Repetimos um processo semelhante para remover a nota mais alta (maior). Usamos max(notas) para encontrar a nota mais alta e a removemos da lista.
#Linhas 25 e 26: Finalmente, somamos todas as notas restantes com sum(notas), e imprimimos a pontuação final do salto.