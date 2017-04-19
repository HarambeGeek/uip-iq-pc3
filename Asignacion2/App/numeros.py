
#Falta hacer clase de pruebas unitarias.

class numeros:
    numero = 0

    def __init__(self,num):
        self.numero = num


    def parImpar(self):
        if (self.numero % 2) == 0:
           #print("El número es par\n")
            return 0
        else:
            #print("El número es impar\n")
            return 1



