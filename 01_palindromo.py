palavra = input("Informe uma palavra ")
palavra = palavra.lower()
invertida = ""
for i in range(0, len(palavra)):  # LOOP PARA VARRER A STRING
    # CONCATENA A ULTIMA POSICAO DA STRING COM A 'INVERTIDA'  PEGANDO O ULTIMO INDICE DA 'PALAVRA'
    invertida += palavra[len(palavra) - 1 - i]

if palavra == invertida:  # COMPARA AS DUAS STRINGS
    print("Palindromo")
else:
    print("Nao é um palindromo")
