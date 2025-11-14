# No python a concatenação de strings pode ser feita de várias maneiras.
# A forma mais comum é usando o operador de adição (+).

# Exemplo 1: Usando o operador +
nome = "Alice"
sobrenome = "Silva"
nome_completo = nome + " " + sobrenome
print("Nome completo (usando +):", nome_completo)  # Imprime: Nome completo (usando +): Alice Silva

# Exemplo 2: Usando f-strings (disponível a partir do Python 3.6)

idade = 25
mensagem = f"Meu nome é {nome} {sobrenome} e eu tenho {idade} anos."

print("Mensagem (usando f-strings):", mensagem)  # Imprime: Mensagem (usando f-strings): Meu nome é Alice Silva e eu tenho 25 anos.


# Além disso, existe a repetição de strings usando o operador de multiplicação (*).

# Exemplo 3: Repetindo strings

eco = "Olá! "* 3
print("Eco (usando *):", eco)  # Imprime: Eco (usando *): Olá! Olá! Olá!



