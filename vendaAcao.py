# A = [23171, 21011, 21123, 21366, 21013, 21367]
# LE VETOR
A = []
valor = 0
while valor >= 0:
    valor = int(input("valor: "))
    if valor >= 0:
        A.append(valor)

# print(A)
maior = 0  # variavel de controle
for i in range(0, len(A)):  # loop do valor da compra
    for j in range(i + 1, len(A)):  # loop do valor da venda
        if i == 0 and j == 1:  # verifica se ainda nao foi definido nenhum valor para maior no caso na primeira passagem
            maior = A[j] - A[i]
        if A[j] - A[i] > maior:  # se a diferença atual for maior que a anterior guarda ela
            maior = A[j] - A[i]
print(maior)
