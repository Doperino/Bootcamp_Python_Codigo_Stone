import modulo

valores = list()

print("\nDigite a quantidade de números que quiser para cálculo da média.")
print("Obs: o 1º valor não pode ser igual a 0. A partir do 2º, o valor 0 retornará a média aritmética dos números.")


while True:
    num = modulo.valida_num(valores)
    if num == 0:
        break
    else:
        valores.append(num)

modulo.calcula_media(valores)