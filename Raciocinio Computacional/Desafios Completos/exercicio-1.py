while True:
    try:
        pedido = float(input("Digite qualquer Número:\n"))
        resultado = pedido * pedido
        print("Seu número ao quadrado é:", resultado)
    except ValueError:
        print("=====ERROR======")
        continue
    continuar = input("Deseja calcular outro número? (S/N) ")
    if continuar.lower() != 's':
        break



