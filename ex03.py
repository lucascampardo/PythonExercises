# Preço caso seja menos de uma dúzia -> R$1,25
# Preço caso seja pelo menos 1 dúzia -> R$0,55

apple = int(input('Quantas maças você gostaria de comprar? '))

if apple < 12:
    print("O valor total é {:.2f}".format(apple * 1.25)) # {:.2f} é utilizado para limitar casas decimais
elif apple >= 12:
    print("O valor total é {:.2f}".format(apple * 0.55))