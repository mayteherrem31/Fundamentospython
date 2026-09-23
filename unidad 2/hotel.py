#Se crea una funcion llamada hotel,aqui vamos a hacer el sistema de las reselvaciones del mismo

    habitaciones = {}

#Usamos la estructura diccionario, donde se almacenan las hbaitaciones de cama individuales y dobles disponibles

habitaciones = {"individual": 3, "doble": 2}


#Usamos un while para dejar ciclos infinitos, que nos permitiran usar las veces que queramos el sistema

while True


#Declaramos una variable como entrada de valor, donde se guardara el mismo

accion = input("¿Reservar o liberar?")


#Con las variables anteriores se ocupara un Match que nos permita escoger una acción entre reservar y o liberar

match accion:
    case "reservar"


#Para reservar pedimos que tipo de habitación quiere el cliente y se almacena en una variable 

print ("que tipo de habitación es")
tipo = input("Tipo: ")


#Se ocupa una condición if para preguntar si el tipo de habitación se encuentra en el diccionario "habitaciones"
#y si la cantidad es mayor a 0

if tipo in habitaciones and habitaciones[tipo] > 0:


#Cuando se cumpla la condición se le restará -1 a la cantidad del tipo de habitacion que se escogio y se mandara 
#mensaje que su habitación fue reservada

