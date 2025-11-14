# Em python, como tudo é um objeto, as strings possuem diversos métodos embutidos que facilitam a manipulação e formatação de texto.
# Vamos explorar alguns dos métodos mais comuns para formatação de strings.

# Exemplo 1: Usando o método .upper() para converter uma string para maiúsculas
texto = "Olá, mundo!"
texto_maiusculo = texto.upper()
print("Texto em maiúsculas:", texto_maiusculo)  # Imprime: Texto em maiúsculas: OLÁ, MUNDO!

# Exemplo 2: Usando o método .lower() para converter uma string para minúsculas
texto_minusculo = texto.lower()
print("Texto em minúsculas:", texto_minusculo)  # Imprime: Texto em minúsculas: olá, mundo!

# Exemplo 3: Usando o método .replace() para substituir partes de uma string
texto_substituido = texto.replace("mundo", "Python")
print("Texto substituído:", texto_substituido)  # Imprime: Texto substituído: Olá, Python!

# Exemplo 4: Usando o método .strip() para remover espaços em branco no início e no fim da string
texto_com_espacos = "   Olá, mundo!   "
texto_sem_espacos = texto_com_espacos.strip()
print("Texto sem espaços:", texto_sem_espacos)  # Imprime: Texto sem espaços: Olá, mundo!

# Exemplo 5: Usando f-strings para formatação avançada
nome = "Alice"
idade = 25
altura = 1.75
mensagem = f"Meu nome é {nome}, eu tenho {idade} anos e minha altura é {altura:.2f} metros."
print("Mensagem formatada:", mensagem)  # Imprime: Mensagem formatada: Meu nome é Alice, eu tenho 25 anos e minha altura é 1.75 metros.

# Exemplo 6: Usando o método .format() para formatação de strings
mensagem_formatada = "Meu nome é {}, eu tenho {} anos e minha altura é {:.2f} metros.".format(nome, idade, altura)
print("Mensagem formatada com .format():", mensagem_formatada)  # Imprime: Mensagem formatada com .format(): Meu nome é
# Alice, eu tenho 25 anos e minha altura é 1.75 metros.

