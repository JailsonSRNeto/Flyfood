def permutacao(lista):
    if len(lista)<=1:
        return [lista]
    lista_auxiliar = []
    for  i, atual in enumerate(lista):
        elementos_restantes = lista[:i] + lista[i+1:]
        for p in permutacao(elementos_restantes):
            lista_auxiliar.append([atual]+p)
    return lista_auxiliar


def lista_de_permutacoes(l):
    todas_permutações = []
    pontos_de_entrega = l
    for p in permutacao(pontos_de_entrega):
        todas_permutações.append(p)
    return todas_permutações


file = open("matriz.txt", 'r')

n, m = file.readline().split()
linhas = file.read().splitlines()

coordenadas = {}
delivery_points = []

for i in range(int(n)):
    linha = linhas[i].split()
    for j in linha:
        if j != '0':
            coordenadas[j] = (i, linha.index(j))
            delivery_points.append(j)


delivery_points.remove('R')
lista_p = lista_de_permutacoes(delivery_points)

menor_custo = float('inf')
for i in range(len(lista_p)):
    custo = 0
    c = 0
    lista_p[i].append('R')
    lista_p[i].insert(0, 'R')
    
    while c < len(lista_p[i])-1:
        custo_y = abs(coordenadas[lista_p[i][c]][0] - coordenadas[lista_p[i][c+1]][0])
        custo_x = abs(coordenadas[lista_p[i][c]][1] - coordenadas[lista_p[i][c+1]][1])
        custo += custo_x + custo_y
        c += 1
    if custo<menor_custo:
        menor_custo = custo
        melhor_rota = lista_p[i]

print(" ".join(melhor_rota[1:-1]))
