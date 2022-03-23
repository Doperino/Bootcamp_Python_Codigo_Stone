valores = list()

print("\nDigite a quantidade de números que quiser para cálculo da média.")
print("Obs: o 1º valor não pode ser igual a 0. A partir do 2º, o valor 0 retornará a média aritmética dos números.")

num = 1
i = 1
while num != 0:
    num = float(input(f'{i}º> '))
    if len(valores) == 0:
        while num == 0:
            num = float(input(f'Valor inválido. Digite novamente o {i}º> '))

    elif len(valores) != 0:
        if num == 0:
            break

    valores.append(num)
    i += 1

media = sum(valores)/len(valores)
print(f'média aritmética ---> {round(media, 2)}')


