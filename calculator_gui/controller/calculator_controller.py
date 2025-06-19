from model import operations

class CalculatorController:
    def __init__(self, view):
        self.view = view
        self.previous_result = None

    def calculate(self, operation):
        val1, val2 = self.view.get_inputs()

        try:
            num1 = float(val1)
            num2 = float(val2)
        except ValueError:
            self.view.show_error("Por favor, insira números válidos.")
            return

        if operation == "add":
            result = operations.add(num1, num2)
        elif operation == "subtract":
            result = operations.subtract(num1, num2)
        elif operation == "multiply":
            result = operations.multiply(num1, num2)
        elif operation == "divide":
            result = operations.divide(num1, num2)
            if isinstance(result, str):
                self.view.show_error(result)
                return

        self.previous_result = result
        self.view.show_result(result)

    def use_previous_result(self):
        if self.previous_result is not None:
            self.view.set_input1(self.previous_result)
        else:
            self.view.show_error("Nenhum resultado anterior disponível.")
