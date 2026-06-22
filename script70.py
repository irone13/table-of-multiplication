import numpy as np
table = np.arange(1,11).reshape(10,1) * np.arange(1,11)
choix = int(input("wish table of multiplication do you want ? (1-10)"))
print (f"The table {choix} is", table[choix-1])
