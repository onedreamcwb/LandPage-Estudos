# Lista para armazenar os estudantes
estudantes = []

def menu_operacoes(nome):
#Primeiro Loop
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
            break
        elif op in [1, 2, 3, 4]:
            print(f"Funcionalidade '{op}' de {nome} ainda não implementada.")
        else:
            print("Opção inválida. Tente novamente.")
# Segundo Loop
print('---- MENU PRINCIPAL ----')
while True:
    print("(1) Gerenciar Estudantes.") 
    print("(2) Gerenciar Disciplinas.") 
    print("(3) Gerenciar Professores.") 
    print("(4) Gerenciar Turmas.'") 
    print("(5) Gerenciar Matrículas.")
    print("(0) Sair.") 
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
    elif opcao in [2, 3, 4, 5]:
        print("Em Desenvolvimento")
        
    

