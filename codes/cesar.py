# sudo python3 cesar.py "criptografía y seguridad en redes" 9 

def cesar (text, shift):
    result = ""
    for i in range(len(text)):
        char = text[i]

        if (char == " "):
            result += " "
        elif (char.isupper()):
            result += chr((ord(char) + shift-65) % 26 + 65)
        elif (char.isnumeric()):
            result += str((int(char) + shift) % 10)    
        elif (char.islower()):
            result += chr((ord(char) + shift - 97) % 26 + 97)        
        else:
            result += chr(ord(char)+shift)

    print(result)

cesar("criptografía y seguridad en redes", 9)

cesar("Criptografía y Seguridad en Redes", 9)

cesar("hola 1 @ )", 2)