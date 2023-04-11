def ler_temp():
    temp = float(input("Qual a temperatura em graus celsius: "))
    return temp

def calc_fahrenheit(temp_celsius):
    temp_fahrenheit = (9 * temp_celsius + 160)/5
    return temp_fahrenheit

def exibir_resultado(temp_fahrenheit):
    print("A temperatura em fahrenheit é: ", temp_fahrenheit)

temp_celsius = ler_temp()
temp_fahrenheit = calc_fahrenheit(temp_celsius)
exibir_resultado(temp_fahrenheit)