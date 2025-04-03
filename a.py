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
        
    # Função para remover um elemento em uma posição específica
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
        

#implementacao de uma pilha em Python
class PersonalStack:
    list = PersonalArray()
    
    #Funcao que insere um elemento na posicao 0 da nossa pilha
    def push(self, newElement):
        self.list.insertAt(0, newElement)
    
    #Funcao que remove um elemento da pilha (no caso sempre a ultima posicao)   
    def pop(self):
        return self.list.removePosition(0)

#implementacao de uma fila em Python
class PersonalQueue:
    list = PersonalArray()
    
    #Funcao que insere um elemento na posicao 0 da nossa fila
    def enqueue(self, newElement):
        self.list.insertAt(0, newElement)
    
    #Funcao que remove um elemento da fila (no caso sempre a ultima posicao)   
    def dequeue(self):
        return self.list.removePosition(self.list.size() - 1)
        

#Cria uma instancia do objeto da fila que implementamos
queue = PersonalQueue();
		
#Enfileirando elementos na estutura de dados
queue.enqueue("1");
queue.enqueue("2");
queue.enqueue("3");
queue.enqueue("4");
queue.enqueue("5");
		
#Desenfileira os elementos inseridos na estrutura de dados e imprime
print( queue.dequeue() );
print( queue.dequeue() );
print( queue.dequeue() );
print( queue.dequeue() );
print( queue.dequeue() );
		
#Cria ou instancia um objeto da fila que implementamos
stack = PersonalStack()

#Empilhando elementos na estutura de dados
stack.push("1")
stack.push("2")
stack.push("3")
stack.push("4")
stack.push("5")

#Desempilha os elementos inseridos na estrutura de dados e imprime
print( stack.pop() )
print( stack.pop() )
print( stack.pop() )
print( stack.pop() )
print( stack.pop() )
