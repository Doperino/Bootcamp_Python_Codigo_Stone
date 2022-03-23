def calcula_pi(i: int) -> float:
    pi_int = 3
    pi_frac = 0
    for j in range(i):
        num = (-1) ** j * 4
        den = (2 + 2 * j) * (3 + 2 * j) * (4 + 2 * j)
        pi_frac += num / den
    pi = pi_int + pi_frac
    return pi

num_aprox = int(input("Número de aproximações do número pi: "))
print(f"Valor de pi: {calcula_pi(num_aprox)}")


