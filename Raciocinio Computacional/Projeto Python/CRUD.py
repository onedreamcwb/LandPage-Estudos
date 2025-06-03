print('---- MENU PRINCIPAL ----')
while True:
    print('(1) Gerenciar Estudantes.') 
    print('(2) Gerenciar Disciplinas.') 
    print('(3) Gerenciar Professores.') 
    print('(4) Gerenciar Turmas.') 
    print('(5) Gerenciar Matrículas.')
    print('(0) Sair.') 
    try:
        opcao = int(input("\nDigite a Opção Desejada: "))
    except ValueError:
        print("Por favor, digite um número válido!")
        continue  # volta para o início do laço
    if opcao == 0:
        print("\nObrigado por usar nosso programa, volte sempre!")
        break
    elif opcao == 1:
        print("Você escolheu: Gerenciar Estudantes.")
    elif opcao == 2:
        print("Você escolheu: Gerenciar Disciplinas.")
    elif opcao == 3:
        print("Você escolheu: Gerenciar Professores.")
    elif opcao == 4:
        print("Você escolheu: Gerenciar Turmas.")
    elif opcao == 5:
        print("Você escolheu: Gerenciar Matrículas.")
    else:
        print("Opção inválida. Tente novamente.")

