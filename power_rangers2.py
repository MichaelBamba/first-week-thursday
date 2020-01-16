power_rangers = ["Jason", "Trini", "Zack", "Billy", "Kim", "Tommy"]

WhoToRemove = input("who would you like to remove ")

if WhoToRemove in power_rangers:
    power_rangers.remove(WhoToRemove)
    print( power_rangers)
else:
    print("%s isn't part of the group "% (WhoToRemove))