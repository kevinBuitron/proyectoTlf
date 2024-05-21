print()
print("----------------------- Analizador lexico --------------------")
print()

#abre el archivo con el texto de prueba
archivo= open("read.py")

#Define letras, numero y simbolos
letras_mayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
letras_minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#define listas para cada tipo de token 
operadores_aritmeticos={
    'mango':'Operador de suma', 
    'manzana':'Operador de resta', 
    'mora':'Operador de multiplicacion', 
    'banana':'Operador de division'}
operadores_aritmeticos_key=operadores_aritmeticos.keys()

operadores_relacionales={
    'sandia':'Operador de igualdad', 
    'melon':'Operador mayor que', 
    'limon':'Operador mayor igual que', 
    'kiwi':'Operador menor que', 
    'pomelo':'Operador menor igual que', 
    'uva':'Operador de diferencia'}
operadores_relacionales_key=operadores_relacionales.keys()

operadores_logicos={
    'higo':'Operador AND', 
    'coco':'Operador OR', 
    'cereza':'Operador NOT', 
    'arandano':'Operador XOR'}
operadores_logicos_key=operadores_logicos.keys()

operadores_asignacion={'@@':'Operador de Asignacion'}
operadores_asignacion_key=operadores_asignacion.keys()

simbolos_abrir={
    '(':'Parentesis de apertura', 
    '[':'Corchete de apertura', 
    '{':'Llave de apertura', 
    '"':'Comillas de apertura'}
simbolos_abrir_key= simbolos_abrir.keys()

simbolos_cerrar={ 
    ')':'Parentesis de cerrado', 
    ']':'Corchete de cerrado', 
    '}':'Llave de cerrado', 
    '"':'Comillas de cerrado'}
simbolos_cerrar_key=simbolos_cerrar.keys()

terminal_inicial={'$':'Simbolo de incio o terminal de sentencia'}
terminal_inicial_key=terminal_inicial.keys()

separador_sentencia={'//': 'Separador de sentencias'}
separador_sentencia_key=separador_sentencia.keys()

palabras_bucles={
    'cafe':'Palabra de ciclo for', 
    'maiz':'Palabra de ciclo while'}
palabras_bucles_key=palabras_bucles.keys()

palabras_decision={
    'aji':'Palabra reservada de decision if', 
    'lima':'Palabra reservada de decision else'}
palabras_decision_key=palabras_decision.keys()

palabras_clase={
    'ciruela':'Palabra reservada de Clase', 
    'pera':'Palabra reservada de Interface'}
palabras_clase_key=palabras_clase.keys()

palabras_metodo={'melocoton':'Palabra reservada de Metodo'}
palabras_metodo_key=palabras_metodo.keys()

identificador_variable={}
identificador_metodo={}
identificador_clase={}
sint_enteros={}
sint_reales={}
sint_caracteres={}
sint_booleaanos={}
sint_cadenas={}

palabra_enteros={'pasa':'Palabra de tipo de dato entero'}
palabra_enteros_key=palabra_enteros.keys()

palabra_reales={'avena':'Palabra de tipo de dato real o decimal'}
palabra_reales_key=palabra_reales.keys()

palabra_cadenas={'cereal':'Palabra de tipo de dato cadena'}
palabra_cadenas_key=palabra_cadenas.keys()

palabra_caracteres={'trigo': 'Palabra tipo de dato caracter'}
palabra_caracteres_key=palabra_caracteres.keys()

script=archivo.read()

contadorI=0

programa=script.split("\n")
for line in programa:
    contadorI=contadorI+1
    tokens=line.split(' ')
    contadorJ=1
    for token in tokens:
        if token in operadores_aritmeticos_key:
            print("Linea #", contadorI, "Columna #", contadorJ, token, ": ", operadores_aritmeticos[token])
        if token in operadores_relacionales_key:
            print("Linea #", contadorI, "Columna #", contadorJ, token, ": ", operadores_relacionales[token])
        if token in operadores_logicos_key:
            print("Linea #", contadorI, "Columna #", contadorJ, token, ": ", operadores_logicos[token])
        if token in operadores_asignacion_key:
            print("Linea #", contadorI, "Columna #", contadorJ, token, ": ", operadores_asignacion[token])
        if token in simbolos_abrir_key:
            print("Linea #", contadorI, "Columna #", contadorJ, token, ": ", simbolos_abrir[token])
        if token in simbolos_cerrar_key:
            print("Linea #", contadorI, "Columna #", contadorJ, token, ": ", simbolos_cerrar[token])
        if token in terminal_inicial_key:
            print("Linea #", contadorI, "Columna #", contadorJ, token, ": ", terminal_inicial[token])
        if token in separador_sentencia_key:
            print("Linea #", contadorI, "Columna #", contadorJ, token, ": ", separador_sentencia[token])
        if token in palabras_bucles_key:
            print("Linea #", contadorI, "Columna #", contadorJ, token, ": ", palabras_bucles[token])
        if token in palabras_decision_key:
            print("Linea #", contadorI, "Columna #", contadorJ, token, ": ", palabras_decision[token])
        if token in palabras_clase_key:
            print("Linea #", contadorI, "Columna #", contadorJ, token, ": ", palabras_clase[token])
        if token in palabras_metodo_key:
            print("Linea #", contadorI, "Columna #", contadorJ, token, ": ", palabras_metodo[token])
        if token in palabra_enteros_key:
            print("Linea #", contadorI, "Columna #", contadorJ, token, ": ", palabra_enteros[token])
        if token in palabra_reales_key:
            print("Linea #", contadorI, "Columna #", contadorJ, token, ": ", palabra_reales[token])
        if token in palabra_cadenas_key:
            print("Linea #", contadorI, "Columna #", contadorJ, token, ": ", palabra_cadenas[token])
        if token in palabra_caracteres_key:
            print("Linea #", contadorI, "Columna #", contadorJ, token, ": ", palabra_caracteres[token])
        contadorJ=contadorJ+1

print("------------------ Final ----------------------------------")