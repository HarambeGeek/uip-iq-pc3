print("Bienvenido al programa de temperaturas;")
far = int(input("Ingrese la temp. en F para transformarla a C: "))
celcius = ((far - 32)*(5/9))
if celcius > 100:
    print("La temperatura en Cº es de " + str(celcius) + " , esta caliente")
elif celcius < 0:
    print("La temperatura en Cº es de " + str(celcius) + " , hace frío")
else:
    print("La temperatura en Cº es de " + str(celcius))