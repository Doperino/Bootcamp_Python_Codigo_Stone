import random

def embaralha(palavra: str, k: None | int = None) -> str:
    """Embaralha a string digitada"""
    if k == None:
        k = len(palavra)
    emb = random.sample(palavra, k)
    return ''.join(emb).lower()

palavra = input("Escreva a palavra a ser embaralhada:\n>")
print(f"Palavra embaralhada: {embaralha(palavra)}")

