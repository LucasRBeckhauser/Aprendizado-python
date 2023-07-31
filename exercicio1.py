
nome = input('Digite o seu nome: ')
idade = input('Digite a sua idade: ')
if nome and idade:
    print (f'seu nome é {nome}')
    print (f'seu nome invertido é {nome[::-1]}')
    if ' ' in nome:
        print ('Seu nome contém espaços')
    else:
        print ('Seu nome não contem espaços')    

    print(f'Seu nome tem {len(nome)} letras')
    # len para ler o numero de letras
    print(f' A primeira letra do seu nome é {nome[0]}')
    # para achar a letra, basta ir seguindo a posição em número. Botar dentro de parenteses o numero dai.
else:
    print("Desculpe, você deixou campos vazios.")    

