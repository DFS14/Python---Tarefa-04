#Programa que solicita para o usuário digitar uma frase e conte quantas vogais e consoantes.

frase = input("Digite uma frase: ")

vogais = sum([1 for char in frase if char.lower() in 'aeiou'])
print("A frase possui", vogais, "vogais. ")

consoates = sum([1 for char in frase if char.lower() in 'b,c,d,f,g,j,j,k,l,m,n,p,q,r,s,t,v,w,x,y,z'])
print("A frase possui", consoates, "consoates. ")

Totaldeletras= vogais + consoates
print ("O total de letras é ", Totaldeletras)