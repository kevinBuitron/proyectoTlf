print()
print("----------------------- Analizador lexico --------------------")
print()

#abre el archivo con el texto de prueba
archivo= open("read.py")

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

simbolos_abrir={}
simbolos_cerrar={}
terminal_inicial={}
separador_sentencia={}
palabras_bucles={}
palabras_decision={}
palabras_clase={}
palabras_metodo={}
identificador_variable={}
identificador_metodo={}
identificador_clase={}
sint_enteros={}
sint_reales={}
sint_caracteres={}
sint_booleaanos={}
sint_cadenas={}
palabra_enteros={}
palabra_reales={}
palabra_booleanos={}
palabra_caracteres={}
palabra_cadenas={}

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
        contadorJ=contadorJ+1

print("Final")