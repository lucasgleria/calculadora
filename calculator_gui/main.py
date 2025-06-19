import tkinter as tk
from view.ui import CalculatorUI
from controller.calculator_controller import CalculatorController

def main():
    root = tk.Tk()
    controller = CalculatorController(None)
    view = CalculatorUI(root, controller)
    controller.view = view
    root.mainloop()

if __name__ == "__main__":
    main()
