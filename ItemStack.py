#0: TestItem
#1: Pokeball(empty)
#2: Pokeball(metadata)
#3:
#4:

class ItemStack:
    def __init__(self, id, amount, metadata):
        self.amount = amount
        self.id = id
        self.metadata = metadata
        
        if(id == 0):
            self.name = "TestItem"
        if(id == 1):
            self.name = "Pókeball(Empty)"
        if(id == 2):
            self.name = "Banana"

    def __str__(self):
        return self.name + " Amount: " +str(self.amount)
