import string
import random

longitud = int(input("ingrese el tamaño de la contraseña: "))

caracteres = string.ascii_letters + string.digits + string.punctuation
## la variable caracteres me genera 10 caracteres, en orden del abecedarios  minusculas + mayusculas + numeros y por ultimo simbolos
## respectivamente son longitud en minisculas , mayusculas , numero y simbolos
contraseña = "".join(random.choice(caracteres) for i in range(longitud))

print("La contraseña generada es: " + contraseña)