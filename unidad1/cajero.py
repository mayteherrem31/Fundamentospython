# Variables para contar billetes
billetes_1000 = 10
billetes_500 = 10
billetes_200 = 10
billetes_100 = 10
billetes_50 = 10

# Variables para billetes a entregar
entregar_1000 = 0
entregar_500 = 0
entregar_200 = 0
entregar_100 = 0
entregar_50 = 0

# Iniciamos el sistema

print("\n--- Dispensadora de Billetes ---")

# Solicitar monto
print("\nIngrese el monto a retirar (0 para salir):")
#entrada = input() "50"
entrada = int(input())

#valido que la entrada sea multiplo de 50
while entrada % 50 != 0 or entrada > 18500:
    print("La cantidad debe de ser multiplos de 50 y maximo $18,500")
    entrada = int(input("Ingresa otra cantidad: "))

# entra lo dividido entre 1000 = numero de billetes de 1

#
entregar_1000 = entrada // 1000
residuo = entrada % 1000

entregar_500 = residuo // 500
residuo = residuo % 500

entregar_200 = residuo // 200
residuo = residuo % 200

entregar_100 = residuo // 100
residuo = residuo % 100

entregar_50 = residuo // 50
residuo = residuo % 50

#mostrar resultados

print("\n--- Entrega de Billetes ---")

print(f"Billetes de $1000: {entregar_1000}")
print(f"Billetes de $500: {entregar_500}")
print(f"Billetes de $200: {entregar_200}")
print(f"Billetes de $100: {entregar_100}")
print(f"Billetes de $50: {entregar_50}")
