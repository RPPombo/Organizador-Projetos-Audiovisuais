import os

def criar_pastas_ep(caminho_do_ep: str):
    lista_de_pastas = ["Bruto", "Fotos", "Trilha", "Arte", "Projeto_Premier", "Projeto_AE", "Finalizados"]

    for item in lista_de_pastas:
        pasta = caminho_do_ep + "\\" + item
        os.mkdir(pasta)

        print(f"Diretório {item} criado!")

        if item == "Bruto":
            qtd_cam = int(input("Quantidade de câmeras:"))
            for i in range(0, qtd_cam):
                nome_cam = input(f"Qual o nome da câmera {i+1}:")
                os.mkdir(pasta + "\\" + nome_cam)

                qtd_cartao = int(input(f"Quantidade de cartões da câmera {nome_cam}:"))
                for j in range(0, qtd_cartao):
                    os.mkdir(pasta + "\\" + nome_cam + f"\\Cartao_{j}")


print("-------------------------")
print("---Criador de Projetos---")
print("-------------------------")
print("\n")

local_do_projeto = input("Informe o local que deseja criar o projeto (caminho):")

nome_do_projeto = input("Nome do projeto:")

caminho_do_projeto = local_do_projeto + "\\" + nome_do_projeto

os.mkdir(caminho_do_projeto)

qtd_ep = int(input("Quantidade de vídeos/episódios:"))

print("\n")

if qtd_ep > 1:
    for ep in range(0, qtd_ep):
        os.mkdir(caminho_do_projeto + f"\\Episodio_{ep+1}")
        criar_pastas_ep(caminho_do_projeto + f"\\Episodio_{ep+1}")
        print(f"Diretório do episódio {ep+1} criado!\n")
elif qtd_ep == 0 or qtd_ep == 1:
    criar_pastas_ep(caminho_do_projeto)
else:
    print("Entrada inválida!")
    exit(1)
    
print("\n")

info_projeto = {
    "Tipo do projeto" : "",
    "Serviço" : "",
    "Nome do Cliente" : "",
    "Nome do Projeto (Opicional)" : ""
}

with open(caminho_do_projeto + "\\Info_Projeto.txt", "w+", encoding="UTF-8") as arquivo:
    for informacao in info_projeto.keys():
        entrada_txt = input(f"{informacao}:")
        info_projeto[informacao] = entrada_txt

        arquivo.write(f"{informacao}: {info_projeto[informacao]}\n")
