def C_F(celsius:float) -> float:
    """converte celsius para fahrenheit"""
    return celsius * 9 / 5 + 32

celsius = 0

while celsius <= 100:
    print(f'{repr(celsius).rjust(3)} ºC ---> {repr(C_F(celsius)).rjust(5 )} ºF')
    celsius += 10