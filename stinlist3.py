FavoritePokemon = "crobat, squirtle, pikachu, chikorita, lugia, sylveon"

reverse = ""
index = len(FavoritePokemon)
print (index)

while index > 0 :
    reverse  += str(FavoritePokemon[index -1 ])
    index= index - 1
    str (reverse)
print (reverse)