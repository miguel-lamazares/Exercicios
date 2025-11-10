# =============================================================
# PRIMEIRO EXERCÍCIO — Jogo de adivinhação
# =============================================================

import random

a = [0,1,2,3,4,5]
i = 0 

print("====================================================================")
print("Olá, eu sou um gênio. Você seria capaz de adivinhar o número em que pensei?")
print("====================================================================")
print("")
while True:
	i+=1
	num = random.choice(a)
	b = int(input("Digite um número (de 0 a 5): "))
	
	if b == num:
		print(f"Parabéns! O número era {num}. Você acertou em {i} tentativas!")
		break
	else:
		print(f"Você errou, tente novamente, lembre-se talvez o número mudou")
		print(f"Número de tentativas até o momento: {i}") 
		continue
	

# =============================================================
# SEGUNDO EXERCÍCIO — Cálculo de multa por excesso de velocidade
# =============================================================

z = int(input("\nQual era a velocidade do veículo (em km/h)? "))

if z <= 80:
	print("Tudo certo. Você permaneceu dentro do limite de velocidade permitido.")
else:
	m = (z - 80)
	m = m * 7
	print(f"Você ultrapassou o limite de velocidade ({z} km/h). A multa será de R$ {m:.2f}.")

# =============================================================
# TERCEIRO EXERCÍCIO — Verificação de número par ou ímpar
# =============================================================

x = int(input("\nDigite um número: "))
if x % 2 == 0:
	print('O número é par.')
else: 
	print("O número é ímpar.")

# =============================================================
# QUARTO EXERCÍCIO — Cálculo de valor de passagem
# =============================================================

p = float(input("\nQual é a distância da viagem (em km)? "))
if p >= 200:
	v = (p * 0.45)
else:
	v = (p * 0.5)
	
print(f"O valor da passagem é R$ {v:.2f}.")

# =============================================================
# QUINTO EXERCÍCIO — Verificação de ano bissexto
# =============================================================

a = int(input("\nDigite um ano: "))
if a % 4 == 0:
	print("Este é um ano bissexto.")
else:
	print("Este não é um ano bissexto.")

# =============================================================
# SEXTO EXERCÍCIO — Identificação do maior e do menor número
# =============================================================

a = int(input("\nDigite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))

# how i wished do it
# ma = max(a,b,c)
# mi = min(a,b,c)

if a >= b and a >= c:
	ma = a
elif b >= c:
	ma = b
else:
	ma = c

if a <= b and a <= c:
	mi = a
elif b <= c:
	mi = b
else:
	mi = c

print(f"O maior número é {maior} e o menor é {menor}.")



# =============================================================
# SÉTIMO EXERCÍCIO — Reajuste salarial
# =============================================================

s = float(input("\nQual é o seu salário atual (em reais)? "))
if s >= 1250:
	a = (s * 0.10) + s
else:
	a = (s * 0.15) + s

print(f"Seu salário de R$ {s:.2f} foi reajustado para R$ {novo_salario:.2f}.")

# =============================================================
# OITAVO EXERCÍCIO — Existência de triângulo
# =============================================================

a = int(input("\nDigite o primeiro lado do triângulo: "))
b = int(input("Digite o segundo lado do triângulo: "))
c = int(input("Digite o terceiro lado do triângulo: "))

if a >= b + c or b >= a + c or c >= a + b:
	print("este triangulo não atende a lei de existência")
else:
	print("este triangulo atende a lei de existência")


