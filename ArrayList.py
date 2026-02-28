class ArrayList:

    # size: initial capacity of the collection
    # initial_elements: allow the collection to start with some elements
    def __init__(self, size=4, initial_elements=None):
        if size <= 0:
            raise ValueError("Initial capacity must be greater than 0")

        self._capacity = size
        self._count = 0
        self._data = [None] * self._capacity

        if initial_elements:
            for element in initial_elements:
                self.append(element)

    # return a str of the collection
    def __str__(self):
        return "[" + ", ".join(str(self._data[i]) for i in range(self._count)) + "]"

    # return the length of the elements in the collection
    def __len__(self):
        return self._count

    # return a boolean that implies if the collection is empty or not
    def isEmpty(self):
        return self._count == 0

    # return the element of the collection in the index position
    # Error: the index dont exist
    def getitem(self, index):
        if index < 0:
            index = self._count + index

        if index < 0 or index >= self._count:
            raise IndexError("Index out of range")

        return self._data[index]

    # allow the collection to be called in a for loop
    def __iter__(self):
        for i in range(self._count):
            yield self._data[i]

    # return a boolean value representing the existence of an element in the collection
    def __contains__(self, element):
        for i in range(self._count):
            if self._data[i] == element:
                return True
        return False

    # internal method to resize the array
    def _resize(self):
        new_capacity = int(self._capacity * 1.125) + 4
        if new_capacity <= self._capacity:
            new_capacity = self._capacity + 4

        new_data = [None] * new_capacity

        for i in range(self._count):
            new_data[i] = self._data[i]

        self._data = new_data
        self._capacity = new_capacity

    # add the element to the end of the collection
    def append(self, element):
        if self._count == self._capacity:
            self._resize()

        self._data[self._count] = element
        self._count += 1

    # add the element to the collection at the requested index
    # Error: non existing index in the collection
    def insert(self, index, element):
        if index < 0 or index > self._count:
            raise IndexError("Index out of range")

        if self._count == self._capacity:
            self._resize()

        for i in range(self._count, index, -1):
            self._data[i] = self._data[i - 1]

        self._data[index] = element
        self._count += 1

    # remove an element in the collection by its value
    # Error: the element dont exist in the collection
    def remove(self, element):
        for i in range(self._count):
            if self._data[i] == element:
                for j in range(i, self._count - 1):
                    self._data[j] = self._data[j + 1]

                self._data[self._count - 1] = None
                self._count -= 1
                return

        raise ValueError("Element not found")

    # remove and return the element in the collection by its index
    def pop(self, index):
        if index < 0 or index >= self._count:
            raise IndexError("Index out of range")

        removed = self._data[index]

        for i in range(index, self._count - 1):
            self._data[i] = self._data[i + 1]

        self._data[self._count - 1] = None
        self._count -= 1

        return removed

    # remove all elements in the collection
    def clear(self):
        self._data = [None] * self._capacity
        self._count = 0



#  BLOQUE DE PRUEBA

if __name__ == "__main__":

    lista = ArrayList(size=4)

    lista.append(10)
    lista.append(20)
    lista.append(30)

    print("Lista inicial:", lista)
    print("Tamaño:", len(lista))

    lista.insert(1, 15)
    print("Después de insertar 15 en índice 1:", lista)

    lista.remove(20)
    print("Después de eliminar 20:", lista)

    print("Elemento en índice 1:", lista.getitem(1))

    print("¿Existe 30 en la lista?", 30 in lista)

    print("Elemento eliminado con pop:", lista.pop(1))
    print("Lista después del pop:", lista)

    lista.clear()
    print("Lista después de clear:", lista)
    print("Tamaño final:", len(lista))