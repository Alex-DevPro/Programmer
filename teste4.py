
brancos = int(input("total de votos brancos do município: "))
nulos = int(input("total de votos nulos do município: "))
validos = int(input("total de votos válidos do município: "))

Eleitores = brancos + nulos + validos

print("numero de eleitores no município é de: ", Eleitores)

percentualbrancos = brancos / Eleitores * 100
percentualnulos = nulos / Eleitores * 100
percentualvalidos = validos / Eleitores * 100

print("Precentual de votos brancos Foi de: ",percentualbrancos,"\n","Precentual de votos nulos foi de: ",percentualnulos,"\n", "Precentual de votos validos foi de: ",percentualvalidos)