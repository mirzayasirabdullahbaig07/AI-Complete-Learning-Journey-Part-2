import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Tkinter Calculator")
        self.root.geometry("300x400")
        self.root.resizable(False, False)

        self.expression = ""
        self.input_text = tk.StringVar()

        self.create_input_field()
        self.create_buttons()

    def create_input_field(self):
        input_frame = tk.Frame(self.root, height=50, bd=0)
        input_frame.pack(side=tk.TOP)

        input_field = tk.Entry(input_frame, font=('arial', 18),
                               textvariable=self.input_text, justify="right", bd=10)
        input_field.grid(row=0, column=0, ipadx=8, ipady=8)

    def create_buttons(self):
        btns_frame = tk.Frame(self.root)
        btns_frame.pack()

        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['C', '0', '=', '+']
        ]

        for row_index, row in enumerate(buttons):
            for col_index, btn_text in enumerate(row):
                button = tk.Button(
                    btns_frame, text=btn_text, width=8, height=3, font=('arial', 14),
                    command=lambda b=btn_text: self.on_button_click(b)
                )
                button.grid(row=row_index, column=col_index, padx=5, pady=5)

    def on_button_click(self, char):
        if char == 'C':
            self.expression = ""
            self.input_text.set("")
        elif char == '=':
            try:
                result = str(eval(self.expression))
                self.input_text.set(result)
                self.expression = result
            except:
                self.input_text.set("Error")
                self.expression = ""
        else:
            self.expression += str(char)
            self.input_text.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
