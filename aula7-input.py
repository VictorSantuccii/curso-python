# No python existe uma função chamada input() que permite ao usuário inserir dados durante a execução do programa.
# A função input() lê uma linha do input (geralmente do teclado) e retorna como uma string.
# Exemplo 1: Solicitando o nome do usuário

nome = input("Digite seu nome: ")
print("Olá,", nome + "!")  # Imprime uma saudação ao usuário

# Exemplo 2: Solicitando a idade do usuário e convertendo para inteiro
idade = int(input("Digite sua idade: "))
print("Você tem", idade, "anos.")  # Imprime a idade do usuário

# Exemplo 3: Solicitando a altura do usuário e convertendo para float
altura = float(input("Digite sua altura em metros (ex: 1.75): "))
print("Sua altura é", altura, "metros.")  # Imprime a altura do usuário

# Exemplo 4: Solicitando se o usuário está estudando (True/False) e convertendo para booleano
estudando_input = input("Você está estudando? (sim/não): ").strip().lower()
estudando = estudando_input == "sim"
print("Estudando:", estudando)  # Imprime se o usuário está estudando ou não

# Exemplo 5: Solicitando múltiplas informações e exibindo uma mensagem formatada
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura em metros (ex: 1.75): "))

mensagem = f"Meu nome é {nome}, eu tenho {idade} anos e minha altura é {altura:.2f} metros."
print(mensagem)  # Imprime a mensagem formatada com as informações do usuário
