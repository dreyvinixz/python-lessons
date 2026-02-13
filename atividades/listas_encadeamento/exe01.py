class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def count_elements(self):
        count = 0
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.next
        return count
    
def main():
    linked_list = LinkedList()
    num_elements = int(input("Digite o número de elementos da lista encadeada: "))
    for _ in range(num_elements):
        data = int(input("digite o elemento: "))
        linked_list.append(data)
    print("Número de elementos na lista encadeada:", linked_list.count_elements())

if __name__ == "__main__":
    main()
