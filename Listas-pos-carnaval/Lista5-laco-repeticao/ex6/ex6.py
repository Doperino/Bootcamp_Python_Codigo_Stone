n = 2
int_H = 1
frac_H = 0
for i in range(n):
    frac_H += 1 / (2 + i)
h = int_H + frac_H
print(h)