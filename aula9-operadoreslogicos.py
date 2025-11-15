# Os operadores lógicos em Python são usados para combinar expressões booleanas.

# Os principais operadores lógicos são:

# E lógico: and
# Ou lógico: or
# Negação lógica: not

# Exemplo 1: Usando o operador and
idade = 25
if idade >= 18 and idade < 65:
    print("Você é um adulto.")

# Imprime: Você é um adulto.


# Exemplo 2: Usando o operador or
dia = 70
if dia == 6 or dia == 7:
    print("É fim de semana!")

# Imprime: É fim de semana!



# Exemplo 3: Usando o operador not
chovendo = False
if not chovendo:
    print("Vamos sair para passear!")

# Imprime: Vamos sair para passear!


# Exemplo 4: Combinando múltiplos operadores lógicos
idade = 30
altura = 1.75
if (idade >= 18 and idade <= 65) or altura > 1.80:
    print("Você atende aos requisitos.")

# Imprime: Você atende aos requisitos.


# Operadores in e not in

# Exemplo 5: Usando o operador in

frutas = ["maçã", "banana", "laranja"]

if "banana" in frutas:
    print("Banana está na lista de frutas.")

# Imprime: Banana está na lista de frutas.


# Exemplo 6: Usando o operador not in

veiculos = ["carro", "moto", "bicicleta"]

if "avião" not in veiculos:
    print("Avião não está na lista de veículos.")

# Imprime: Avião não está na lista de veículos.


