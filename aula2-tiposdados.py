# Como o Python possui tipagem dinâmica, não precisamos declarar o tipo da variável antes de usá-la
# Basta atribuir um valor a uma variável e o Python infere o tipo automaticamente

# Python também possui uma tipagem forte, o que significa que não podemos misturar
# tipos de dados de forma inconsistente

# Existem outras linguagens que possuem tipagem fraca ou tipagem estática, como C e Java

# O python possui vários tipos de dados embutidos, como:

# Números inteiros (int)
# Números de ponto flutuante (float)
# Strings (str)
# Booleanos (bool)
 
# Esses são os tipos primitivos mais comuns, mas existem outros tipos compostos, como:

# Listas (list)
# Tuplas (tuple)
# Dicionários (dict)
# Conjuntos (set)




idade = 25  # Variável do tipo inteiro
nome = "Alice"  # Variável do tipo string
altura = 1.75  # Variável do tipo float (número decimal)
estudando = True  # Variável do tipo booleano (True ou False)


# Podemos usar a função type() para verificar o tipo de uma variável


print(type(idade))     # <class 'int'>
print(type(nome))      # <class 'str'>
print(type(altura))    # <class 'float'>
print(type(estudando)) # <class 'bool'>


# Podemos fazer conversões entre tipos de dados usando funções como int(), float(), str() e bool()


idade_str = str(idade)  # Converte inteiro para string
altura_int = int(altura)  # Converte float para inteiro (perde a parte decimal)
print("Idade como string:", idade_str)  # Imprime: Idade como string: 25
print("Altura como inteiro:", altura_int)  # Imprime: Altura como inteiro: 1


# Note que a conversão de float para int trunca o valor decimal


# Caracteres de escape em strings
print("Linha 1\nLinha 2")  # Imprime duas linhas
print("Coluna 1\tColuna 2")  # Imprime com tabulação entre as colunas
print("Aspas simples: ' ' e aspas duplas: \" \"")  # Imprime aspas simples e duplas

# O caractere de escape \" é usado para imprimir aspas duplas dentro de uma string delimitada por aspas duplas
# O caractere de escape \' é usado para imprimir aspas simples dentro de uma string delimitada por aspas simples

# Podemos usar aspas simples, duplas ou triplas para definir strings
string_simples = 'Olá, Mundo!'  # Aspas simples
string_duplas = "Olá, Mundo!"   # Aspas duplas
string_triplas = """Olá, Mundo!"""  # Aspas triplas para múltiplas linhas


print(string_simples)
print(string_duplas)
print(string_triplas)


# O escape também pode ser usado para pular caracteres e exibí-los na string
print("Oi \"Otávio" )

# Imprime: Oi "Otávio

# E por final, o r antes das aspas indica que a string é raw (crua), ou seja, os caracteres de escape
# não serão interpretados

raw_string = r"C:\Users\Nome\Documentos"
print(raw_string) 

 # Imprime: C:\Users\Nome\Documentos
