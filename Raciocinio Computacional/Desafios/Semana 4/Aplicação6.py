# Exemplo de aplicação 6: Solicite ao usuário que digite três coordenadas (x, y), armazenando-as em uma matriz bidimensional.

coordenadas = []
for i in range(3):
    x = int(input("Insira um valor de x: "))
    y = int(input("Insira um valor de y: "))
    coordenadas.append([x, y])
print(coordenadas)

# Linha 1: Começamos criando uma lista vazia chamada coordenadas, que servirá para armazenar as coordenadas fornecidas pelo usuário.
# Linha 2: Em seguida, entramos em um laço "for" que será executado três vezes (de 0 a 2).
# Linhas 3 e 4: Durante cada iteração do laço, pedimos ao usuário para fornecer um valor para x e um valor para y, que representam as coordenadas de um ponto no plano. Esses valores são convertidos em inteiros e armazenados nas variáveis x e y, respectivamente.
#Linha 5: Depois, adicionamos um par de coordenadas, que é uma lista contendo x e y, à lista coordenadas.
# Linha 6: Finalmente, depois que todas as três coordenadas foram coletadas e armazenadas, imprimimos a lista coordenadas.