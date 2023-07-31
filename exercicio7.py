nome = input("Digite o seu nome: ")
tamanho_nome = len(nome)
# funçaõ len lê o numero de dígitos de uma variável
if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print ("Seu nome é curto")
    elif tamanho_nome >= 5 and tamanho_nome <= 6:     
        print ("Seu nome é normal")
    else:
        print ("Seu nome é muito grande")    

else:
    print ("Por favor digite mais de um dígito ")    
