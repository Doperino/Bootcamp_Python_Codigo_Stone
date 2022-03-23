import itertools

def geraQdMag(num: list) -> list:
    qd_mag = list()
    all_perm = list(itertools.permutations(a))
            
    for i in all_perm:
        if i[0] + i[1] + i[2] == i[3] + i[4] + i[5] and i[0] + i[1] + i[2] == i[6] + i[7] + i[8]:
            if i[0] + i[3] + i[6] == i[1] + i[4] + i[7] and i[0] + i[3] + i[6] == i[2] + i[5] + i[8]:
                if i[0] + i[4] + i[8] == i[2] + i[4] + i[6]:
                    qd_mag.append(i)

    for i in qd_mag:
        print(i[0], i[1], i[2])
        print(i[3], i[4], i[5])
        print(i[6], i[7], i[8])
        print('')

perm_valid = list()

a = [1, 2, 3, 4 ,5, 6, 7, 8, 9]
geraQdMag(a)


