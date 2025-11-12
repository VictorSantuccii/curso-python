# Temos que entender que tudo em Python é um objeto, inclusive os valores booleanos
# Os valores booleanos em Python são representados pelos literais True e False (com T e F maiúsculos)

# Além disso, existem os callables que são objetos que podem ser chamados como funções, como por exemplo:
def exemplo_callable():
    return "Eu sou um callable!"
print(exemplo_callable()) 

# Imprime: Eu sou um callable!

# Callable é um termo usado em programação para descrever qualquer objeto que possa ser chamado como uma função.


verdadeiro = True
falso = False

print(type(verdadeiro))  # <class 'bool'>
print(type(falso))       # <class 'bool'>

# Podemos usar valores booleanos em expressões condicionais
if verdadeiro:
    print("Isso é verdadeiro!")
if not falso:
    print("Isso é falso!")
    
# Podemos combinar valores booleanos usando operadores lógicos: and, or, not

# Também existe a comparação entre valores que resulta em booleanos

a = 10
b = 20

print(a < b)   # True
print(a > b)   # False
print(a == b)  # False
print(a != b)  # True