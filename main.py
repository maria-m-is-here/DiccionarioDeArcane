import random

caracteres = "+-/*!&$#?=@abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
longitud = int(input("Introduzca el tamaño de la contraseña:"))
contraseña = ""

for i in range(longitud):
    contraseña += random.choice(caracteres)

print("Tu contraseña segura es:", contraseña)



