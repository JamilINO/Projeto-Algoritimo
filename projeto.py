# Copyright © 2024 João Vitor de Souza Rodello, Marcella Bedine, Thiago Brito Oliveira dos Santos, Mateus Felipe da Silveira Vieira 
#     This file is part of this program.
#     This program is free software: you can redistribute it and/or modify it under the terms of the Affero GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
#     This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the Affero GNU General Public License for more details.
#     You should have received a copy of the Affero GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>. 

# Repositório Git https://github.com/JamilINO/Projeto-Algoritimo.git
preco_base_1 = 20
preco_base_2 = 15
preco_base_3 = 10


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

capacidade = [50, 40, 30]

relatorio = ""

inte1 = 0

mei1 = 0
vp1 = 0

inte2 = 0
mei2 = 0
vp2 = 0

inte3 = 0
mei3 = 0
vp3 = 0

filmes = [
    {
        "sessao": {
            "1": 0,
            "2": 0,
        },  
        "avalicao": []
    },
        {
        "sessao": {
            "1": 0,
            "2": 0,
        },  
        "avalicao": []
    },
        {
        "sessao": {
            "1": 0,
            "2": 0,
        },  
        "avalicao": []
    }


]
    

while (True):

    print("Filmes disponíveis: ")

    for i in range(len(filmes)):
        print(f"\t{i + 1}) Filme {i + 1}")

    t_filme = int(input("\nQual filme deseja assistir? "))

    if t_filme > len(filmes):
        print("opção inválida\n\n")
        continue


    print("Escolha entre uma as sessões disponíveis: ")

    for i in filmes[t_filme - 1]["sessao"].keys():
        print(f"\t-> Sessão {i}: {capacidade[t_filme - 1] - filmes[t_filme - 1]["sessao"][i]} ingressos restantes")
    

    sessao = input("\nQual a sessão: ")
    
    while (sessao not in filmes[t_filme - 1]["sessao"].keys()):
        sessao = input("Digite uma sessão válida: " )

    print("Os tipos de ingresso são: Inteira, Meia e VIP ")

    inteiras = int(input("Quantas entradas inteiras:" ))
    meias = int(input("Quantas entradas meia:" ))
    vips = int(input("Quantas entradas vip:" ))

    soma_inteira=0
    soma_meia=0
    soma_vip=0
    soma_filme=""
    
    inteira=inteiras
    meia=meias
    vip=vips

    if filmes[t_filme - 1]["sessao"][sessao] + (inteiras + meias + vips) > capacidade[t_filme - 1]:
        print("Capacidade acima do limite, Descartando os Ingressos ")
        continue
    else:
        filmes[t_filme - 1]["sessao"][sessao] += (inteiras + meias + vips)

    print(filmes)

    print("Avalie o filme de 0 a 5 estrelas")
    
    avaliacao = int(input("Qual a avaliação desse filme: " ))

    while avaliacao < 0 or avaliacao > 5:
        print(f"{avaliacao} avalicação inválida!\nDigite um número entre 0 e 5 ")
        avaliacao = int(input("Qual a avaliação desse filme: " ))

    filmes[t_filme - 1]["avalicao"].append(avaliacao)

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
            
        print (f"Total de ingresso vendidos: {f1_s1 + f1_s2 + f2_s1 + f2_s2 + f3_s1 + f3_s2}")
        print (f"Receita total do dia: R$ { inte1 + mei1 + vp1 }\n")
    
        break
