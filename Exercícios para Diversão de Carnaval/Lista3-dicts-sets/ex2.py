"""
Faça um programa que lê uma sigla de um estado do usuário e imprime na 
tela o nome completo do estado. Exemplo:

>>> Digite um estado: SP
>>> O nome completo do estado é São Paulo.

"""

siglas_estados = {"SP": "São Paulo", "MG": "Minas Gerais", "AC": "Acre", 
                "RO": "Rondônia", "RR": "Roraima", "PI": "Piau", 
                "PR": "Paraná", "TO": "Tocantins", "PE": "Pernambuco", 
                "BA": "Bahia", "MT": "Mato Grosso", "GO": "Goiás", 
                "RS": "Rio Grande do Sul", "SC": "Santa Catarina", 
                "AM": "Amazonas", "RJ": "Rio de Janeiro", "PA": "Paraná", 
                "CE": "Ceará", "ES": "Espírito Santo", "MA": "Maranhão", 
                "RN": "Rio Grande do Norte", "SE": "Sergipe"}

def valida_sigla(siglas_estados):
    while True:
        try:
            sigla = str(input('>'))
            sigla = sigla.upper()
            while sigla not in siglas_estados:
                sigla = str(input("Digite uma sigla válida:\n>"))
            return sigla
        except ValueError:
            print("Valor inválido, digite uma sigla:")


print("Forneça a sigla do seu estado:")
sigla = valida_sigla(siglas_estados)

print(f"A sigla {sigla} refere-se ao estado: {siglas_estados[sigla]}")


