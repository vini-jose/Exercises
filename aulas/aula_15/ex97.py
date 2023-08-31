# Defina uma classe TemperatureConverter com métodos para converter de Celsius para Fahrenheit e vice-versa. 
# Mantenha os atributos e métodos privados.

class ConverterTemperatura:
    def __init__(self, celsiu, fahrenheit):
        self.celsiu = celsiu
        self.fahrenheit = fahrenheit
    
    @property
    def celsiu(self):
        return self._celsiu

    @celsiu.setter
    def celsiu(self, celsiu):
        if self.celsiu != celsiu:
            self._celsiu = celsiu
        else:
            print("ERRO")
            
    @property
    def fahrenheit(self):
        return self._fahrenheit
    
    @fahrenheit.setter
    def fahrenheit(self, fahrenheit):
        if self.fahrenheit != fahrenheit:
            self._fahrenheit = fahrenheit
        else:
            print("ERRRO")

    @classmethod
    def get(cls):
        celsiu = float(input("Qual o valor de celsiu: "))
        fahrenheit = float(input("Qual o valor do fahrenheit: ")) 
        return cls(celsiu, fahrenheit)
    
    def celsius_e_fahrenheit(self):
        fahrenheit = (self.celsiu * 9/5) + 32
        return (f"O valor de fahrenheit é: {fahrenheit}")
    
    def fahrenheit_e_celsius(self):
        celsiu = (self.fahrenheit - 32) * 5/9
        return (f"O valor de celsius é: {celsiu}")

def main():
    aluno1 = ConverterTemperatura.get()
    print(aluno1.celsius_e_fahrenheit())
    print(aluno1.fahrenheit_e_celsius())

main()