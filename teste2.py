palavra = input("Qual a palavra: ")
qt = 0

for palavras in palavra:
    if palavras in "aeiou":
        qt += 1
        print("Quantidade de vogais: ", palavras)

# print("Quantidade de vogais: ", qt)