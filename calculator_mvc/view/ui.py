def show_menu():
    print("\nSelecione a operação:")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")

def get_user_choice():
    return input("Digite sua escolha (1/2/3/4/5): ")

def ask_use_cache(cache):
    while True:
        choice = input(f"Deseja usar o resultado anterior ({cache}) como o primeiro número? (s/n): ").lower()
        if choice in ['s', 'n']:
            return choice
        else:
            print("Entrada inválida. Por favor, responda apenas com 's' ou 'n'.")

def get_number(prompt):
    try:
        return float(input(prompt))
    except ValueError:
        print("Entrada inválida.")
        return None

def show_result(num1, operation, num2, result):
    print(f"\nResultado: {num1} {operation} {num2} = {result}")

def show_message(msg):
    print(msg)
