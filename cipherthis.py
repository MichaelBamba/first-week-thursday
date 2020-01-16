Ceasar_code = input("Code you need to crack")
offset_amount = input("how much code is off by")
Letters = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
# changed_letters = "yzabcdefghijklmnopqrstuvwx"
H4x0r = ""



for index in range(len(Ceasar_code)):
    add_to = ""
    for innerindex in range(len(Letters)):
        if Ceasar_code[index] == Letters[innerindex]:
            rotated_index = innerindex + int(offset_amount)
            add_to = str(Letters[rotated_index])
            break
        else :
            add_to = Ceasar_code[index] 
    H4x0r = H4x0r + add_to
    # H4x0r += add_to
print (H4x0r)