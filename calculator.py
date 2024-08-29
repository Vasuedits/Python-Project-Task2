import tkinter as tk
import math

class SC_Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Scientific Calculator')
        self.configure(bg='#0000FF')
        self.resizable(width=False, height=False)
        
        self.current = ''
        self.inp_value = True
        self.result = False
        
        self._create_widgets()

    def _create_widgets(self):
        self.ent_field = tk.Entry(self, bg='#ADD8E6', fg='#000080', font=('Arial', 25), borderwidth=10, justify="right")
        self.ent_field.grid(row=0, column=0, columnspan=8, padx=10, pady=10, sticky='nsew')
        self.ent_field.insert(0, '0')
        
        buttons = [
            ('CE', self.Clear_Entry, 1, 0, 2),
            ('\u221A', self.SQ_Root, 1, 2),
            ('+', lambda: self.Standard_Ops('+'), 1, 3),
            ('\u03C0', self.Pi, 1, 4),
            ('e', self.E, 1, 5),
            ('Deg', self.Deg, 1, 6),
            ('x\u00B2', self.Pow_2, 1, 7),
            ('7', lambda: self.Enter_Num(7), 2, 0),
            ('8', lambda: self.Enter_Num(8), 2, 1),
            ('9', lambda: self.Enter_Num(9), 2, 2),
            ('-', lambda: self.Standard_Ops('-'), 2, 3),
            ('Exp', self.Exp, 2, 4),
            ('x!', self.Fact, 2, 5),
            ('Rad', self.Rad, 2, 6),
            ('x\u00B3', self.Pow_3, 2, 7),
            ('4', lambda: self.Enter_Num(4), 3, 0),
            ('5', lambda: self.Enter_Num(5), 3, 1),
            ('6', lambda: self.Enter_Num(6), 3, 2),
            ('*', lambda: self.Standard_Ops('*'), 3, 3),
            ('sin', self.Sin, 3, 4),
            ('cos', self.Cos, 3, 5),
            ('tan', self.Tan, 3, 6),
            ('10\u207F', self.Pow_10_n, 3, 7),
            ('1', lambda: self.Enter_Num(1), 4, 0),
            ('2', lambda: self.Enter_Num(2), 4, 1),
            ('3', lambda: self.Enter_Num(3), 4, 2),
            ('/', lambda: self.Standard_Ops('/'), 4, 3),
            ('sinh', self.Sinh, 4, 4),
            ('cosh', self.Cosh, 4, 5),
            ('tanh', self.Tanh, 4, 6),
            ('1/x', self.One_div_x, 4, 7),
            ('0', lambda: self.Enter_Num(0), 5, 0, 2),
            ('.', lambda: self.Standard_Ops('.'), 5, 2),
            ('=', lambda: self.Standard_Ops('='), 5, 3),
            ('ln', self.Ln, 5, 4),
            ('log2', self.Log_2, 5, 5),
            ('log10', self.Log_10, 5, 6),
            ('Abs', self.Abs, 5, 7)
        ]
        
        for (text, cmd, row, col, colspan=1) in buttons:
            self._create_button(text, cmd, row, col, colspan)
    
    def _create_button(self, text, command, row, col, colspan=1):
        btn = tk.Button(self, text=text, command=command, font=('Arial', 10, 'bold'), fg="#000000", width=5, height=2,
                        highlightbackground='#ADD8E6', highlightthickness=2)
        btn.grid(row=row, column=col, columnspan=colspan, sticky='nsew', padx=10, pady=10)

    def Entry(self, value):
        self.ent_field.delete(0, 'end')
        self.ent_field.insert(0, value)

    def Enter_Num(self, num):
        self.result = False
        firstnum = self.ent_field.get()
        secondnum = str(num)
        if self.inp_value:
            self.current = secondnum
            self.inp_value = False
        else:
            self.current = firstnum + secondnum
        self.Entry(self.current)

    def Standard_Ops(self, val):
        temp_str = self.ent_field.get()
        try:
            if val == '=':
                ans = str(eval(temp_str))
                self.result = True
                self.Entry(ans)
            else:
                self.Entry(temp_str + val)
            self.inp_value = False
        except ValueError:
            self.Entry('Error')
        except SyntaxError:
            self.Entry('Error')

    def Clear_Entry(self):
        self.result = False
        self.current = "0"
        self.Entry(0)
        self.inp_value = True

    def SQ_Root(self):
        try:
            self.current = math.sqrt(float(self.ent_field.get()))
            self.Entry(self.current)
        except ValueError:
            self.Entry('Error')
        except SyntaxError:
            self.Entry('Error')

    def Pi(self):
        self.result = False
        self.current = math.pi
        self.Entry(self.current)

    def E(self):
        self.result = False
        self.current = math.e
        self.Entry(self.current)

    def Deg(self):
        try:
            self.result = False
            self.current = math.degrees(float(self.ent_field.get()))
            self.Entry(self.current)
        except ValueError:
            self.Entry('Error')
        except SyntaxError:
            self.Entry('Error')

    def Rad(self):
        try:
            self.result = False
            self.current = math.radians(float(self.ent_field.get()))
            self.Entry(self.current)
        except ValueError:
            self.Entry('Error')
        except SyntaxError:
            self.Entry('Error')

    def Exp(self):
        try:
            self.result = False
            self.current = math.exp(float(self.ent_field.get()))
            self.Entry(self.current)
        except ValueError:
            self.Entry('Error')
        except SyntaxError:
            self.Entry('Error')

    def Fact(self):
        try:
            self.result = False
            self.current = math.factorial(int(self.ent_field.get()))
            self.Entry(self.current)
        except ValueError:
            self.Entry('Error')
        except SyntaxError:
            self.Entry('Error')

    def Sin(self):
        try:
            self.result = False
            self.current = math.sin(math.radians(float(self.ent_field.get())))
            self.Entry(self.current)
        except ValueError:
            self.Entry('Error')
        except SyntaxError:
            self.Entry('Error')

    def Cos(self):
        try:
            self.result = False
            self.current = math.cos(math.radians(float(self.ent_field.get())))
            self.Entry(self.current)
        except ValueError:
            self.Entry('Error')
        except SyntaxError:
            self.Entry('Error')

    def Tan(self):
        try:
            self.result = False
            self.current = math.tan(math.radians(float(self.ent_field.get())))
            self.Entry(self.current)
        except ValueError:
            self.Entry('Error')
        except SyntaxError:
            self.Entry('Error')

    def Sinh(self):
        try:
            self.result = False
            self.current = math.sinh(math.radians(float(self.ent_field.get())))
            self.Entry(self.current)
        except ValueError:
            self.Entry('Error')
        except SyntaxError:
            self.Entry('Error')

    def Cosh(self):
        try:
            self.result = False
            self.current = math.cosh(math.radians(float(self.ent_field.get())))
            self.Entry(self.current)
        except ValueError:
            self.Entry('Error')
        except SyntaxError:
            self.Entry('Error')

    def Tanh(self):
        try:
            self.result = False
            self.current = math.tanh(math.radians(float(self.ent_field.get())))
            self.Entry(self.current)
        except ValueError:
            self.Entry('Error')
        except SyntaxError:
            self.Entry('Error')

    def Ln(self):
        try:
            self.result = False
            self.current = math.log(float(self.ent_field.get()))
            self.Entry(self.current)
        except ValueError:
            self.Entry('Error')
        except SyntaxError:
            self.Entry('Error')

    def Log_10(self):
        try:
            self.result = False
            self.current = math.log10(float(self.ent_field.get()))
            self.Entry(self.current)
        except ValueError:
            self.Entry('Error')
        except SyntaxError:
            self.Entry('Error')

    def Log_2(self):
        try:
            self.result = False
            self.current = math.log2(float(self.ent_field.get()))
            self.Entry(self.current)
        except ValueError:
            self.Entry('Error')
        except SyntaxError:
            self.Entry('Error')

    def Pow_2(self):
        try:
            self.result = False
            self.current = int(self.ent_field.get()) ** 2
            self.Entry(self.current)
        except ValueError:
            self.Entry('Error')
        except SyntaxError:
            self.Entry('Error')

    def Pow_3(self):
        try:
            self.result = False
            self.current = int(self.ent_field.get()) ** 3
            self.Entry(self.current)
        except ValueError:
            self.Entry('Error')
        except SyntaxError:
            self.Entry('Error')

    def Pow_10_n(self):
        try:
            self.result = False
            self.current = 10 ** int(self.ent_field.get())
            self.Entry(self.current)
        except ValueError:
            self.Entry('Error')
        except SyntaxError:
            self.Entry('Error')

    def One_div_x(self):
        try:
            self.result = False
            self.current = 1 / float(self.ent_field.get())
            self.Entry(self.current)
        except ValueError:
            self.Entry('Error')
        except SyntaxError:
            self.Entry('Error')

    def Abs(self):
        try:
            self.result = False
            self.current = abs(float(self.ent_field.get()))
            self.Entry(self.current)
        except ValueError:
            self.Entry('Error')
        except SyntaxError:
            self.Entry('Error')


if __name__ == "__main__":
    calc = SC_Calculator()
    calc.mainloop()
