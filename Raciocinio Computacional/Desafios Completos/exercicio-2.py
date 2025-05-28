while True:  # Laço principal para repetir a soma
    while True:  # Laço para validar o primeiro número
        try:
            primeiro_numero = int(input("Escolha um número qualquer\n"))
            break
        except ValueError:
            print("Valor inválido, por favor digite um número inteiro.")

    while True:  # Laço para validar o segundo número
        try:
            segundo_numero = int(input("Agora escolha outro número\n"))
            break
        except ValueError:
            print("Valor inválido, por favor digite um número inteiro.")

    numero_real = primeiro_numero + segundo_numero
    print(f"A soma total é {numero_real}")

    sair = input("Deseja fazer outra soma? (s/n): ")
    if sair.lower() != 's':
        print("Programa finalizado.")
        break

