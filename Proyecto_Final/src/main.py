from calculadora import Calculadora


def interpretar_expresion(expresion):
    for operador in ['+', '-', '*', '/', '^']:
        if operador in expresion:
            partes = expresion.split(operador)

            if len(partes) >= 2:
                numeros = [float(numero.strip()) for numero in partes]
                return numeros, operador

    return None
def main():
    calc = Calculadora([])

    operaciones = {
        '+': calc.sumar,
        '-': calc.restar,
        '*': calc.multiplicar,
        '/': calc.dividir,
        '^': calc.potencia
    }

    print("Calculadora. Escribe 'salir' para terminar o 'historial' para ver operaciones.\n")

    while True:
        entrada = input("Ingresa la operación: ")

        if entrada.strip().lower() == "salir":
            print("¡Hasta pronto!")
            break

        if entrada.strip().lower() == "historial":
            calc.ver_historial()
            continue

        resultado = interpretar_expresion(entrada)

        if not resultado:
            print("Expresión no válida.\n")
            continue

        numeros, operador = resultado
        calc.numeros = numeros

        try:
            print("Resultado:", operaciones[operador]())
        except (ZeroDivisionError, ValueError, IndexError):
            print("No se pudo realizar la operación.")
main()
         