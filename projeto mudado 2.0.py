# Copyright © 2024 João Vitor de Souza Rodello, Marcella Bedine, Thiago Brito Oliveira dos Santos, Mateus Felipe da Silveira Vieira 
#     This file is part of this program.
#     This program is free software: you can redistribute it and/or modify it under the terms of the Affero GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
#     This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the Affero GNU General Public License for more details.
#     You should have received a copy of the Affero GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>. 

# Repositório Git https://github.com/JamilINO/Projeto-Algoritimo.git

from datetime import *

soma = 0 

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

poltronas1_1 = []
poltronas1_2 = []
poltronas2_1 = []
poltronas2_2 = []
poltronas3_1 = []
poltronas3_2 = []

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
        "nome": "Alcides no país dos Fluxogramas",
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
        print(f"\t{i + 1}) Filme {filmes[i]['nome']}")

    t_filme = int(input("\nQual filme deseja assistir? "))

    if t_filme > len(filmes):
        print("opção inválida\n\n")
        print_filmes()
    else:
        return t_filme

def verifica_sessao(t_filme: int):
    print("Escolha entre uma as sessões disponíveis: ")

    for i in filmes[t_filme - 1]["sessao"].keys():
        print(f"\t-> Sessão {i}: {filmes[t_filme - 1]['capacidade'] - filmes[t_filme - 1]['sessao'][i]} ingressos restantes")
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
 

def selecionar_poltronas(tfilme, sessao):
       
    entrada = input("Digite os números das poltronas que deseja reservar (1-50), separados por espaço: ")

    poltronas_desejadas_str = entrada.split()

    poltronas_desejadas = poltronas_desejadas_str.copy()

    print (poltronas_desejadas_str) 
    if int(entrada) > 50 or int(entrada) < 1:
        selecionar_poltronas(tfilme,sessao)

    for i in range(len(poltronas_desejadas_str)):
        poltronas_desejadas[i] = 0 
        if poltronas_desejadas_str[i] in poltronas_desejadas:
            print(f"A cadeira {poltronas_desejadas_str[i]} já está reservada, escolha outra: ")
            selecionar_poltronas(tfilme,sessao)
    if tfilme == "1":
        if sessao == "1":
            cadeiras = poltronas1_1 + poltronas_desejadas_str
            for i in range(len(poltronas_desejadas_str)):
                poltronas_desejadas[i] = 0 
                if poltronas_desejadas_str[i] in poltronas_desejadas:
                    print(f"A cadeira {poltronas_desejadas_str[i]} já está reservada, escolha outra: ")
                    selecionar_poltronas(tfilme,sessao)
            poltronas1_1 += poltronas_desejadas_str

                    
        if sessao == "2":
            cadeiras = poltronas1_2 + poltronas_desejadas_str
            for i in range(len(poltronas_desejadas_str)):
                poltronas_desejadas[i] = 0 
                if poltronas_desejadas_str[i] in poltronas_desejadas:
                    print(f"A cadeira {poltronas_desejadas_str[i]} já está reservada, escolha outra: ")
                    selecionar_poltronas(tfilme,sessao)
            poltronas1_2 += poltronas_desejadas_str


    elif tfilme == "2":
        if sessao == "1":
            cadeiras = poltronas2_1 + poltronas_desejadas_str
            for i in range(len(poltronas_desejadas_str)):
                poltronas_desejadas[i] = 0 
                if poltronas_desejadas_str[i] in poltronas_desejadas:
                    print(f"A cadeira {poltronas_desejadas_str[i]} já está reservada, escolha outra: ")
                    selecionar_poltronas(tfilme,sessao)
            poltronas2_1 += poltronas_desejadas_str

        if sessao == "2":
            cadeiras = poltronas2_1 + poltronas_desejadas_str
            for i in range(len(poltronas_desejadas_str)):
                poltronas_desejadas[i] = 0 
                if poltronas_desejadas_str[i] in poltronas_desejadas:
                    print(f"A cadeira {poltronas_desejadas_str[i]} já está reservada, escolha outra: ")
                    selecionar_poltronas(tfilme,sessao)
            poltronas2_2 += poltronas_desejadas_str

    elif tfilme == "3":
        if sessao == "1":
            cadeiras = poltronas3_1 + poltronas_desejadas_str
            for i in range(len(poltronas_desejadas_str)):
                poltronas_desejadas[i] = 0 
                if poltronas_desejadas_str[i] in poltronas_desejadas:
                    print(f"A cadeira {poltronas_desejadas_str[i]} já está reservada, escolha outra: ")
                    selecionar_poltronas(tfilme,sessao)
            poltronas3_1 += poltronas_desejadas_str
        if sessao == "2":
            cadeiras = poltronas3_2 + poltronas_desejadas_str
            for i in range(len(poltronas_desejadas_str)):
                poltronas_desejadas[i] = 0 
                if poltronas_desejadas_str[i] in poltronas_desejadas:
                    print(f"A cadeira {poltronas_desejadas_str[i]} já está reservada, escolha outra: ")
                    selecionar_poltronas(tfilme,sessao)
            poltronas3_2 += poltronas_desejadas_str

