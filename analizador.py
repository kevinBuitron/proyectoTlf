import tkinter as tk
from tkinter import filedialog, ttk

#abre el archivo con el texto de prueba
with open("read.py") as archivo:
    script = archivo.read()

#Define letras, numero y simbolos
letras_mayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
letras_minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def analizar_lexico(script):
    # Define tokens y sus descripciones
    tokens = {
        'operadores_aritmeticos': {
            'mango': 'Operador de suma', 
            'manzana': 'Operador de resta', 
            'mora': 'Operador de multiplicacion', 
            'banana': 'Operador de division'
        },
        'operadores_relacionales': {
            'sandia': 'Operador de igualdad', 
            'melon': 'Operador mayor que', 
            'limon': 'Operador mayor igual que', 
            'kiwi': 'Operador menor que', 
            'pomelo': 'Operador menor igual que', 
            'uva': 'Operador de diferencia'
        },
        'operadores_logicos': {
            'higo': 'Operador AND', 
            'coco': 'Operador OR', 
            'cereza': 'Operador NOT', 
            'arandano': 'Operador XOR'
        },
        'operadores_asignacion': {
            '@@': 'Operador de Asignacion'
        },
        'simbolos_abrir': {
            '(': 'Parentesis de apertura', 
            '[': 'Corchete de apertura', 
            '{': 'Llave de apertura', 
            '"': 'Comillas de apertura'
        },
        'simbolos_cerrar': {
            ')': 'Parentesis de cerrado', 
            ']': 'Corchete de cerrado', 
            '}': 'Llave de cerrado', 
            '"': 'Comillas de cerrado'
        },
        'terminal_inicial': {
            '$': 'Simbolo de incio o terminal de sentencia'
        },
        'separador_sentencia': {
            '//': 'Separador de sentencias'
        },
        'palabras_bucles': {
            'cafe': 'Palabra de ciclo for', 
            'maiz': 'Palabra de ciclo while'
        },
        'palabras_decision': {
            'aji': 'Palabra reservada de decision if', 
            'lima': 'Palabra reservada de decision else'
        },
        'palabras_clase': {
            'ciruela': 'Palabra reservada de Clase', 
            'pera': 'Palabra reservada de Interface'
        },
        'palabras_metodo': {
            'melocoton': 'Palabra reservada de Metodo'
        },
        'palabra_enteros': {
            'pasa': 'Palabra de tipo de dato entero'
        },
        'palabra_reales': {
            'avena': 'Palabra de tipo de dato real o decimal'
        },
        'palabra_cadenas': {
            'cereal': 'Palabra de tipo de dato cadena'
        },
        'palabra_caracteres': {
            'trigo': 'Palabra tipo de dato caracter'
        }
    }

    # Generar un diccionario de búsqueda rápida
    lookup = {token: (category, desc) for category, group in tokens.items() for token, desc in group.items()}


    # Procesar el script
    resultado = []
    programa = script.split("\n")
    for contadorI, line in enumerate(programa, start=1):
        tokens = line.split(' ')
        for contadorJ, token in enumerate(tokens, start=1):
            if token in lookup:
                category, desc = lookup[token]
                resultado.append((token, category, f"Linea #{contadorI} Columna #{contadorJ}"))
            if isIdentificadorVariable():
                category, desc= "Identificador Variable"
                resultado.append((token, category, f"Liinea #{contadorI} Columna#{contadorJ}"))
            if isIdentificadorMetodo():
                category, desc= "Identificador Metodo"
                resultado.append((token, category, f"Liinea #{contadorI} Columna#{contadorJ}"))
            if isIdentificadorClase():
                category, desc= "Identificador Clase"
                resultado.append((token, category, f"Liinea #{contadorI} Columna#{contadorJ}"))
            if isValorAsignacionEntero():
                category, desc= "Asignacion Entero"
                resultado.append((token, category, f"Liinea #{contadorI} Columna#{contadorJ}"))
            if isValorAsignacionCaracteres():
                category, desc= "Asignacion Caracteres"
                resultado.append((token, category, f"Liinea #{contadorI} Columna#{contadorJ}"))
            if isValorAsignacionBooleanos():
                category, desc= "Asignacion Booleanos"
                resultado.append((token, category, f"Liinea #{contadorI} Columna#{contadorJ}"))
    return resultado

