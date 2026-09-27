# Abro y leo el archivo1.txt
archivo1 = open("archivo1.txt", "r")

# Abro y leo el archivo2.txt
archivo2 = open("archivo2.txt", "r")

# Abro archivo con readlines archivo1.txt para que me quede una lista así:
# ['a\n', 'b\n', 'c\n']
lineas1 = archivo1.readlines()

# Abro archivo con readlines archivo2.txt para que me quede una lista así:
# ['a\n', 'a\n', 'c\n']
lineas2 = archivo2.readlines()

archivo1.close()
archivo2.close()

# Estoy creando el archivo3.txt
resultados = open("resultados.txt", "w")
suma = 0
for i in range(len(lineas1)):
    respuestaEstudiante = lineas1[i].strip()
    respuestaCorrecta = lineas2[i].strip()

    if respuestaEstudiante == respuestaCorrecta:
        resultados.write("1\n")
        suma = suma + 1
    else:
        resultados.write("0\n")

resultados.write(str(suma))
resultados.write("\n")
resultados.close()
print("resultados.txt generado correctamente")