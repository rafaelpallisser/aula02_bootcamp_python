import math

# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
# n1 = int(input("Digite o primeiro número: "))
# n2 = int(input("Digite o segundo número: "))
# soma = n1 + n2
# print(soma)

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
# numero = int(input("Digite um número: "))
# print(numero % 5)

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
# n1 = int(input("Digite o primeiro número: "))
# n2 = int(input("DIgite o segundo número: "))
# multiplicacao = n1 * n2
# print(multiplicacao)

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
# n1 = int(input("Digite o primeiro número: "))
# n2 = int(input("DIgite o segundo número: "))
# print(n1 // n2)

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
# numero = int(input("Digite um número: "))
# quadrado = numero ** 2
# print(quadrado)


# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
# n1 = float(input("Digite o primeiro número: "))
# n2 = float(input("Digite o segundo número: "))
# adicao = n1 + n2
# print(adicao)

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
# n1 = float(input("Digite o primeiro número: "))
# n2 = float(input("Digite o segundo número: "))
# media = (n1 + n2) / 2
# print(media)

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
# base = float(input("Digite a base: "))
# expoente = int(input("Digite o expoente: "))
# potencia = base ** expoente
# print(potencia)

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
# celsius = float(input("Digite a temperatura em graus celsius: "))
# fahrenheit = (celsius * 9 / 5) + 32
# print(f"Temperatura em fahrenheits: {fahrenheit}")

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
# pi = math.pi
# raio = float(input("Digite o raio: "))
# area = pi * (raio ** 2)
# print(f"{area:.2f}")


# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
# texto = input("Digite um texto: ")
# print(texto.upper())

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
# nome_usuario = input("Digite seu nome completo: ")
# nome_usuario_min = nome_usuario.lower()
# print(nome_usuario_min)

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
# frase = input("Digite uma frase: ")
# print(frase.strip())

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
# data = input("Digite uma data no formato dd/mm/yyyy: ")
# data_separada = data.split("/")
# dia = data_separada[0]
# mes = data_separada[1]
# ano = data_separada[2]
# print(f"Dia: {dia}")
# print(f"Mês: {mes}")
# print(f"Ano: {ano}")

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
# txt1 = input("Digite o primeiro texto: ")
# txt2 = input("Digite o segundo texto: ")
# txt_concat = txt1 + " " + txt2
# print(txt_concat)


# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
# exp1 = bool(int(input("Digite a primeira expressão booleana (1 = True | 0 = False): ")))
# exp2 = bool(int(input("Digite a segunda expressão booleana (1 = True | 0 = False): ")))
# resultado = exp1 and exp2
# print(f"{exp1} OR {exp2} = {resultado}")

# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# exp1 = bool(int(input("Digite a primeira expressão booleana (1 = True | 0 = False): ")))
# exp2 = bool(int(input("Digite a segunda expressão booleana (1 = True | 0 = False): ")))
# resultado = exp1 or exp2
# print(f"{exp1} OR {exp2} = {resultado}")

# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# valor_bool = bool(int(input("Digite um valor booleano (1 = True | 0 = False): ")))
# valor_bool_invertido = not valor_bool
# print(f"Valor digitado: {valor_bool}")
# print(f"Valor invertido: {valor_bool_invertido}")

# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# n1 = float(input("Digite o primeiro número: "))
# n2 = float(input("Digite o segundo número: "))
# valida = n1 == n2
# print(f"Os números são diferentes: {valida}")

# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
valida = n1 != n2
print(f"Os números são diferentes: {valida}")


# #### try-except e if

# 21: Conversor de Temperatura
# 22: Verificador de Palíndromo
# 23: Calculadora Simples
# 24: Classificador de Números
# 25: Conversão de Tipo com Validação