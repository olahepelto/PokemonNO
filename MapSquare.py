class MapSquare:
    def __init__(self, type):
        self.type_id = type
        if(type == 0):
            self.type = " "
        if(type == 1):
            self.type = "T"
        if(type == 2):
            self.type = "G"
        if(type == 3):
            self.type = "F"
        if(type == 4):
            self.type = "H"
        if(type == 5):
            self.type = "C"
        if(type == 6):
            self.type = "L"

    def __str__(self):
        return self.type
