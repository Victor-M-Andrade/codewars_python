while True:
    casos_teste = int(input())

    if casos_teste != 0:
        vencedores = []
        for i in range(casos_teste):

            jogo1 = input().split()
            jogo2 = input().split()
            equipe1_saldo = int(jogo1[0]) + int(jogo2[1])
            equipe2_saldo = int(jogo1[1]) + int(jogo2[0])
            equipe1_fora = int(jogo2[1])
            equipe2_fora = int(jogo1[1])
            if equipe1_saldo > equipe2_saldo:
                vencedores.append('Time 1')
            elif equipe1_saldo < equipe2_saldo:
                vencedores.append('Time 2')
            elif equipe1_saldo == equipe2_saldo:
                if equipe1_fora > equipe2_fora:
                    vencedores.append('Time 1')
                if equipe1_fora < equipe2_fora:
                    vencedores.append('Time 2')
                else:
                    vencedores.append('Penaltis')
    
    else:
        break
    for i in range(len(vencedores)):
        print(vencedores[i])