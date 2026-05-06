class Torre:

    def __init__(self, valores_iniciales=[]):
        self.items = []

        for dato in valores_iniciales:
            self.agregar(dato)


    def __str__(self):
        if len(self.items) == 0:
            return "Sin elementos"

        resultado = ""
        posicion = 0

        while posicion < len(self.items):
            resultado = resultado + str(self.items[posicion])

            if posicion != len(self.items) - 1:
                resultado = resultado + " | "

            posicion = posicion + 1

        return resultado


    def __len__(self):
        return len(self.items)


    def vacia(self):
        return len(self.items) == 0


    def ultimo(self):
        if self.vacia():
            return None

        return self.items[len(self.items) - 1]


    def __iter__(self):
        indice = 0

        while indice < len(self.items):
            yield self.items[indice]
            indice = indice + 1


    def __contains__(self, valor):
        for elemento in self.items:
            if elemento == valor:
                return True

        return False


    def agregar(self, valor):
        self.items.append(valor)


    def eliminar(self):
        if self.vacia():
            raise IndexError("La estructura esta vacia")

        return self.items.pop()


torre_datos = Torre()

print("Estado inicial:")
print(torre_datos)

torre_datos.agregar(5)
torre_datos.agregar(15)
torre_datos.agregar(25)

print("Luego de agregar 5, 15 y 25:")
print(torre_datos)

print("Elemento superior:")
print(torre_datos.ultimo())

print("Elemento eliminado:")
print(torre_datos.eliminar())

print("Estado actual:")
print(torre_datos)

print("Cantidad de datos:")
print(len(torre_datos))

print("¿El numero 5 esta en la estructura?")
print(5 in torre_datos)