def isIdentificadorVariable(token):
    identificador=token.split()
    if len(identificador) < 2:
        return False
    
    indice = 0
     # Validar primer caracter (minúscula)
    if not es_minuscula(identificador[indice]):
        return False
    
    indice += 1
    while indice < len(identificador):
    # Validar siguiente caracter (mayúscula, minúscula, número o símbolo)
        if not es_valida_siguiente_caracter(identificador[indice]):
            return False
        indice += 1
        # Si encuentra un símbolo, validar que el siguiente caracter sea '#'
        if es_simbolo(identificador[indice - 1]):
            if identificador[indice] != '#':
                return False
            indice += 1  # Saltar el '#'
        break  # Salir del bucle al encontrar '#'
    # Si termina el bucle sin encontrar '#', la cadena no es válida
    if indice == len(identificador):
        return False

    # La cadena cumple la estructura
    return True

def isIdentificadorMetodo(token):
    identificador=token.split()
    if len(identificador) < 2:
        return False
    
    indice = 0
     # Validar primer caracter (minúscula)
    if not es_minuscula(identificador[indice]):
        return False
    
    indice += 1
    while indice < len(identificador):
    # Validar siguiente caracter (mayúscula, minúscula, número o símbolo)
        if not es_valida_siguiente_caracter(identificador[indice]):
            return False
        indice += 1
        # Si encuentra un símbolo, validar que el siguiente caracter sea '#'
        if es_simbolo(identificador[indice - 1]):
            if identificador[indice] != '&':
                return False
            indice += 1  # Saltar el '#'
        break  # Salir del bucle al encontrar '#'
    # Si termina el bucle sin encontrar '#', la cadena no es válida
    if indice == len(identificador):
        return False

    # La cadena cumple la estructura
    return True

def isIdentificadorClase(token):
    if len(token) < 3:
        return False
    
    if token[0] != '%' or token[-1] != '%':
        return False
    
    # Eliminar los primeros y últimos '%'
    cadena = token[1:-1]

    # Bucle para validar cada segmento "%letra_mayuscula%"
    for caracter in cadena:
        if not caracter.isupper():
            return False

    # La cadena cumple la estructura
    return True

def isValorAsignacionEntero(token):
    if len(token) < 3:
        return False
    
    if token[0] != '#' or token[-1] != '#':
        return False
    
    # Eliminar los primeros y últimos '%'
    cadena = token[1:-1]

    # Bucle para validar cada segmento "%letra_mayuscula%"
    for caracter in cadena:
        if not caracter.isdigit():
            return False

    # La cadena cumple la estructura
    return True

def isValorAsignacionCaracteres(token):
    if len(token) < 3 or len(token)>3:
        return False
    
    if token[0] != '"' or token[-1] != '"':
        return False

    # Bucle para validar cada segmento "%letra_mayuscula%"
    if not (token[1].isdigit or token[1].isupper):
        return False

    # La cadena cumple la estructura
    return True

def isValorAsignacionBooleanos(token):
    if len(token) < 3 or len(token)>3:
        return False
    
    if token[0] != '¡' or token[-1] != '!':
        return False

    # Bucle para validar cada segmento "%letra_mayuscula%"
    if not (token[1]=='V' or token[1]=='F'):
        return False

    # La cadena cumple la estructura
    return True

def es_minuscula(caracter):
  #Verifica si un caracter es una letra minúscula.
  return caracter.islower()

def es_valida_siguiente_caracter(caracter):
  #Verifica si un caracter es válido para la estructura (mayúscula, minúscula, número o símbolo).
  return caracter.isupper() or es_minuscula(caracter) or caracter.isdigit() or es_simbolo(caracter)

def es_simbolo(caracter):
  #Verifica si un caracter es un símbolo (cualquier caracter que no sea letra, número o '#').
  return not caracter.isalnum() and caracter != '#' and caracter!= '&' 

def abrir_archivo():
    ruta_archivo = filedialog.askopenfilename(filetypes=[("Archivos de Python", "*.py"), ("Todos los archivos", "*.*")])
    if ruta_archivo:
        with open(ruta_archivo, 'r') as archivo:
            script = archivo.read()
        resultados = analizar_lexico(script)
        mostrar_resultados(resultados)

def mostrar_resultados(resultados):
    for row in tree.get_children():
        tree.delete(row)
    for token, category, position in resultados:
        tree.insert('', tk.END, values=(token, category, position))


root = tk.Tk()
root.title("Analizador Léxico")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack(padx=10, pady=10)

boton_abrir = tk.Button(frame, text="Abrir archivo", command=abrir_archivo)
boton_abrir.pack()

tree = ttk.Treeview(frame, columns=('Token', 'Categoría', 'Posición'), show='headings')
tree.heading('Token', text='Token')
tree.heading('Categoría', text='Categoría')
tree.heading('Posición', text='Posición')

tree.pack()

root.mainloop()