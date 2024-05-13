# Programa que Calcular a média aritmética simples 

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2

if media >= 6:
    print("O aluno foi aprovado.")
else:
    print("O aluno não foi aprovado.")
print("A média do aluno é", media)