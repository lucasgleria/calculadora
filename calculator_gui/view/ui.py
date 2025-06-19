import tkinter as tk
from tkinter import messagebox

class CalculatorUI:
    def __init__(self, root, controller):
        self.controller = controller
        self.root = root
        self.root.title("Calculadora MVC")

        self.entry1 = tk.Entry(root, width=20)
        self.entry1.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.entry2 = tk.Entry(root, width=20)
        self.entry2.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.result_label = tk.Label(root, text="Resultado: ")
        self.result_label.grid(row=2, column=0, columnspan=2)

        self.create_buttons()

    def create_buttons(self):
        tk.Button(self.root, text="+", width=5, command=lambda: self.controller.calculate("add")).grid(row=3, column=0)
        tk.Button(self.root, text="-", width=5, command=lambda: self.controller.calculate("subtract")).grid(row=3, column=1)
        tk.Button(self.root, text="×", width=5, command=lambda: self.controller.calculate("multiply")).grid(row=4, column=0)
        tk.Button(self.root, text="÷", width=5, command=lambda: self.controller.calculate("divide")).grid(row=4, column=1)
        tk.Button(self.root, text="Usar resultado", command=self.controller.use_previous_result).grid(row=5, column=0, columnspan=2, pady=10)

    def get_inputs(self):
        return self.entry1.get(), self.entry2.get()

    def set_input1(self, value):
        self.entry1.delete(0, tk.END)
        self.entry1.insert(0, str(value))

    def show_result(self, result):
        self.result_label.config(text=f"Resultado: {result}")

    def show_error(self, message):
        messagebox.showerror("Erro", message)
