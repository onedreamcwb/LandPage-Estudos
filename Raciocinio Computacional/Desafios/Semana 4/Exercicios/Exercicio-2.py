# 🎯 Objetivo:
#Pedir duas listas de 5 elementos.

#Criar uma terceira lista intercalada: 1º da lista1, 1º da lista2, 2º da lista1, 2º da lista2...

lista1 = []
lista2 = []

for i in range(5):
    valor = input(f"Digite o {i+1}º, elemento da Lista 1: ")
    lista1.append(valor)
    
for i in range(5):
    valor = input(f"Digite o {i+1}º elemento da Lista 2: ")
    lista2.append(valor)
    
lista_intercalada = []

for i in range(5):
    lista_intercalada.append(lista1[i])
    lista_intercalada.append(lista2[i])
    
print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("Lista intercalada:", lista_intercalada)


