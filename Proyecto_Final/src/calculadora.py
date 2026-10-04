class Calculadora:

    def __init__(self, numeros):
        self._numeros = numeros
        self._historial = []

    @property
    def numeros(self):
        return self._numeros

    @numeros.setter
    def numeros(self, nuevos_numeros):
        if all(type(numero) in (int, float) for numero in nuevos_numeros):
            self._numeros = nuevos_numeros
        else:
            raise ValueError("Todos los valores deben ser números")

    def sumar(self):
        resultado = sum(self._numeros)
        self._registrar_operacion('+', resultado)
        return resultado

    def restar(self):
        resultado = self._numeros[0]
        for numero in self._numeros[1:]:
            resultado -= numero
        self._registrar_operacion('-', resultado)
        return resultado

    def multiplicar(self):
        resultado = 1
        for numero in self._numeros:
            resultado *= numero
        self._registrar_operacion('*', resultado)
        return resultado

    def dividir(self):
        resultado = self._numeros[0]
        for numero in self._numeros[1:]:
            resultado /= numero
        self._registrar_operacion('/', resultado)
        return resultado

    def potencia(self):
        resultado = self._numeros[0] ** self._numeros[1]
        self._registrar_operacion('^', resultado)
        return resultado

    def _registrar_operacion(self, operador, resultado):
        operacion = f" {operador} ".join(str(numero) for numero in self._numeros)
        self._historial.append({
            'operacion': operacion,
            'resultado': resultado
        })

    def ver_historial(self):
        if not self._historial:
            print("No hay operaciones en el historial.")
            return

        print("\n--- Historial de Operaciones ---")
        for i, operacion in enumerate(self._historial, 1):
            print(f"{i}. {operacion['operacion']} = {operacion['resultado']}")
            