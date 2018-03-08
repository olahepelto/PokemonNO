from MapSquare import MapSquare
from Pokemon import Pokemon
import random
import copy

#   id 0 empty 12
#T  id 1 smallTown 1
#G   id 2 tallGrass 2
#F   id 3 forest 4
#H   id 4 lonelyHouse 2
#C   id 5 cave 1
#L   id 6 lake 3
#X = PLAYER
#yht 25


class Map:
    def __init__(self, x_size, y_size):
        self.x_size = x_size
        self.y_size = y_size
        self.map_squares = []        
        self.awful_thing = [MapSquare(0),MapSquare(0),MapSquare(0),MapSquare(0),MapSquare(0),MapSquare(0),MapSquare(0),MapSquare(0),MapSquare(0),MapSquare(0),MapSquare(0),MapSquare(0),MapSquare(0),MapSquare(0),MapSquare(0),MapSquare(0),MapSquare(0),MapSquare(0),MapSquare(0),MapSquare(0),MapSquare(0),MapSquare(0),MapSquare(1),MapSquare(2),MapSquare(2),MapSquare(3),MapSquare(3),MapSquare(3),MapSquare(3),MapSquare(4),MapSquare(4),MapSquare(5),MapSquare(6),MapSquare(6),MapSquare(6)]

        for x in range(0, self.x_size):
            for y in range(0, self.y_size):
                self.map_squares.append(MapSquare(self.awful_thing[random.randint(0,34)].type_id))
                self.map_squares[-1].x = x
                self.map_squares[-1].y = y


    def catch_pokemon(self, player):
        if self.find_square(player.x, player.y).type == "G":
            found_pokemon = Pokemon(random.randint(0,4),random.randint(0,400) + 100,random.randint(0,400) + 100)    
            xp_level = found_pokemon.health * found_pokemon.power
            
            while(True):
                print("do you want to throw a pókeball? (y/n) def: y")
                if input() != "n":
                    if player.inv.get_stack(1) != False:
                        player.inv.set_stack(1,player.inv.get_stack(1).amount - 1)
                        success = random.randint(0,xp_level)
                        if(success < 30000):                           
                            player.inv.add_pokemon(found_pokemon)
                            print("\"Gotcha!\"")                        
                            break
                    else:
                        print("You don't have any pókeballs")
                        print("Get some more in the premium store only 5.99€ for 10")
                        break
                else:
                    print("Why didn't you catch the pokemon? Well, maybe next time.")   
                    break     
        else:
            print("Where do you see a pókemon?")

    def find_square(self, x, y):
        for square in self.map_squares:
            if(x == square.x and y == square.y):
                return square
        return MapSquare(0)

    def draw(self, player):
        print("\n" * 40);
        print("You are standing in x: " + str(player.x) + " y: " + str(player.y))
        print("_____________________" + " X = Player")
        print("│ {0} │ {1} │ {2} │ {3} │ {4} │".format(self.find_square(player.x-2,player.y+2),self.find_square(player.x-1,player.y+2),self.find_square(player.x,player.y+2),self.find_square(player.x+1,player.y+2),self.find_square(player.x+2,player.y+2)) + " T = Small Town")
        print("│___│___│___│___│___│" + " G = Grass")
        print("│ {0} │ {1} │ {2} │ {3} │ {4} │".format(self.find_square(player.x-2,player.y+1),self.find_square(player.x-1,player.y+1),self.find_square(player.x,player.y+1),self.find_square(player.x+1,player.y+1),self.find_square(player.x+2,player.y+1)) + " F = Forest")
        print("│___│___│___│___│___│" + " H = House")
        print("│ {0} │ {1} │ {2} │ {3} │ {4} │".format(self.find_square(player.x-2,player.y),self.find_square(player.x-1,player.y),"X",self.find_square(player.x+1,player.y),self.find_square(player.x+2,player.y)) + " C = Cave")
        print("│___│___│___│___│___│" + " L = Lake")
        print("│ {0} │ {1} │ {2} │ {3} │ {4} │".format(self.find_square(player.x-2,player.y-1),self.find_square(player.x-1,player.y-1),self.find_square(player.x,player.y-1),self.find_square(player.x+1,player.y-1),self.find_square(player.x+2,player.y-1)))
        print("│___│___│___│___│___│")
        print("│ {0} │ {1} │ {2} │ {3} │ {4} │".format(self.find_square(player.x-2,player.y-2),self.find_square(player.x-1,player.y-2),self.find_square(player.x,player.y-2),self.find_square(player.x+1,player.y-2),self.find_square(player.x+2,player.y-2)))
        print("│___│___│___│___│___│")
