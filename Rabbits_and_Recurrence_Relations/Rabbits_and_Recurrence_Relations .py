n = int(input("Quantos meses passaram?")) 
k = int(input("Quantos pares de coelho cada coelho terá?"))


geracoes = [1,1, 1 + k, (1 + (k*2))]


i=2
while i<=(n-3): 
    nova_geracao = geracoes[-1] + geracoes[-2]*k
    geracoes.append(nova_geracao)
    i = i + 1

print(geracoes)
