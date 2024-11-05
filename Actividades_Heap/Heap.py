

class HeapMax():
    # crea un monticulo

    def __init__(self):
        # crea el vector vacio para el monticulo
        self.elements = []
    
    #___________________________________________________________

    def add(self, value):
        # agrega un dato al monticulo
        self.elements.append(value)
        self.float(len(self.elements)-1)

    def remove(self):
        # quita un elemento de la cima
        if len(self.elements) > 0:
            self.interchange(0, len(self.elements)-1)
            value = self.elements.pop()
            self.sink(0)
            return value
        else:
            return None

    def interchange(self, index_1, index_2):
        # intercambia elementos, index1 por index2
        self.elements[index_1], self.elements[index_2] = self.elements[index_2], self.elements[index_1]

    def float(self, index):
        # flota el elemento en la posicion index
        father = (index-1) // 2
        while index > 0 and self.elements[index] > self.elements[father]:
            self.interchange(index, father)
            index = father
            father = (index-1) // 2

    def sink(self, index):
        # hunde el elemento en la posicion index
        left_child = (index * 2) + 1
        control = True
        while control and left_child < len(self.elements):
            right_child = (index * 2) + 2
            max = left_child
            if right_child < len(self.elements):
                if self.elements[right_child] > self.elements[left_child]:
                    max = right_child
            if self.elements[index] < self.elements[max]:
                self.interchange(index, max)
                index = max
                left_child = (index * 2) + 1
            else:
                control = False

    def heapify(self, elements):
        # transforma una vector (lista) en un monticulo, "monticulizar".
        self.elements = elements
        for i in range(len(self.elements)):
            self.float(i)

    def sort(self):
        # ordena el monticulo
        result = []
        amount_elements = len(self.elements)
        for i in range(amount_elements):
            value = self.remove()
            result.append(value)
        return result
    
    def arrive(self, value, priority):
        # Agrega el elemento al final del montículo 
        # y luego lo flota según su criterio de prioridad, 
        # para utilizarlo como cola de prioridad.
        self.add([priority, value])

    def atention(self):
        # Elimina y devuelve el elemento almacenado en la cima del montículo, 
        # utilizado como cola de prioridad.
        return self.remove()

    def change_proirity(self, index, new_priority):
        # Cambia la prioridad de un elemento del montículo 
        # y lo flota o hunde según corresponda.
        if index < len(self.elements):
            previous_priority = self.elements[index][0]
            self.elements[index][0] = new_priority
            if new_priority > previous_priority:
                self.float(index)
            elif new_priority < previous_priority:
                self.sink(index)


class HeapMin():

    def __init__(self):
        self.elements = []
    
    def add(self, value):
        self.elements.append(value)
        self.float(len(self.elements)-1)

    def remove(self):
        if len(self.elements) > 0:
            self.interchange(0, len(self.elements)-1)
            value = self.elements.pop()
            self.sink(0)
            return value
        else:
            return None

    def interchange(self, index_1, index_2):
        self.elements[index_1], self.elements[index_2] = self.elements[index_2], self.elements[index_1]

    def float(self, index):
        father = (index-1) // 2
        while index > 0 and self.elements[index] < self.elements[father]:
            self.interchange(index, father)
            index = father
            father = (index-1) // 2

    def sink(self, index):
        left_child = (index * 2) + 1
        control = True
        while control and left_child < len(self.elements):
            right_child = (index * 2) + 2
            min = left_child
            if right_child < len(self.elements):
                if self.elements[right_child] < self.elements[left_child]:
                    min = right_child
            if self.elements[index] > self.elements[min]:
                self.interchange(index, min)
                index = min
                left_child = (index * 2) + 1
            else:
                control = False

    def heapify(self, elements):
        self.elements = elements
        for i in range(len(self.elements)):
            self.float(i)

    def sort(self):
        result = []
        amount_elements = len(self.elements)
        for i in range(amount_elements):
            value = self.remove()
            result.append(value)
        return result


    def arrive(self, value, priority):
        self.add([priority, value])

    def atention(self):
        return self.remove()

    def change_proirity(self, index, new_priority):
        if index < len(self.elements):
            previous_priority = self.elements[index][0]
            self.elements[index][0] = new_priority
            if new_priority < previous_priority:
                self.float(index)
            elif new_priority > previous_priority:
                self.sink(index)



