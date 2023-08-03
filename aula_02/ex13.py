# Crie um conversor de temperatura (°C °F K)

celsius = int(input("Quantos graus está fazendo hoje? "))
fahrenheit = (celsius*1.8) + 32
kelvin = (fahrenheit - 32) / 9

print(f"O temperatura em celsius é: {celsius}")
print(f"Transformando celsius em fahrenheit fica: {fahrenheit}")
print(f"Transformando fahrenheit em kelvin fica: {kelvin}")      