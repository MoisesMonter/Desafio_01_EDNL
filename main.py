class Tripulante:
    def __init__(self, codigo, nome, idade):
        self.codigo = codigo
        self.nome = nome
        self.idade = idade

class NavioCruzeiro:
    def __init__(self):
        self.tripulacao = {}


TRIP= 250
MAX_NAV = 50
def criar_navio(navios):
    for x in range(1,int(TRIP/MAX_NAV)+1,1):
        if x not in navios:
            navios[x] = NavioCruzeiro()
            # print("Navio", x, "criado com sucesso.")
        else:
            print("O navio", x, "já existe.")

def verify_navio(navios):
    for x in range(1,int(TRIP/MAX_NAV)+1,1):
        navio = navios[x]
        if len(navio.tripulacao) < 50:
            return x
    return None
def adicionar_tripulante(navios,count, nome, idade):
    numero_navio = verify_navio(navios)
    if numero_navio != None:
        navio = navios[numero_navio]
        if len(navio.tripulacao) < 50:
            codigo_tripulante = count  
            tripulante = Tripulante(codigo_tripulante, nome, idade)
            navio.tripulacao[codigo_tripulante] = tripulante
            print("Tripulante", codigo_tripulante, "adicionado ao Navio", numero_navio)
            print("Código:", tripulante.codigo, "Nome:", tripulante.nome, "Idade:", tripulante.idade)
            return count+1
        else:
            print("O Navio", numero_navio, "está lotado. Não é possível adicionar mais tripulantes.")
    else:
        print("O Navio", numero_navio, "não existe.")
    return count

def consultar_tripulante(navios, numero_navio, codigo):
    if numero_navio in navios:
        navio = navios[numero_navio]
        if codigo in navio.tripulacao:
            tripulante = navio.tripulacao[codigo]
            print("Dados do Tripulante", codigo, "no Navio", numero_navio)
            print("Código:", tripulante.codigo, "Nome:", tripulante.nome, "Idade:", tripulante.idade)
        else:
            print("Tripulante com código", codigo, "não encontrado no Navio", numero_navio)
    else:
        print("O Navio", numero_navio, "não existe.")

def main():
    navios = {}  # Dicionário para armazenar os navios-cruzeiros
    count = 0
    criar_navio(navios)
    while True:
        print('''Escolha uma operação:\n1. Adicionar tripulante a um navio\n2. Consultar tripulante em um navio\n3. Sair\n''')

        escolha = input("Digite o número da operação: ")

        if escolha == "1":
            nome = input("Digite o nome do tripulante: ")
            idade = int(input("Digite a idade do tripulante: "))
            count = adicionar_tripulante(navios,count,  nome, idade)
        elif escolha == "2":
            codigo = int(input("Digite o código do tripulante: "))
            consultar_tripulante(navios, 0, codigo)
        elif escolha == "3":
            print("Saindo do programa.")
            break
        else:
            print("Operação inválida. Digite 1, 2, 3 ou 4 para escolher uma operação.")

if __name__ == "__main__":
    main()
