# 1
import os  # importa o módulo os para usar a função system
os.system("cls") or None  # limpa a tela do console

faturamento = 50000
percentual_bonus = 0.1 #10.1 é o mesmo que 10%
bonus_total = faturamento * percentual_bonus
faturamento_liquido = faturamento - bonus_total
print("Faturamento Liquido: ", faturamento_liquido)
print("Bonus Total: ", bonus_total)

#2
