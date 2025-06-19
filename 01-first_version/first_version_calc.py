# Menu principal com as operações
# Input para escolha das operações e depois das operações
# Validação de erro
# Memória cachê (para continuar com a operação anterior)

def adicao(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y): # Validação de divisão por 0
    if y == 0:
        return 'Erro: divisão por zero'
    return x / y

def calculadora():
    cache = None

    while True: # Laço infinito 1 == 1, só sai de um while True com um "Break"
        print('''
        CALCULADORA
        ===========
        Selecione a operação desejada:
        1 - Adição
        2 - Subtração
        3 - Multiplicação
        4 - Divisão
        5 - Sair
        ''')

        escolha = input("Digite sua escolha (1/2/3/4/5): ")

        if escolha == "5":
            print("O programa foi encerrado")
            break

        if escolha not in ['1', '2', '3', '4', '5']:
            print("Opção inválida.")
            continue

        if cache is not None:
            es_cache = input(f"Deseja utilizar o resultado '{cache}' para próxima operação? (s/n): ").lower()
        else:
            es_cache = 'n'

        if es_cache == 's':
            n1 = cache
        else:
            try:                
                n1 = float(input("Digite o primeiro número: "))
            except ValueError:
                print("Entrada inválida.")
                continue
        try: 
            n2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Entrada inválida.")
            continue

        # if escolha == "1": 
        #     res = adicao(n1,n2)
        #     op = "+"

        elif escolha == "2":
            res = subtracao(n1,n2)
            op = "-"

        elif escolha == "3":
            res = multiplicacao(n1,n2)
            op = "*"

        elif escolha == "4":
            res = divisao(n1,n2)
            op = "/"

        if isinstance(res, str):
            print(res)
        else:
            print(f"""
                  ***********************************************
                  O resultado da operação: {n1} {op} {n2} = {res}
                  ***********************************************
""")
            cache = res

calculadora()