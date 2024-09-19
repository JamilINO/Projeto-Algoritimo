preco_base_1=20
preco_base_2=15
preco_base_3=10

while (True):

    print("Filmes disponíveis: Filme 1, Filme 2 e Filme 3")

    t_filme=input("Qual filme deseja assistir? \n")

    print("Escolha entre sessão 1 e 2")

    sessao=int(input("Qual a sessão:"))

    print("Os tipos de ingresso são: Inteira, Meia e VIP ")

    inteira=int(input("Quantas entradas inteiras:"))
    meia=int(input("Quantas entradas meia:"))
    vip=int(input("Quantas entradas vip:"))

    endloop = input ("Deseja encerrar o atendimento:")
    
    if (t_filme.lower() == "filme 1" ):
        inteira *= preco_base_1 
        meia = (meia * preco_base_1) / 2 
        vip = (vip * preco_base_1) * 1.5
        print (f"R$ {inteira}")
        print (f"R$ {meia}")
        print (f"R$ {vip}")
        if (sessao == 1):
            sessao1_f1=True
        elif (sessao == 2):
            sessao2_f1=True 
    elif (t_filme.lower() == "filme 2" ):
        inteira *= preco_base_2 
        meia = (meia * preco_base_2) / 2 
        vip = (vip * preco_base_2) * 1.5
        print (f"R$ {inteira}")
        print (f"R$ {meia}")
        print (f"R$ {vip}")
        if (sessao == 1):
            sessao1_f1=True
        elif (sessao == 2):
            sessao2_f1=True 
    elif (t_filme.lower() == "filme 3" ):
        inteira *= preco_base_3
        meia = (meia * preco_base_3) / 2 
        vip = (vip * preco_base_3) * 1.5
        print (f"R$ {inteira}")
        print (f"R$ {meia}")
        print (f"R$ {vip}")
        if (sessao == 1):
            sessao1_f1=True
        elif (sessao == 2):
            sessao2_f1=True 
    else:
        print ("Error")
    if (endloop.lower() == "sim"):
        break 


