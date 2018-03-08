from Inventory import Inventory

class Player:
    def __init__(self, curr_place_id):
        self._id = curr_place_id
        self.x = 20
        self.y = 20
        self.inv = Inventory(20)

    def get_place_id(self,x,y):
        return

    def goto(self, dir):
        if(dir == "w"):
            self.x -= 1
        if(dir == "e"):
            self.x += 1
        if(dir == "s"):
            self.y -= 1
        if(dir == "n"):
            self.y += 1
