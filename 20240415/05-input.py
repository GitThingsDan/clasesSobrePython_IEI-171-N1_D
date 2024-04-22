# ENVIAR correo electrónico al profesor, con la respuesta a la pregunta: "¿Cómo hacer que input acepte floats sin que tire error?". ¡5 décimas AL PRIMER POSTOR! (Pista: al parecer, tiene que ver con que ".isdecimal()" SÍ existe, pero aplica sólo para strings.)

# numero = int(input("Ingrese un número: ")) # "casting"
numero = input("Ingrese un número: ")
print(type(numero))
if(numero.isnumeric()): # ¡¡¡NUEVO!!! Verifica si el string es un string que contiene sólo caracteres numéricos (y, por tanto, si es "casteable" a entero).
    numero = int(numero)
    print(numero > 18)
    print("El número ingresado es:", numero)
    mult = numero * 3
    print("La multiplicación de", numero, "x 3 es:", mult)
else: 
    print(numero, "no es un número.")