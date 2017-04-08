from App.numeros import numeros

if __name__ == "__main__":
    x = int(input("Ingrese el número que desea evaluar: \n"))
    pi = numeros(x)
    pi.parImpar()