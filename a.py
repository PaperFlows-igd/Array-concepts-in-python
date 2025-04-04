#Criando um array de 5 posicoes vazias
class PersonalArray:
    SIZE = 5
    insertPosition = 0
    elements = [None] * SIZE

    # Função que serve para definir se o array está vazio ou não
    def isEmpty(self):
        return self.size() == 0
    
    # Função que serve para retornar o número de elementos já armazenados no array
    def size(self):
        return self.insertPosition
        
    # Função que serve para definir se precisamos de mais memória
    def isMemoryFull(self):
        return self.insertPosition == len(self.elements)
    
    # Função para inserir um novo elemento na lista
    def append(self, newElement):
        if self.isMemoryFull():
            self.updateMemory()
        self.elements[self.insertPosition] = newElement
        self.insertPosition += 1
    
    # Função para aumentar a memória quando necessário
    def updateMemory(self):
        newArray = [None] * (self.size() + self.SIZE)
        for position in range(self.insertPosition):  # Correção: iterar até self.insertPosition
            newArray[position] = self.elements[position]
        self.elements = newArray
    
    # Função para limpar o array
    def clear(self):
        self.elements = [None] * self.SIZE  # Simplificação
        self.insertPosition = 0
    
    # Função para remover o último elemento
    def remove(self):
        if not self.isEmpty():
            self.elements[self.insertPosition - 1] = None
            self.insertPosition -= 1
    
    # Função para remover um elemento em uma posição específica
    def removePosition(self, position):
        if position < 0 or position >= self.insertPosition:
            print("Posição inválida!")
            return ""
        removedElement = self.elements[position]
        index = position
        while index < self.insertPosition - 1:  
            self.elements[index] = self.elements[index+1]
            index += 1
        self.insertPosition -= 1
        return removedElement
        
    # Função para inserir+ um elemento em uma posição específica
    def insertAt(self, position, newElement):
        if position < 0 or position > self.insertPosition:
            print("Posição inválida!")
            return
        if self.isMemoryFull():
            self.updateMemory()
        index = self.insertPosition - 1
        while index >= position:  
            self.elements[index + 1] = self.elements[index]
            index -= 1
        self.elements[position] = newElement
        self.insertPosition += 1   
        
    
    # Função para retornar um elemento em uma posição específica
    def elementAt(self, position):
        if position < 0 or position >= self.insertPosition:
            print("Posição inválida!")
            return None
        return self.elements[position]
        

#implementacao de uma fila em Python
class PersonalQueue:
    list = PersonalArray()
    
    #Funcao que insere um elemento na posicao 0 da nossa fila
    def enqueue(self, newElement):
        self.list.insertAt(0, newElement)
    
    #Funcao que remove um elemento da fila (no caso sempre a ultima posicao)   
    def dequeue(self):
        return self.list.removePosition(self.list.size() - 1)
        

class MedicalOffice:
    def __init__(self):
        self.queue = PersonalQueue()
    
    def checkIn(self, patientName):
        print(f"{patientName} chegou ao consultório e entrou na fila.")
        self.queue.enqueue(patientName)
    
    def callNext(self):
        if self.queue.list.isEmpty():
            print("Nenhum paciente na fila!")
        else:
            nextPatient = self.queue.dequeue()
            print(f"Chamando {nextPatient} para atendimento.")
    
    def showQueue(self):
        if self.queue.list.isEmpty():
            print("Fila vazia.")
        else:
            print("Pacientes na fila:", [self.queue.list.elementAt(i) for i in range(self.queue.list.size())])


consultorio = MedicalOffice()
consultorio.checkIn("Alice")
consultorio.checkIn("Bob")
consultorio.checkIn("Carlos")
consultorio.showQueue()
consultorio.callNext()
consultorio.showQueue()
consultorio.callNext()
consultorio.showQueue()
consultorio.callNext()
consultorio.callNext()
