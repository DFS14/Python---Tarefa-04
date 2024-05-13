
#Programa que receba um número inteiro e retorne se é primo ou não.

numero = int(input('Digite um número: '))

if numero > 1 and all(numero % i != 0 for i in range(2, numero)):
    print("O número é primo.")
else:
    print('O número não é primo. ')