def comida():
    print ("Valor pipoca: R$10")

    comida1 = input("Vai querer pipoca (sim/não):")
    if comida1 == "sim":
        quant = int(input("Quantas:"))
        soma = 10 * quant
    else:
        soma = 0 
    return soma 

def get_avalicao(t_filme: int):
    avaliacao = int(input("Qual a avaliação desse filme: " ))

    while avaliacao < 0 or avaliacao > 5:
        print(f"{avaliacao} avalicação inválida!\nDigite um número entre 0 e 5 ")
        avaliacao = int(input("Qual a avaliação desse filme: " ))

    filmes[t_filme - 1]["avalicao"].append(avaliacao)

def exibe_relatorio():
    print(relatorio)
    writer = open(f"Relatorio {datetime.now().strftime('%B_%d_%G')}", "a")
    writer.write(relatorio)
    writer.close()

def main():
    t_filme = print_filmes()

    sessao = verifica_sessao(t_filme)

    inteiras, meias, vips = get_ingressos()

    selecionar_poltronas(t_filme, sessao)
    
    food = comida()
    
    if filmes[t_filme - 1]["sessao"][sessao] + (inteiras + meias + vips) > filmes[t_filme - 1]["capacidade"]:
        print("Capacidade acima do limite, Descartando os Ingressos ")
        return
    else:
        filmes[t_filme - 1]["sessao"][sessao] += (inteiras + meias + vips)


    print("Avalie o filme de 0 a 5 estrelas")
    
    get_avalicao(t_filme)
    

    global inte1, mei1, vp1, relatorio

    inte1 += (inteiras * filmes[t_filme - 1]["preco_inteira"]) 
    mei1 += (meias * filmes[t_filme - 1]["preco_meia"]) 
    vp1 += (vips * filmes[t_filme - 1]["preco_vip"]) 

    
    relatorio += f"""
Filme {t_filme} - Sessão {sessao}: 
Quantidade de ingressos vendidos
-Inteira: {inteiras}
-Meia:{meias}
-VIP:{vips}
    """
    
    relatorio += f"""
Receita por tipo Sessão {sessao}: 
- Receita Inteira: R$ {inte1}
- Receita Meia: R$ {mei1}
- Receita VIP: R$ {vp1}
    """
    

    end_loop = input ("Deseja encerrar o atendimento: ")
    
    if (end_loop.lower() == "sim"):
        
        relatorio += "\nMédia de avaliações:\n"

    for i in range(len(filmes)):
        if len(filmes[i]["avalicao"]) != 0:
            relatorio += f"Filme {i + 1}: {round(sum(filmes[i]['avalicao']) / len(filmes[i]['avalicao']) )}\n"

    total = 0 
    for i in range(len(filmes)):
        for j in filmes[i]["sessao"].values():
            total += j
    relatorio += (f"\nTotal de ingresso vendidos: {total}\n")
    if food >= 10:
         relatorio += (f"Receita total do dia: R$ { inte1 + mei1 + vp1 } + R$10 por pipoca. O valor setá então de R$ {inte1 + mei1 + vp1 + food} \n")
    else: 
        relatorio += (f"Receita total do dia: R$ { inte1 + mei1 + vp1} \n")

    exibe_relatorio()
    if (end_loop.lower() == "sim"):
        exit()   
    
while (True):
    main()


