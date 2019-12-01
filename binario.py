def converte(num):
    binario = []
    numero = num
    # cria um vetor com o numero binario da direira pra esquerda
    if numero == 1:
        binario.append(1)
    else:
        while True:
            if numero % 2 == 0:  # se o resto da divisao for 0 guarda 0 no vetor senao 1
                binario.append(0)
            else:
                binario.append(1)
            numero //= 2  # pega a parte inteira da divisao
            if numero == 1:  # se o numero chegar a 1 guarda 1 e para o loop
                binario.append(1)
                break
        # inverte o vetor
        invertido = []
        for i in range(0, len(binario)):
            invertido.append(binario[len(binario) - 1 - i])
        binario = invertido
    return binario


def contaEspaco(num):
    espaco = maior = 0
    for i in range(0, len(num)):
        # se o numero atual for igual a 1, o proximo nao estourar a lista e for igua a 0 inicia um loop
        if num[i] == 1 and i + 1 < len(num) and num[i + 1] == 0:
            for j in range(i + 1, len(num)):
                # se o numero atual for igual a 1, o proximo nao estourar a lista adiciona um na contagem
                if num[j] == 0 and j + 1 < len(num):
                    espaco += 1
                else:  # senao verifica se atual é igual a um, pois irá parar a contagem e salvar o maior
                    if num[j] == 1:
                        if espaco > maior:  # verifica se o novo valor é maior que o atual
                            maior = espaco
                    break
            espaco = 0
    return maior


numero = 15
print(contaEspaco(converte(numero)))
