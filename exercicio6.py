entrada = input ("Que horas são?") 
if entrada.isdigit():
    entrada_int = int(entrada)
    if entrada_int >= 0 and entrada_int <= 11:
        print ("Bom dia!")
    elif entrada_int > 12 and entrada_int <= 17:
        print ("Boa tarde!")
    elif entrada_int > 18 and entrada_int <= 23:
        print ("Boa noite")
    else:
        print ("Digite um número válido!")  
           




