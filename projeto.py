# Copyright © 2024 João Vitor de Souza Rodello, Marcella Bedine, Thiago Brito Oliveira dos Santos, Mateus Felipe da Silveira Vieira 
#     This file is part of this program.
#     This program is free software: you can redistribute it and/or modify it under the terms of the Affero GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
#     This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the Affero GNU General Public License for more details.
#     You should have received a copy of the Affero GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>. 

# Repositório Git https://github.com/JamilINO/Projeto-Algoritimo.git

from datetime import *


media_f1 = 0
it_f1 = 0
media_f2 = 0
it_f2 = 0
media_f3 = 0
it_f3 = 0

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
    filmes[i]["preco_inteira"] *= filmes[i]["preco_base"]
    filmes[i]["preco_meia"] = (filmes[i]["preco_meia"] * filmes[i]["preco_base"]) / 2
    filmes[i]["preco_vip"] = (filmes[i]["preco_vip"] * filmes[i]["preco_base"]) * 1.5 


def print_filmes():
    print("Filmes disponíveis: ")

    for i in range(len(filmes)):
        print(f"\t{i + 1}) Filme {filmes[i]["nome"]}")

    t_filme = int(input("\nQual filme deseja assistir? "))

    if t_filme > len(filmes):
        print("opção inválida\n\n")
        print_filmes()
    else:
        return t_filme

def verifica_sessao(t_filme: int):
    print("Escolha entre uma as sessões disponíveis: ")

    for i in filmes[t_filme - 1]["sessao"].keys():
        print(f"\t-> Sessão {i}: {filmes[t_filme - 1]["capacidade"] - filmes[t_filme - 1]["sessao"][i]} ingressos restantes")
    sessao = input("\nQual a sessão: ")

    while (sessao not in filmes[t_filme - 1]["sessao"].keys()):
        sessao = input("Digite uma sessão válida: " )

    return sessao
    
def get_ingressos():
    print("Os tipos de ingresso são: Inteira, Meia e VIP ")

    inteiras = int(input("Quantas entradas inteiras:" ))
    meias = int(input("Quantas entradas meia:" ))
    vips = int(input("Quantas entradas vip:" ))

    return (inteiras, meias, vips)

def exibe_relatorio():
    print(relatorio)
    writer = open(f"Relatorio {datetime.now().strftime("%B_%d_%G")}", "a")
    writer.write(relatorio)
    writer.close()


def main():
    t_filme = print_filmes()

    sessao = verifica_sessao(t_filme)

    inteiras, meias, vips = get_ingressos()

    if filmes[t_filme - 1]["sessao"][sessao] + (inteiras + meias + vips) > filmes[t_filme - 1]["capacidade"]:
        print("Capacidade acima do limite, Descartando os Ingressos ")
        return
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

    global inte1, mei1, vp1, relatorio

<<<<<<< HEAD
        inteira *= preco_base_1 
        meia = (meia * preco_base_1) / 2
        vip = (vip * preco_base_1) * 1.5 
        
    elif (t_filme.lower() == "filme 2" ):
        
        inteira *= preco_base_2 
        meia = (meia * preco_base_2) / 2 
        vip = (vip * preco_base_2) * 1.5
            
    elif (t_filme.lower() == "filme 3" ):

        inteira *= preco_ base_3
        meia = (meia * preco_base_3) / 2 
        vip = (vip * preco_base_3) * 1.5
        
    endloop = input ("Deseja encerrar o atendimento:" )

    inte1 += inteira 
    mei1 += meia 
    vp1 += vip   
=======
    inte1 += (inteiras * filmes[t_filme - 1]["preco_inteira"]) 
    mei1 += (meias * filmes[t_filme - 1]["preco_meia"]) 
    vp1 += (vips * filmes[t_filme - 1]["preco_vip"]) 
>>>>>>> 58b32c085a822eecd3abc8e73148686d6bba9d8e

    
    relatorio += f"""
Filme {t_filme} - Sessão {sessao}: 
Quantidade de ingressos vendidos
-Inteira: {inteiras}
-Meia:{meias}
-VIP:{vips}
Receita por tipo (Sessão {sessao})

    """

    end_loop = input ("Deseja encerrar o atendimento:" )
    
    if (end_loop.lower() == "sim"):
        relatorio += "\nMédia de avaliações:\n"

        for i in range(len(filmes)):
            if len(filmes[i]["avalicao"]) != 0:
                relatorio += f"Filme {i + 1}: {round(sum(filmes[i]["avalicao"]) / len(filmes[i]["avalicao"]) )}\n"

        total = 0 
        for i in range(len(filmes)):
            for j in filmes[i]["sessao"].values():
                total += j

        print (f"Total de ingresso vendidos: {total}")
        print (f"Receita total do dia: R$ { inte1 + mei1 + vp1 }\n")

        exibe_relatorio()
        exit()

while (True):
    main();



