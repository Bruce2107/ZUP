def ordenaVetor(vetor):  # ordena o vetor em ordem crescente
    aux = 0
    for i in range(0, len(vetor)):
        for j in range(0, len(vetor)):
            if vetor[i] < vetor[j]:
                aux = vetor[i]
                vetor[i] = vetor[j]
                vetor[j] = aux
    return vetor


def validaPermutacao(vetor):  # verifica se nao há valores repetidos no vetor e se nao possui saltos na sequencia
    for i in range(0, len(vetor)):
        if vetor[i] != i + 1:
            # se a posição do vetor for diferente da posicao do loop + 1(o menor numero sempre é um) retorna false
            return False
    return True


vetor = [2, 1, 3]
vetor = ordenaVetor(vetor)
if validaPermutacao(vetor):
    print(1)
else:
    print(0)
