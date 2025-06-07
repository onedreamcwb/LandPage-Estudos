import matplotlib.pyplot as plt

numeros = [float(input(f"Digite o {i+1}º número: ")) for i in range(6)]

media = sum(numeros) / len(numeros)

acima_ou_igual = [num for num in numeros if num >= media]
abaixo = [num for num in numeros if num < media]

# Mostrar as listas
print("Média:", media)
print("Números iguais ou acima da média:", acima_ou_igual)
print("Números abaixo da média:", abaixo)

# Visualização com gráfico de barras
cores = ['green' if num >= media else 'red' for num in numeros]

plt.bar(range(1, 7), numeros, color=cores)
plt.axhline(y=media, color='blue', linestyle='--', label=f'Média = {media:.2f}')
plt.xticks(range(1, 7))
plt.title("Comparação dos Números com a Média")
plt.xlabel("Posição")
plt.ylabel("Valor")
plt.legend()
plt.show()
