import sys

message = sys.argv[1] 
shift = sys.argv[2]

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

    return(result)

print(cesar(message, int(shift)))