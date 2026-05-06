class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None


class ListaCircular:

    def __init__(self, elementos_iniciales=None):
        self.cabeza = None
        self.tamano = 0

        if elementos_iniciales:
            for e in elementos_iniciales:
                self.append(e)

    def __str__(self):
        if not self.cabeza:
            return "Empty"

        resultado = ""
        actual = self.cabeza

        for i in range(self.tamano):
            resultado += str(actual.valor)
            if i < self.tamano - 1:
                resultado += " -> "
            actual = actual.siguiente

        return resultado

    def __len__(self):
        return self.tamano

    def __getitem__(self, idx):
        if idx < 0 or idx >= self.tamano:
            raise IndexError("Index does not exist")

        actual = self.cabeza
        for _ in range(idx):
            actual = actual.siguiente

        return actual.valor

    def isEmpty(self):
        return self.tamano == 0

    def __iter__(self):
        actual = self.cabeza
        for _ in range(self.tamano):
            yield actual.valor
            actual = actual.siguiente

    def __contains__(self, elemento):
        actual = self.cabeza
        for _ in range(self.tamano):
            if actual.valor == elemento:
                return True
            actual = actual.siguiente
        return False

    def append(self, elemento):
        nuevo = Nodo(elemento)

        if not self.cabeza:
            self.cabeza = nuevo
            nuevo.siguiente = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente != self.cabeza:
                actual = actual.siguiente

            actual.siguiente = nuevo
            nuevo.siguiente = self.cabeza

        self.tamano += 1

    def add(self, indice, elemento):
        if indice < 0 or indice > self.tamano:
            raise IndexError("Index does not exist")

        nuevo = Nodo(elemento)

        if indice == 0:
            if not self.cabeza:
                self.cabeza = nuevo
                nuevo.siguiente = nuevo
            else:
                ultimo = self.cabeza
                while ultimo.siguiente != self.cabeza:
                    ultimo = ultimo.siguiente

                nuevo.siguiente = self.cabeza
                ultimo.siguiente = nuevo
                self.cabeza = nuevo
        else:
            actual = self.cabeza
            for _ in range(indice - 1):
                actual = actual.siguiente

            nuevo.siguiente = actual.siguiente
            actual.siguiente = nuevo

        self.tamano += 1

    def remove(self, elemento):
        if not self.cabeza:
            raise ValueError("Element does not exist")

        actual = self.cabeza
        anterior = None

        for _ in range(self.tamano):
            if actual.valor == elemento:
                if anterior is None:
                    ultimo = self.cabeza
                    while ultimo.siguiente != self.cabeza:
                        ultimo = ultimo.siguiente

                    self.cabeza = self.cabeza.siguiente
                    ultimo.siguiente = self.cabeza
                else:
                    anterior.siguiente = actual.siguiente

                self.tamano -= 1
                return

            anterior = actual
            actual = actual.siguiente

        raise ValueError("Element does not exist")

    def pop(self, indice):
        if indice < 0 or indice >= self.tamano:
            raise IndexError("Index does not exist")

        actual = self.cabeza
        anterior = None

        for _ in range(indice):
            anterior = actual
            actual = actual.siguiente

        dato = actual.valor

        if anterior is None:
            ultimo = self.cabeza
            while ultimo.siguiente != self.cabeza:
                ultimo = ultimo.siguiente

            self.cabeza = self.cabeza.siguiente
            ultimo.siguiente = self.cabeza
        else:
            anterior.siguiente = actual.siguiente

        self.tamano -= 1
        return dato

    def clear(self):
        self.cabeza = None
        self.tamano = 0


# PRUEBA (igual comportamiento)
lista = ListaCircular()

print("Lista inicial:")
print(lista)

lista.append(10)
lista.append(20)
lista.append(30)

print("Despues de append:")
print(lista)

lista.add(1, 15)

print("Despues de add en posicion 1:")
print(lista)

lista.remove(20)

print("Despues de remove 20:")
print(lista)

print("Pop indice 1:")
print(lista.pop(1))

print("Lista final:")
print(lista)

print("Tamaño:")
print(len(lista))