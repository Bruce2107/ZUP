def ordenaVetor(vetor):  # ordena o vetor em ordem crescente
    aux = 0
    for i in range(0, len(vetor)):
        for j in range(0, len(vetor)):
            if vetor[i] < vetor[j]:
                aux = vetor[i]
                vetor[i] = vetor[j]
                vetor[j] = aux
    return vetor


def contaNumeros(vetor):
    cont = 1  # O primeiro numero do vetor nao foi repetido ainda
    for i in range(1, len(vetor)):  # começa a loop a partir do segundo valor
        if vetor[i] != vetor[i - 1]:  # compara o valor com seu anterior caso sejão diferentes soma um no contador
            cont += 1
    return cont


vetor = [2, 1, 3, 1]
print(contaNumeros(ordenaVetor(vetor)))
