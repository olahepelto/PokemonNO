class Inventory:
    def __init__(self, max_size):
        self.items = []
        self.max_size = max_size

    def __str__(self):
        backpack_str = "Backpack: \n"
        for item in self.items:
            backpack_str += str(item) + "\n"
        return backpack_str

    def get_stack(self, id):
        for inv_stack in self.items:
            if(hasattr(inv_stack, 'id')):
                if(inv_stack.id == id):
                    return inv_stack
        return False

    def set_stack(self, id, amount):
        
        stack = self.get_stack(id)
        ind = self.items.index(stack)
        
        self.items[ind].amount = amount
        if(amount == 0):
            self.items.pop(ind)

    def new_stack(self, stack):
        if(self.get_stack(id) == False):
            self.items.append(stack)
            return
        
        stack = self.get_stack(id)
        ind = self.items.index(stack)
        
        self.items[ind].amount = amount
        if(amount <= 0):
            self.items.pop(ind)

    def add_pokemon(self, pokemon):
        self.items.append(pokemon)
