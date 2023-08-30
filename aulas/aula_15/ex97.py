# Defina uma classe TemperatureConverter com métodos para converter de Celsius para Fahrenheit e vice-versa. 
# Mantenha os atributos e métodos privados.

class ConverterTemperatura:
    def __init__(self):
        pass
    
    def celsius_to_fahrenheit(self, celsius):
        fahrenheit = (celsius * 9/5) + 32
        print(f"O valor de fahrenheit é: {fahrenheit}")
    
    def fahrenheit_to_celsius(self, fahrenheit):
        celsius = (fahrenheit - 32) * 5/9
        print(f"O valor de celsius é: {celsius}")
    
celsiu_1 = float(input("Digite o valor de celsiu: "))
fah = float(input("Digite o valor de fahrenheit: "))

converter_cel = ConverterTemperatura()
converter_fah = ConverterTemperatura()

converter_cel.celsius_to_fahrenheit(celsiu_1)
converter_fah.fahrenheit_to_celsius(fah)