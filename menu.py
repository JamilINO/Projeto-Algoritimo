preco = [20, 15, 10]
capacidade = [50, 40, 30]

def avalia ():
    if t_filme.lower() == "filme 1":
        media_f1 += avaliacao
        it_f1 += 1

    elif t_filme.lower() == "filme 2":
        media_f2 += avaliacao
        it_f2 += 1

    elif t_filme.lower() == "filme 3":
        media_f3 += avaliacao
        it_f3 += 1

def total_ingressos():
    soma = f1_s1 + f1_s2 + f2_s1 + f2_s2 + f3_s1 + f3_s2
    print (f"Total de ingresso vendidos: {soma:.2f}") 

def receita_total():
    soma = inte1 + mei1 + vp1
    print (f"Receita total do dia: R$ {soma:.2f}\n")
    
def main():
    avalia()    
    total_ingressos()
    receita_total()

media_f1 = 0
it_f1 = 0
media_f2 = 0
it_f2 = 0
media_f3 = 0
it_f3 = 0

f1_s1 = 0  
f1_s2 = 0 
f2_s1 = 0 
f2_s2 = 0
f3_s1 = 0
f3_s2 = 0 

relatorio = ""

inte1 = 0
mei1 = 0
vp1 = 0

while (True):

    print("Filmes disponíveis: Filme 1, Filme 2 e Filme 3")

    t_filme=input("Qual filme deseja assistir? ")

    print("Escolha entre sessão 1 e 2")

    sessao=int(input("Qual a sessão:"))
    while (sessao >= 3) or (sessao < 1):
        sessao = int(input("Digite uma sessão válida:" ))

    print("Os tipos de ingresso são: Inteira, Meia e VIP ")
    
    if t_filme.lower() == "filme 1":
        print(f"Ingressos Restantes Sessão 1: {capacidade[0] - f1_s1}\nIngressos Restantes Sessão 2: {capacidade[0] - f1_s2}")
    elif t_filme.lower() == "filme 2":
        print(f"Ingressos Restantes Sessão 1: {capacidade[1] - f2_s2}\nIngressos Restantes Sessão 2: {capacidade[1] - f2_s2}")
    if t_filme.lower() == "filme 3":
        print(f"Ingressos Restantes Sessão 1: {capacidade[2] - f3_s2}\nIngressos Restantes Sessão 2: {capacidade[2] - f3_s2}")

    inteira_1=int(input("Quantas entradas inteiras:" ))
    meia_1=int(input("Quantas entradas meia:" ))
    vip_1=int(input("Quantas entradas vip:" ))

    inteira=inteira_1
    meia=meia_1
    vip=vip_1

    if t_filme.lower() == "filme 1":
        if sessao == 1:
            f1_s1 += (inteira_1 + meia_1 + vip_1)
        elif sessao == 2:
            f1_s2 += (inteira_1 + meia_1 + vip_1)

        if f1_s1 > capacidade[0] or f1_s2 > capacidade[0]:
            print("Capacidade acima do limite, Descartando os Ingressos ")
            continue

    if t_filme.lower() == "filme 2":
        if sessao == 1:
            f2_s1 += (inteira_1 + meia_1 + vip_1)
        elif sessao == 2:
            f2_s2 += (inteira_1 + meia_1 + vip_1)

        if f2_s2 > capacidade[0] or f2_s2 > capacidade[0]:
            print("Capacidade acima do limite, Descartando os Ingressos ")
            continue

    if t_filme.lower() == "filme 3":
        if sessao == 1:
            f3_s1 += (inteira_1 + meia_1 + vip_1)
        elif sessao == 2:
            f3_s2 += (inteira_1 + meia_1 + vip_1)

        if f3_s1 > capacidade[0] or f3_s2 > capacidade[0]:
            print("Capacidade acima do limite, Descartando os Ingressos ")
            continue

    print("Avalie o filme de 1 a 5 estrelas")
    
    avaliacao = int(input("Qual a avaliação desse filme:" ))
    
    if (t_filme.lower() == "filme 1" ):

        inteira *= preco[0] 
        meia = (meia * preco[0]) / 2
        vip = (vip * preco[0]) * 1.5 
        
    elif (t_filme.lower() == "filme 2" ):
        
        inteira *= preco[1] 
        meia = (meia * preco[1] ) / 2 
        vip = (vip * preco[1] ) * 1.5
            
    elif (t_filme.lower() == "filme 3" ):

        inteira *= preco[2] 
        meia = (meia * preco[2] ) / 2 
        vip = (vip * preco[2]) * 1.5

    endloop = input ("Deseja encerrar o atendimento:" )

    inte1 += inteira 
    mei1 += meia 
    vp1 += vip   

    relatorio += f"""
{t_filme} - Sessão {sessao}: 
Quantidade de ingressos vendidos
-Inteira: {inteira_1}
-Meia:{meia_1}
-VIP:{vip_1}
Receita por tipo (Sessão {sessao})
- Inteira: R$ {inteira:.2f}
- Meia: R$ {meia:.2f}
- VIP: R$ {vip:.2f}\n
    """

    if (endloop.lower() == "sim"):
        print(relatorio)
        print ("Média de avaliações:\n")

        if it_f1 > 0:
            print (f"Filme 1: {round(media_f1 / it_f1 )}\n" )
            relatorio += f"Filme 1: {round(media_f1 / it_f1 )}"
        if it_f2 > 0:
            print (f"Filme 2: {round(media_f2 / it_f2)}\n" )
            relatorio += f"Filme 2: {round(media_f2 / it_f2)}"
        if it_f3 > 0:
            print (f"Filme 3: {round(media_f3 / it_f3 )}\n" )
            relatorio += f"Filme 3: {round(media_f3 / it_f3 )}"

        break
main()