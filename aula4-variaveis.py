# As variáveis em Python são usadas para armazenar valores que podem ser usados e manipulados ao longo do código.
idade = 25  # Variável do tipo inteiro
nome = "Alice"  # Variável do tipo string
altura = 1.75  # Variável do tipo float (número decimal)
estudando = True  # Variável do tipo booleano (True ou False)

# Podemos usar a função type() para verificar o tipo de uma variável

print(type(idade))     # <class 'int'>
print(type(nome))      # <class 'str'>
print(type(altura))    # <class 'float'>
print(type(estudando)) # <class 'bool'>

# As variáveis também podem ser reatribuídas para armazenar valores de tipos diferentes

idade = "vinte e cinco"  # Agora idade é uma string
print(type(idade))  # <class 'str'>


# Além disso, podemos usar variáveis em expressões e operações

soma_idade = 5 + 10  # Soma de dois inteiros
print("Soma da idade:", soma_idade)  # Imprime: Soma da idade: 15

nova_altura = altura + 0.05  # Adiciona 0.05 à altura

