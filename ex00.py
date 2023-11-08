def calculo():

    v1 = input("Insira o primeiro valor: ")
    v2 = input("Insira o segundo valor: ")

    if v1 > v2:
        print("{} é maior que {}".format(v1, v2))
    else:
        print("{} é menor que {}".format(v1, v2))
    
    
def repeat():
    repeat = input("Deseja repetir? 1 - Sim | 2 - Não: ")
    if repeat == '1':
        calculo()
    else:
        print("Até a próxima!")
        
        
calculo()
repeat()