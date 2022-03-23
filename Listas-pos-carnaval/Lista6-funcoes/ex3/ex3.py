def rev(num: int) -> int:
    """Manuseia o número invertendo a sua ordem"""
    num = str(num)
    num = list(reversed(num))
    num = ''.join(num)
    return int(num)

def rev2(num: int) -> int:
    rev = 0
    digito = 0
    while num != 0:
        digito =  num % 10
        rev *= 10
        rev += digito
        num //= 10
    return rev


numero = int(input("Digite um número inteiro qualquer:\n>"))
reverso = rev(numero)
reverso2 = rev2(numero)
print(f"O reverso desse número é igual a: {reverso}")
print(f"O reverso desse número é igual a: {reverso2}")