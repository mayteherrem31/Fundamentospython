import pandas as pd

# 1. LEER LOS ARCHIVOS

# Leemos el archivo con las respuestas de los estudiantes
df_estudiantes = pd.read_csv("respuestas_estudiantes.csv")

# Leemos el archivo con las respuestas correctas
df_correctas = pd.read_excel("respuestas_correctas.xlsx")

# 2. OBTENER LAS PREGUNTAS Y LAS RESPUESTAS CORRECTAS

# Obtenemos la columna "Pregunta"
preguntas = df_correctas["Pregunta"].values

# 3. CREAR EL DICCIONARIO DE RESPUESTAS CORRECTAS

clave_respuestas = {}

for i in range(df_correctas.shape[0]):
    pregunta = df_correctas["Pregunta"].iloc[i]
    respuesta = df_correctas["Respuesta"].iloc[i]
    clave_respuestas[pregunta] = respuesta

# 4. CREAR LA COLUMNA PUNTUACIÓN

# Creamos una nueva columna llamada "Puntuación"
# Todos los estudiantes comienzan con 0 puntos
df_estudiantes["Puntuación"] = 0

# 5. COMPARAR CADA PREGUNTA Y ACUMULAR PUNTOS

for pregunta in preguntas:
    respuesta_correcta = clave_respuestas[pregunta]

    puntos = (
        df_estudiantes[pregunta] == respuesta_correcta
    ).astype(int)

    df_estudiantes["Puntuación"] = (
        df_estudiantes["Puntuación"] + puntos
    )

# 6. MOSTRAR LOS RESULTADOS

print(df_estudiantes[["Nombre", "Puntuación"]])

# 7. ORDENAR Y GUARDAR LOS RESULTADOS

df_resultados = df_estudiantes.sort_values("Puntuación", ascending=False)

# 8. GUARDAR EL ARCHIVO FINAL

df_resultados.to_csv("resultados_examen.csv", index=False)

print("Resultados guardados en resultados_examen.csv")

