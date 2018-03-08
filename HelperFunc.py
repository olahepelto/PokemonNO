def print_help():
    clear()   
    print("map           :View Map  \n"
          "n,w,e,s       :Move around the map  \n"
          "catch         :Catch pokemon (have to be standing in tall grass)  \n"
          "inv           :Inventory  \n"
          "§             :Cheats  \n"
          "clear         :Clears screen\n"
          "open(WIP)     :Open Savegame\n"
          "save(WIP)     :Save Game\n"
          "splash        :Back to the fancy ascii art\n"
          "exit          :Exit game\n"
          "help          :What do you think?\n")

def ascii_art():
    clear()
    print("             _                                               _  \n"+
      "            | |                                             | | \n"+
      " _ __   ___ | | _____ _ __ ___   ___  _ __       _  ______  | | \n"+
      "|  _ \ / _ \| |/ / _ \  _   _ \ / _ \|  _ \     / |/ / __ \ |_| \n"+
      "| |_) | (_) |   <  __/ | | | | | (_) | | | |   /    / /_/ /  _  \n"+
      "|  __/ \___/|_|\_\___|_| |_| |_|\___/|_| |_|  /_/|_/\____/  (_) \n"+
      "| |                                                             \n"+
      "|_|  By: Otto Lähepelto 22-23.7.2016                            \n")


    print("You are in some fancy adventure fantasy place\n"+
      "there aren't any Pókemon in the around\n" +
      "use help for help \n\n")

def clear():
    print("\n" * 40);
def save():
    print("WIP")
def load():
    print("WIP")
