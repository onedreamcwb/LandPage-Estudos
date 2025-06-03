def menu_operacoes(nome):
    while True:
        print(f"\n--- Menu de Operações: {nome} ---")
        print("(1) Incluir")
        print("(2) Listar")
        print("(3) Atualizar")
        print("(4) Excluir")
        print("(0) Voltar ao menu principal")
        try:
            op = int(input("Escolha uma opção: "))
        except ValueError:
            print("Por favor, digite um número válido!")
            continue
        if op == 0:
            print(f"Voltando ao menu principal de {nome}...")
            break
        elif op == 1:
            print(f"Você escolheu: Incluir em {nome}. (Funcionalidade ainda não implementada.)")
        elif op == 2:
            print(f"Você escolheu: Listar em {nome}. (Funcionalidade ainda não implementada.)")
        elif op == 3:
            print(f"Você escolheu: Atualizar em {nome}. (Funcionalidade ainda não implementada.)")
        elif op == 4:
            print(f"Você escolheu: Excluir em {nome}. (Funcionalidade ainda não implementada.)")
        else:
            print("Opção inválida. Tente novamente.")

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
        menu_operacoes("Estudantes")
    elif opcao == 2:
        print("Você escolheu: Gerenciar Disciplinas.")
        menu_operacoes("Disciplinas")
    elif opcao == 3:
        print("Você escolheu: Gerenciar Professores.")
        menu_operacoes("Professores")
    elif opcao == 4:
        print("Você escolheu: Gerenciar Turmas.")
        menu_operacoes("Turmas")
    elif opcao == 5:
        print("Você escolheu: Gerenciar Matrículas.")
        menu_operacoes("Matrículas")
    else:
        print("Opção inválida. Tente novamente.")

