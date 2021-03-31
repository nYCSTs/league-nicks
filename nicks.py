import requests
import pathlib

# Leitura .TXT
def leituraNicks():
    try:
        with open(f'{path}/nicks.txt') as file:
            nicks = [nick.rstrip('\n').strip() for nick in file.readlines()]
        return nicks
    except: 
        print('Um arquivo nicks.txt não foi encontrado.')
        try:
            open('nicks.txt', mode='w')
            print('Foi criado um .txt para a adicao de nicks. \n')
        except:
            print('Nao foi possivel criar um nicks.txt. Verifique as configuracoes de permissao da pasta')

# Verifica a disponibilidade
def verificarDisponibilidade(nick):
    url = "https://lols.gg/en/name/checker/br/"
    r = requests.get(url + nick.replace(" ", "%20")) # Caso o nick possua espaco
    html = r.text
    index = html.find("Cleanup date (if inactive):")

    # Caso exista porem nao disponivel
    if (index != -1):
        return html[index + 28:index + 39]
    else:
        return "DISPONIVEL"

path = pathlib.Path().absolute() 
lista_nicks = leituraNicks()
espacamento = " " * 18

# Menu
opt = int(input("\t1) Verificar nicks\n\t2) Verificar um nick especifico\n\t3) Adicionar um novo nick\n>> "))
# Verificar todos nicks
if (opt == 1):
    if (len(lista_nicks) == 0):
        print('Lista vazia. Experimente adicionar mais nicks')
    else:
        for nick in lista_nicks:
            print(f"{nick.strip()}: {espacamento[:18 - len(nick)]}{verificarDisponibilidade(nick)}")
# Verificar nick especifico
elif (opt == 2):
    nick = input("Insira o nick: ")
    print(f"{nick.strip()}: {espacamento[:18 - len(nick)]}{verificarDisponibilidade(nick)}")
# Adicionar novo nick
elif (opt == 3):
    with open(f'{path}/nicks.txt') as file:
        while (nick != "0"):
            nick = input("Nick a ser adicionado (0 para sair): ").strip()
            if (nick != "0"):
                file.write(nick + "\n")
    lista_nicks = leituraNicks()