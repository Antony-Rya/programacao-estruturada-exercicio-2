def q1():
    """
    Faça um programa que calcula a
    quantidade de divisores de um
    número (incluindo 1 e o próprio 
    número) que são divisíveis por 3.

    parte 1 = Mostra os divisores

    """
    cont = 0
    numero = int(input())
    for i in range(1, numero + 1):
        if (numero % i == 0) and (numero % 3 == 0):
            cont += 1
    if (cont == 0):
        print("O numero nao possui divisores multiplos de 3")
    else:
        print(f"Quantidade de divisores divisiveis por 3:{cont}")
    

def q2():
    soma = 0
    n1 = int(input())
    n2 = int(input())
    if n1>n2:
        primeiro = n2
        segundo = n1
    else:
        primeiro = n1
        segundo = n2

        
    for i in range(primeiro, segundo + 1):
        if i > 0:
            soma += i
    print(soma)

def q3():
    soma = 0
    cont = 0
    nota = 0
    while True:
        nota = float(input())
        if nota == -1:
            break
        if nota in range(0, 11):
            soma += nota
            cont += 1
        else:
            print("Nota invalida")
            break
    if cont> 0:
        print(soma/cont)

q3()