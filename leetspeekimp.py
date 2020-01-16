inputword = input("you sentance here")

Letters = "aegiostAEGIOST"
numbers = "43610574361057"
H4x0r = ""

for index in range(len(inputword)):
    add_to = ""
    for innerindex in range(len(Letters)):
        if inputword[index] == Letters[innerindex]:
            add_to = str(numbers[innerindex])
            break
        else :
            add_to = inputword[index] 
    H4x0r = H4x0r + add_to
    # H4x0r += add_to
print (H4x0r)