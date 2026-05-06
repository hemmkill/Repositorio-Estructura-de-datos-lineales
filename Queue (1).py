class Fila:

    def __init__(self, datos_iniciales=[]):
        self.elementos = []

        for valor in datos_iniciales:
            self.encolar(valor)


    def __str__(self):
        if len(self.elementos) == 0:
            return "Fila vacia"

        cadena = ""
        contador = 0

        while contador < len(self.elementos):
            cadena = cadena + str(self.elementos[contador])

            if contador != len(self.elementos) - 1:
                cadena = cadena + " <- "

            contador = contador + 1

        return cadena


    def __len__(self):
        return len(self.elementos)


    def esta_vacia(self):
        return len(self.elementos) == 0


    def primero(self):
        if self.esta_vacia():
            return None

        return self.elementos[0]


    def __iter__(self):
        indice = 0

        while indice < len(self.elementos):
            yield self.elementos[indice]
            indice = indice + 1


    def __contains__(self, numero):
        for dato in self.elementos:
            if dato == numero:
                return True

        return False


    def encolar(self, numero):
        self.elementos.append(numero)


    def desencolar(self):
        if self.esta_vacia():
            raise IndexError("No hay elementos en la fila")

        return self.elementos.pop(0)


fila_principal = Fila()

print("Estado inicial de la fila:")
print(fila_principal)

fila_principal.encolar(100)
fila_principal.encolar(200)
fila_principal.encolar(300)

print("Despues de encolar 100, 200 y 300:")
print(fila_principal)

print("Primer elemento de la fila:")
print(fila_principal.primero())

print("Elemento eliminado:")
print(fila_principal.desencolar())

print("Fila actual:")
print(fila_principal)

print("Cantidad de elementos:")
print(len(fila_principal))

print("¿El numero 200 esta en la fila?")
print(200 in fila_principal)