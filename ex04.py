# Entendendo como funciona a ordenação, crescente ou decrescente, de uma lista

lista = [5, 12, 0, 15, 6, 8]
print(lista)
print("")
print("C - Crescente | D - Decrescente")
opt_ordem = input("Você quer ordenar a lista de forma crescente ou decrescente? ")

if opt_ordem == 'C':
    lista.sort(key=int)
    print(lista)
elif opt_ordem == 'D':
    lista.sort(key=int, reverse=True)
    print(lista)
else:
    print("Opção não encontrada!")