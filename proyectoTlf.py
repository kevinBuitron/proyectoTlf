import tkinter as tk
from tkinter import ttk
import re

class LexicalAnalyzer:
    def __init__(self, code):
        self.code = code
        self.tokens = []

    def analyze(self):
        # Expresiones regulares para los tokens
        patterns = [
            
            
            (r'[0-9]+', 'Numero Natural'),
            (r'[0-9]+\.[0-9]+', 'Numero Real'),
            (r'(my|our|local)', 'Identificador'),
            (r'(if|else|while|function|return|import)', 'Palabra Reservada'),
            (r'(\+|\-|\*|\/)', 'Operador Aritmetico'),
            (r'(==|!=|<|>|<=|>=)', 'Operador de Comparacion'),
            (r'(&&|\|\|)', 'Operador Logico'),
            (r'=', 'Operador de Asignacion'),
            (r'(\+\+|\-\-)', 'Operador Incremento/Decremento'),
            (r'(\(|\))', 'Parentesis'),
            (r'(\{|\})', 'Llaves'),
            (r';', 'Terminal'),
            (r',', 'Separador'),
            (r'0x[0-9a-fA-F]+', 'Hexadecimal'),
            (r'\"(\\\"|[^\"])*\"', 'Cadena de Caracteres'),
            (r'\/\/.*', 'Comentario de Linea'),
            (r'\/\*(.|\n)*\*\/', 'Comentario de Bloque')
        ]

        position = 1
        for pattern, token_type in patterns:
            regex = re.compile(pattern)
            match = regex.search(self.code)
            while match:
                lexeme = match.group(0)
                start = match.start() + position
                end = match.end() + position
                self.tokens.append((lexeme, token_type))
                match = regex.search(self.code, end)

    def get_tokens(self):
        return self.tokens

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("QuirkLang Analizaor Lexico")

        self.text_area = tk.Text(root, wrap=tk.WORD, width=40, height=10)
        self.text_area.pack(pady=10)

        self.analyze_button = ttk.Button(root, text="Analizar", command=self.analyze_code)
        self.analyze_button.pack(pady=5)

        self.tree = ttk.Treeview(root, columns=('Lexico', 'Categoria'))
        self.tree.heading('#0', text='Tokens')
        self.tree.heading('#1', text='Lexico')
        self.tree.heading('#2', text='Categoria')
      
        self.tree.pack(pady=10)

    def analyze_code(self):
        code = self.text_area.get("1.0", "end-1c")
        analyzer = LexicalAnalyzer(code)
        analyzer.analyze()
        self.display_results(analyzer.get_tokens())

    def display_results(self, tokens):
        self.tree.delete(*self.tree.get_children())
        for token in tokens:
            self.tree.insert('', 'end', values=token)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

