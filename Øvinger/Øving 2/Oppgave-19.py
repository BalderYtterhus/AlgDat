class Queue:

    def __init__(self, max_size):
        # Initialiser de underliggende datastrukturene her
        self.max_size = max_size

        self.queue = [None] * max_size # Tom liste som skal være køen
        self.head = 0 # Indekser for head og tail 
        self.tail = 0
        self.count = 0


    def enqueue(self, value):
        # Skriv kode for Enqueue operasjonen
        if self.count < self.max_size:
            self.queue[self.tail] = value
            self.tail = (self.tail + 1) % self.max_size
            self.count += 1
        else:
            print(f"OVERFLOW")

        # Setter tail 

    def dequeue(self):
        # Skriv kode for Dequeue operasjonen
        if self.count > 0:
            x = self.queue[self.head]
            self.head = (self.head + 1) % self.max_size
            self.count -= 1
            return x
        else: 
            print(f"UNDERFLOW")


highscore = True