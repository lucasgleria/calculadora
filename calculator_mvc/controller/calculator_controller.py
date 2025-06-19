from model import operations
from view import ui

def run_calculator():
    result_cache = None

    while True:
        ui.show_menu()
        choice = ui.get_user_choice()

        if choice == '5':
            ui.show_message("Encerrando a calculadora.")
            break

        if choice not in ['1', '2', '3', '4']:
            ui.show_message("Opção inválida.")
            continue

        if result_cache is not None and ui.ask_use_cache(result_cache) == 's':
            num1 = result_cache
        else:
            num1 = ui.get_number("Digite o primeiro número: ")
            if num1 is None:
                continue

        num2 = ui.get_number("Digite o segundo número: ")
        if num2 is None:
            continue

        if choice == '1':
            result = operations.add(num1, num2)
            op_symbol = '+'
        elif choice == '2':
            result = operations.subtract(num1, num2)
            op_symbol = '-'
        elif choice == '3':
            result = operations.multiply(num1, num2)
            op_symbol = '*'
        elif choice == '4':
            result = operations.divide(num1, num2)
            op_symbol = '/'

        if isinstance(result, str):
            ui.show_message(result)
        else:
            ui.show_result(num1, op_symbol, num2, result)
            result_cache = result
