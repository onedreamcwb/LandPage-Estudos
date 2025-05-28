nome_disciplina = input("Digite o nome de sua Disciplina\n")
nota = float(input("Digite suas notas do Primeiro Bimestre\n"))
nota = float(input("Digite suas notas do Segundo Bimestre\n"))
nota = float(input("Digite suas notas do Terceiro Bimestre\n"))
nota = float(input("Digite suas notas do quarto Bimestre\n"))
resultado = nota / 4
if resultado < 6:
    print("Sua média atual foi: {resultado}, fique atento as brechas de conteúdo que podem existir em seu aprendizado!")
elif resultado > 6 and - 9:
    print(f"Sua Média foi {resultado}, você está dentro da média.")
else:
    print("Parabéns!!! Sua média foi {resultado}, você está muito acima da média")    
    
