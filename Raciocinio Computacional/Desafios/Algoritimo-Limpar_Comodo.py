# Início
#   Mostrar opções: 1 - Cozinha, 2 - Quarto, 3 - Banheiro
#   Pedir para o usuário escolher um cômodo
#
#    Se opção = 1 então
#        Materiais: vassoura, pano, detergente, esponja, saco de lixo
#        Passos: lavar louça, limpar pia, varrer, passar pano, tirar lixo
#   Senão se opção = 2 então
#       Materiais: vassoura, pano, espanador, saco de lixo
#       Passos: arrumar cama, tirar lixo, varrer, passar pano, limpar móveis
#   Senão se opção = 3 então
#       Materiais: desinfetante, escova, pano, balde, saco de lixo
#       Passos: lavar vaso, limpar pia, varrer, passar pano, tirar lixo
#   Fim se
#
#    Guardar materiais de limpeza
# Fim

# Listas de materiais para cada cômodo
materiais_quarto = ["Vassoura", "Pano", "Espanador", "Saco de lixo"]
materiais_cozinha = ["Vassoura", "Pano", "Detergente", "Esponja", "Saco de Lixo"]
materiais_banheiro = ["Desinfetante", "Escova", "Pano", "Balde", "Saco de Lixo"]
comodos_limpos = []

while len(comodos_limpos) < 3:
    # Monta as opções apenas com cômodos ainda não limpos
    opcoes = []
    if "cozinha" not in comodos_limpos:
        opcoes.append("1. Cozinha")
    if "quarto" not in comodos_limpos:
        opcoes.append("2. Quarto")
    if "banheiro" not in comodos_limpos:
        opcoes.append("3. Banheiro")
    print("\nEscolha qual cômodo você quer limpar:")
    print('\n'.join(opcoes))
    escolha = int(input("Digite sua Resposta: "))

    if escolha == 1 and "cozinha" not in comodos_limpos:
        print(f"🛠️  Pegue esses materiais: {', '.join(materiais_cozinha)} e siga os passos a seguir\n")
        print("1. Lave a louça\n2. Limpe a pia\n3. Varra a cozinha\n4. Passe pano no chão\n5. Tire o lixo\n")
        print("Cozinha limpa, parabéns!")
        comodos_limpos.append("cozinha")
    elif escolha == 2 and "quarto" not in comodos_limpos:
        print(f"🛠️  Pegue esses materiais: {', '.join(materiais_quarto)} e siga os passos a seguir\n")
        print("1. Arrume sua cama, afinal como você quer fazer algo se nem sua cama você arruma?\n2. Tire o Lixo\n3. Varra o quarto\n4. Passe Pano de chão\n5. Limpe os Móveis\n")
        print("Depois disso, curta um pouco seu Quarto, Parabéns!!!!!")
        comodos_limpos.append("quarto")
    elif escolha == 3 and "banheiro" not in comodos_limpos:
        print(f"🛠️  Pegue esses materiais: {', '.join(materiais_banheiro)} e siga os passos a seguir\n")
        print("1. Lave o vaso\n2. Limpe a pia\n3. Varra o banheiro\n4. Passe pano\n5. Tire o lixo\n")
        print("Banheiro limpo, parabéns!")
        comodos_limpos.append("banheiro")
    else:
        print("Opção inválida ou cômodo já limpo. Tente novamente.")
        continue

    if len(comodos_limpos) < 3:
        print(f"\nVocê já limpou: {', '.join(comodos_limpos)}.")
        continuar = input("Deseja limpar outro cômodo? (s/n): ")
        if continuar.lower() != 's':
            certeza = input("Tem certeza que não quer limpar os outros cômodos? (s/n): ")
            if certeza.lower() == 's':
                print("Ok! Se mudar de ideia, volte para deixar tudo brilhando! :)")
                break
            else:
                continue

if len(comodos_limpos) == 3:
    print("\nUau! Você limpou todos os cômodos da casa! Agora sim, pode descansar e curtir um ambiente limpinho. Parabéns pelo esforço! 🎉")

