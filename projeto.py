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
        "nome": "Elisangela.py",
        "capacidade": 50,
        "sessao": {
            "1": 0,
            "2": 0,
        },  
        "avalicao": [],

        "preco_base": 20,

        "preco_inteira": 1,
        "preco_meia": 1,
        "preco_vip": 1,
    },
    {
        "nome": "JamilINO",
        "capacidade": 40,
        "sessao": {
            "1": 0,
            "2": 0,
        },  
        "avalicao": [],

        "preco_base": 15,

        "preco_inteira": 1,
        "preco_meia": 1,
        "preco_vip": 1,
    },
    {
        "nome": "Fluxograma: Uma saga Alcides",
        "capacidade": 30,
        "preco_base": 10,
        "sessao": {
            "1": 0,
            "2": 0,
        },  
        "avalicao": [],

        "preco_base": 10,
        
        "preco_inteira": 1,
        "preco_meia": 1,
        "preco_vip": 1,
    }
]




for i in range(len(filmes)):
    print(filmes[i]["preco_base"])
    filmes[i]["preco_inteira"] *= filmes[i]["preco_base"]
    filmes[i]["preco_meia"] = (filmes[i]["preco_meia"] * filmes[i]["preco_base"]) / 2
    filmes[i]["preco_vip"] = (filmes[i]["preco_vip"] * filmes[i]["preco_base"]) * 1.5 


while (True):

    print("Filmes disponíveis: ")

    for i in range(len(filmes)):
        print(f"\t{i + 1}) Filme {filmes[i]["nome"]}")

    t_filme = int(input("\nQual filme deseja assistir? "))

    if t_filme > len(filmes):
        print("opção inválida\n\n")
        continue


    print("Escolha entre uma as sessões disponíveis: ")

    for i in filmes[t_filme - 1]["sessao"].keys():
        print(f"\t-> Sessão {i}: {filmes[t_filme - 1]["capacidade"] - filmes[t_filme - 1]["sessao"][i]} ingressos restantes")
    

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

    if filmes[t_filme - 1]["sessao"][sessao] + (inteiras + meias + vips) > filmes[t_filme - 1]["capacidade"]:
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

    print(filmes)

    inte1 += (inteiras * filmes[t_filme - 1]["preco_inteira"]) 
    mei1 += (meias * filmes[t_filme - 1]["preco_meia"]) 
    vp1 += (vips * filmes[t_filme - 1]["preco_vip"]) 

    
    relatorio += f"""
{t_filme} - Sessão {sessao}: 
Quantidade de ingressos vendidos
-Inteira: {inteiras}
-Meia:{meias}
-VIP:{vips}
Receita por tipo (Sessão {sessao})

    """

    endloop = input ("Deseja encerrar o atendimento:" )
    
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

        total = 0 
        for i in range(len(filmes)):
            for j in filmes[i]["sessao"].values():
                total += j
        
        print (f"Total de ingresso vendidos: {total}")
        print (f"Receita total do dia: R$ { inte1 + mei1 + vp1 }\n")
    
        break
