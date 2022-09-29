from models.calcular import Extrutura


def jogar():
    score = 0

    while True:
        try:
            dificulty = int(input("Escolha um nível de dificuldade:\n"
                                  "1 -> Muito Fácil \n"
                                  "2 -> Fácil \n"
                                  "3 -> Médio \n"
                                  "4 -> Difícil \n"
                                  "-> "))
        except:
            return f'Valor inválido, escolha um valor entre 1, 2, 3 e 4'

        jogador = Extrutura(dificuldade=dificulty)

        print('Digite o resultado da conta a seguir')

        print(jogador.gerar_conta())

        resultado = int(input('-> '))

        if resultado == jogador.gerar_resultado():
            print('Você acertou')
            score += 1
            escolha = str(input((f'Sua pontuação está em {score} pontos, deseja continuar jogando? [Sim, Não]\n'
                                 f'-> ')))
            if escolha.lower() == 'sim':
                print(jogar())

            else:
                print(f'Sua pontuação final foi de {score} pontos')
                print("Até a próxima")
                break
            break
        else:
            print("Resultado incorreto")
            escolha = str(input('Deseja continuar jogando? [Sim, Não]'
                                '-> '))
            if escolha.lower() == 'sim':
                print(jogar())
            else:
                print(f'Sua pontuação final foi de {score} pontos')
                print("Até a próxima")
                break
            break


print(jogar())
