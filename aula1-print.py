# Interpretador de código python : python aula1.py -> rodar um arquivo em python
print("Hello, World!")  # print é uma função que imprime na tela o que estiver entre parênteses

"""
Comentário com DocString
Podemos usar aspas triplas para fazer comentários de múltiplas linhas
Tanto as aspas simples quanto as aspas duplas podem ser usadas para criar DocStrings

"""

# A função print recebe argumentos, que são os valores que queremos imprimir na tela
print('Olá, Mundo!', 10)  # Podemos usar aspas simples ou duplas para strings
print(42)  # Podemos imprimir números inteiros

# O print já tem um caractere de nova linha (\n) no final, então cada print será em uma nova linha

# Além disso, a função print já possui um separador padrão entre os argumentos, que é um espaço
print('Python', 'é', 'legal!')  # Imprime: Python é legal
print('Python', 'é', 'legal!', sep='-')  # Imprime: Python-é-legal!

# O sep é um parâmetro opcional que define o separador entre os argumentos, que pode ser usado para
# personalizar a saída do print

# Existem também outros parâmetros opcionais, como end, que define o que será impresso no final
print('Primeira linha', end=' *** ')  # Imprime: Primeira linha ***
print('Segunda linha')  # Imprime: Segunda linha
# Nesse caso, o end foi alterado para ' *** ', então a primeira linha termina com isso

# Além do padrão CRLF (\r\n) em sistemas Windows, o Python também reconhece o LF (\n) usado em sistemas Unix/Linux e macOS
print("Linha 1\nLinha 2")  # Imprime duas linhas
print("Coluna 1\tColuna 2")  # Imprime com tabulação entre as colunas

# O \t é usado para criar uma tabulação (espaço maior) entre os textos
print("Aspas simples: ' ' e aspas duplas: \" \"")  # Imprime aspas simples e duplas
# O caractere de escape \" é usado para imprimir aspas duplas dentro de uma string delimitada por aspas duplasD