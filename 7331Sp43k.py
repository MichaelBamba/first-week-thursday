Darth_Sidious = "Darth Sidious, a Force-sensitive human male, was the Dark Lord of the Sith and Galactic Emperor who ruled the galaxy from the fall of the Galactic Republic to the fragmentation of the Galactic Empire. ... Inherently gifted with the Force, he became Darth Sidious during his apprenticeship under Darth Plagueis."

Letters = "aegiost"
numbers = "4361057"
Darth_1337 = ""

for index in range(len(Darth_Sidious)):
    add_to = ""
    for innerindex in range(len(Letters)):
        if Darth_Sidious[index] == Letters[innerindex]:
            add_to = str(numbers[innerindex])
            break
        else :
            add_to = Darth_Sidious[index] 
    Darth_1337 = Darth_1337 + add_to
    # Darth_1337 += add_to
print (Darth_1337)