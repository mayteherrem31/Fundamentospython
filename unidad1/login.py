# Número de intentos disponibles
intentos = 3

print("\n--- Sistema de inicio de sesion ---")

print(f"Intentos restantes {intentos}")

print("\nUsuario:")
usuario=input()

print("\nPassword:")
password = input()

# Primer intento
if usuario == "admin" and password == "1234":
    print("Usuario válido")
else:
    print("Usuario inválido")
    intentos = intentos - 1

# Segundo intento
if intentos == 2 :
    print(f"Intentos restantes {intentos}")
    print("\nUsuario:")
    usuario = input()
    print("\nPassword:")
    password = input()
    if usuario == "admin" and password =="1234":
        print("Usuario válido")
    else:
        print("Usuario invalido")
        intentos = intentos - 1

if intentos == 1:
    print(f"Intentos restantes {intentos}")
    print("\nUsuario:")
    usuario = input()
    print("\nPassword:")
    password = input()
    if usuario == "admin" and password =="1234":
        print("Usuario válido")
    else:
        print("Usuario invalido")
        intentos = intentos - 1

# Se bloquea cuenta
if intentos == 0:
    print("\nCuenta bloqueada")
