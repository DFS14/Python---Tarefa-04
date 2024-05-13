#Programa que solicita para usuário digitar um número e verifique se é positivo, negativo ou zero.

numero = float (input('Digite um número: '))

if numero > 0:
    print(f'O valor é positivo.')
elif numero == 0:
    print('O valor zero é neutro.')
else:
    print(f'O valor é negativo.')  