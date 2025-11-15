# Operadores condicionais em Python
# Em Python, os operadores condicionais são usados para comparar valores e tomar decisões com base nessas comparações.

# Lista dos principais operadores condicionais: 
# Igual a: ==
# Diferente de: !=
# Maior que: >
# Menor que: <
# Maior ou igual a: >=
# Menor ou igual a: <=


# E vamos utilizar esses operadores em estruturas condicionais como if, elif e else.




# Exemplo 1: Usando if para verificar se um número é positivo

numero = 10
if numero > 0:
    print(f"O número {numero} é positivo.")
# Imprime: O número 10 é positivo.





# Exemplo 2: Usando if-else para verificar se um número é par ou ímpar

numero = 7
if numero % 2 == 0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")

# Imprime: O número 7 é ímpar.





# Exemplo 3: Usando if-elif-else para classificar a idade de uma pessoa

idade = 20
if idade < 12:
    print("Criança")
elif 12 <= idade < 18:
    print("Adolescente")
else:
    print("Adulto")

# Imprime: Adulto





# Exemplo 4: Verificando múltiplas condições com operadores lógicos

idade = 25
altura = 1.80

if idade >= 18 and altura >= 1.60:
    print("Você é elegível para o time de basquete.")

# Imprime: Você é elegível para o time de basquete.



