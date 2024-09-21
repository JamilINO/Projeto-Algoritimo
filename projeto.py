preco_base_1=20
preco_base_2=15
preco_base_3=10

while (True):

    print("Filmes disponíveis: Filme 1, Filme 2 e Filme 3")

<<<<<<< HEAD
    t_filme=input("Qual filme deseja assistir? ")

    print("Escolha entre sessão 1 e 2")

    sessao=int(input("Qual a sessão:"))
    while (sessao >= 3) or (sessao < 1):
        
        sessao = int(input("Digite uma sessão válida:" ))

    print("Os tipos de ingresso são: Inteira, Meia e VIP ")

    inteira_1=int(input("Quantas entradas inteiras:" ))
    meia_1=int(input("Quantas entradas meia:" ))
    vip_1=int(input("Quantas entradas vip:" ))

    soma_ava = 0
    inteira=0
    meia=0
    vip=0
    soma_inteira=0
    soma_meia=0
    soma_vip=0
    soma_filme=""

=======
    t_filme=input("Qual filme deseja assistir: ")

    print("Escolha entre sessão 1 e 2")

    sessao=int(input("Qual a sessão: "))

    print("Os tipos de ingresso são: Inteira, Meia e VIP ")

    inteira=int(input("Quantas entradas inteiras: "))
    meia=int(input("Quantas entradas meia: "))
    vip=int(input("Quantas entradas vip: "))

    endloop = input ("Deseja encerrar o atendimento: ")
>>>>>>> da2b94ac963222fc62eca6c5e2de22ef7bb9c0c5
    
    inteira=inteira_1
    meia=meia_1
    vip=vip_1
    
    print("Avalie o filme de 1 a 5 estrelas")
    
    avaliacao = int(input("Qual a avaliação desse filme:" ))

    soma_ava = soma_ava + avaliacao

    if (t_filme.lower() == "filme 1" ):
        

        inteira *= preco_base_1
        


        meia = (meia * preco_base_1) / 2
        

        vip = (vip * preco_base_1) * 1.5
        
            
    elif (t_filme.lower() == "filme 2" ):
        inteira *= preco_base_2 
        meia = (meia * preco_base_2) / 2 
        vip = (vip * preco_base_2) * 1.5
           
            
    elif (t_filme.lower() == "filme 3" ):

        inteira *= preco_base_3
        meia = (meia * preco_base_3) / 2 
        vip = (vip * preco_base_3) * 1.5
<<<<<<< HEAD
        
    endloop = input ("Deseja encerrar o atendimento:" )
             
    
=======

        if (sessao == 1):
            sessao1_f1=True
        elif (sessao == 2):
            sessao2_f1=True 
    else:
        print ("Error")

        print (f"R$ {inteira} - {preco_base_1} porb")
        print (f"R$ {meia}")
        print (f"R$ {vip}")

>>>>>>> da2b94ac963222fc62eca6c5e2de22ef7bb9c0c5
    if (endloop.lower() == "sim"):
        
            print (t_filme," - Sessão", sessao, ":"  )
            print ("Quantidade de ingressos vendidos")
            print (f"-Inteira: {inteira_1:.2f}")
            print (f"-Meia:{meia_1:.2f}")
            print (f"-VIP:{vip_1:.2f}")
            print ("Receita por tipo",sessao)
            print (f"- Inteira: R$ {inteira:.2f}")
            print (f"- Meia: R$ {meia:.2f}")
            print (f"- VIP: R$ {vip:.2f}")
            print ("Média de avaliações:" )
            print ("Filme 1:" )
            print ("Filme 2:" )
            print ("Filme 3:" )
            print ("Total de ingresso vendidos:" )
            print ("Receita total do dia: R$", inteira+meia+vip )
    
            break
                
   
   

