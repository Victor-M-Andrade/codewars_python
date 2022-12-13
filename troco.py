

while True:
    casos_teste = int(input())

    if casos_teste != 0:
        new_precos = []
        for i in range(casos_teste):
            entradas1 = input().split()
            valor_dinheiro = float(entradas1[0])
            qtd_produtos = int(entradas1[1])
            precos = input().split()
            for j in range(len(precos)):
                new_precos.append(valor_dinheiro - (valor_dinheiro//float(precos[j]))*float(precos[j]))
        troco = sorted(new_precos, key=float, reverse=True)
        print(troco[0])
