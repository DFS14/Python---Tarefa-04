#Programa que leia o número de maçãs compradas, calcule e escreva o custo total da compra.
quantidade = int(input("Digite a quantidade de maçãs compradas: "))
if quantidade < 12:
    custo = quantidade * 1.30
else:
    custo = quantidade * 1.00
print("O custo total da compra é R$", custo)