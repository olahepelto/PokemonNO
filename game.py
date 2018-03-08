from Player import Player
from ItemStack import ItemStack
from MapSquare import MapSquare
from Map import Map
from HelperFunc import *
from Pokemon import Pokemon
import random


ascii_art()

player = Player(0);
map = Map(40, 40); #40x40 Map size

player.inv.new_stack(ItemStack(1,10,0))
player.inv.new_stack(ItemStack(2,10,0))

idk_phrases = ["wtf does {0} mean?", "i'm not quite sure what you mean by {0}", "are you crazy! I can't do {0}", "i dont know how to say this but.. {0} doesn't mean anything", "Talking gibberish is a sign of impending mental collapse", "That doesn't make any sense","next time, try to say something useful","No!","I don't agree"] #0->8
while True:
    cmd = input("> ")
    if cmd == "exit":
        print("Bye")
        break
    elif cmd == "pack":
        print(inv)
    elif cmd == "help":
        print_help()
    elif cmd.startswith("go"):
        player.goto(cmd.split(" ")[1])
        map.draw(player)
    elif cmd.split(" ")[0] == "catch":
        map.catch_pokemon(player)
        
    elif cmd == "n" or cmd == "w" or cmd == "e" or cmd == "s":
        player.goto(cmd)
        map.draw(player)
    elif cmd == "map":
        map.draw(player)
    elif cmd == "inv":
        print("\n"*40) 
        print(str(player.inv))
    elif cmd == "splash":
        ascii_art()
    elif cmd == "clear":
        clear()
    elif cmd == "save":
        save()
    elif cmd == "load":
        load()
    elif cmd.startswith("§"):
        print("What do you want to do?")
        print("1. Item")
        print("2. Pókemon")
        print("...back")

        choice = input()
        if choice == "2":
            print("{id,health,power}")
            cmd = input()
            player.inv.add_pokemon(Pokemon(int(cmd.split(" ")[0]),int(cmd.split(" ")[1]),int(cmd.split(" ")[2])))
        if choice == "1": 
            print("{id,amount,metadata}")
            cmd = input()          
            player.inv.new_stack(ItemStack(int(cmd.split(" ")[0]),int(cmd.split(" ")[1]),int(cmd.split(" ")[2])))
    else:
        print(idk_phrases[random.randint(0,8)].format(cmd))
