ano_nasc = int(input("Que ano você nasceu? "))

## Considerando o ano eleitoral de 2024
if ano_nasc <= 2006:
    print("Você pode votar nessa eleição.")
elif ano_nasc > 2006 <= 2008:
    print('Você pode votar, mas seu voto não é obrigatório')
else:
    print("Você não pode votar nessa eleição.")