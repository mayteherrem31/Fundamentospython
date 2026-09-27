archivo = open("archivo.txt", "r")

for linea in archivo:
    print(linea.strip())

archivo.close()