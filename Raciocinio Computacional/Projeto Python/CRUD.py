# Nome: Gustavo Luan Leite de Araújo
# Curso: Superior de Tecnologia em Inteligência Artificial Aplicada.

import time

# Lista para armazenar os estudantes
estudantes = []

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
            break
        elif op == 1:
            nome_estudante = input("Digite o nome do estudante: ")
            estudantes.append(nome_estudante)
            print(f"Estudante '{nome_estudante}' incluído com sucesso!")
        elif op == 2:
            if not estudantes:
                print("Não há estudantes cadastrados!")
            else:
                print("\nEstudantes cadastrados:")
                for i, estudante in enumerate(estudantes, 1):
                    print(f"{i}. {estudante}")
        elif op in [3, 4]:
            print("EM DESENVOLVIMENTO")
        else:
            print("Opção inválida. Tente novamente.")

def menu_principal():
    while True:
        print('\n---- MENU PRINCIPAL ----')
        print("(1) Gerenciar Estudantes.")
        print("(2) Gerenciar Disciplinas.")
        print("(3) Gerenciar Professores.")
        print("(4) Gerenciar Turmas.")
        print("(5) Gerenciar Matrículas.")
        print("(0) Sair.")
        try:
            opcao = int(input("\nDigite a Opção Desejada: "))
        except ValueError:
            print("Por favor, digite um número válido!")
            continue
        if opcao == 0:
            print("\nObrigado por usar nosso programa, volte sempre!")
            break
        elif opcao == 1:
            print("Você escolheu: Gerenciar Estudantes.")
            menu_operacoes("Estudantes")
        elif opcao in [2, 3, 4, 5]:
            print("\nFuncionalidade em desenvolvimento. Por favor, escolha outra opção.\n")
            time.sleep(1)
        else:
            print("Opção inválida. Tente novamente.")

# Inicia o sistema
menu_principal()

