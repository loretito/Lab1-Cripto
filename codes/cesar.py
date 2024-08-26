import sys
from functions import cesar

message = sys.argv[1] 
shift = sys.argv[2]

print(cesar(message, int(shift)))