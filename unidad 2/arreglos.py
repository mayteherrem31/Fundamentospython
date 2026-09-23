asientos_cine = ["Adriana", "Alberto", "Alejandro", "Angeles", "Angelina", "", 4]

print("Array Unidemencional - Notas de estudiantes:")
print(notas_estudiante)

#Recorrido del Array con for
print("/nRecorrido del array:")
for i, nota in enumerate(notas_estudiante):
    print(f"Estudiante {i+1}: {nota}")
