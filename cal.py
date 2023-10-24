import tkinter as tk


light_grey = "#F5F5F5"
label_color = "#25265E"
small_font = ("arial", 16)
large_font = ("arial", 40, "bold")
button_font = ("arial", 24, "bold")
white = "#FFFFFF"
default_font = ("arial", 20)
off_white = "#F8FAFF"
light_blue = "#CCEDFF"


class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(0, 0)
        self.window.title("Calculator") 

        self.display_frame = self.create_display_frame()
        self.button_frame = self.create_button_frame()

        self.button_frame.rowconfigure(0, weight=1)
        for x in range(1,5):
            self.button_frame.rowconfigure(x, weight=1)
            self.button_frame.columnconfigure(x, weight=1)


        self.total_expression = ""
        self.digits = {
            7:(1,1), 8:(1,2), 9:(1,3),
            4:(2,1), 5:(2,2), 6:(2,3), 
            1:(3,1), 2:(3,2), 3:(3,3), 
            0:(4,2), ".":(4,1)
        }
        self.operation = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}
        self.current_expression = ""

        self.total_label, self.current_label = self.create_display_label()
        self.create_digit_button()
        self.create_operator_button()
        self.special_button()

       
    def special_button(self):
        self.create_clear_button()
        self.create_equal_button()


    def create_display_label(self):
        total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, bg = label_color, padx=24, font=small_font)
        total_label.pack(expand=True, fill="both")

        current_label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E, bg = label_color, padx=24, font=large_font)
        current_label.pack(expand=True, fill="both")

        return total_label, current_label    

    def create_display_frame(self):
        frame = tk.Frame(self.window, height=221, bg=light_grey)
        frame.pack(expand=True, fill="both")
        return frame
    
    def add_to_expression(self, value):
        self.current_expression += str(value)
        self.update_label()
    
    def create_digit_button(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.button_frame, text=str(digit), anchor=tk.E, bg=white, fg=label_color, font=button_font, borderwidth=0, command=lambda x=digit:self.add_to_expression(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW,)
    
    def update_operator(self, operator):
        self.current_expression += operator
        self.total_expression = self.current_expression
        self.current_expression = ""
        self.update_total_label()
        self.update_label()


    def create_operator_button(self):
        i = 0
        for operator, symbol in self.operation.items():
            button = tk.Button(self.button_frame, text=symbol, bg=off_white, fg=label_color, font=default_font, borderwidth=0, command= lambda x=operator: self.update_operator(x))
            button.grid(row=i, column=4, sticky=tk.NSEW)
            i += 1
    def clear(self):
        self.current_expression = ""
        self.total_expression = ""
        self.update_total_label()
        self.update_label()


    def create_clear_button(self):
        button = tk.Button(self.button_frame, text="C", bg=off_white, fg=label_color, font=default_font, borderwidth=0, command=self.clear)
        button.grid(row=0, column=1, columnspan=3, sticky=tk.NSEW)

    def evaluate(self):
        self.total_expression += self.current_expression
        self.update_total_label()
        self.current_expression = str(eval(self.total_expression))
        self.total_expression = ""
        self.update_label()


    def create_equal_button(self):
        button = tk.Button(self.button_frame, text="=", bg=light_blue, fg=label_color, font=default_font, borderwidth=0, command=self.evaluate)
        button.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW)



    def create_button_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame
    

    def update_total_label(self):
        self.total_label.config(text=self.total_expression)

    def update_label(self):
        self.current_label.config(text=self.current_expression)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    calc = Calculator()
    calc.run()

    