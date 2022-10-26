#Name: Marcela Soriano Cornejo
#Email: marcela.sorianocornejo40@myhunter.cuny.edu
#Date: 24 October 2022
#Program 25: Converts pseudocode to a string decimal.

numberx = input("Enter a string with 0 or 1 only: ")
num = 0

for i in (len(numberx), 0, -1):
  if numberx [i-1] == "1":
    num = num + (2**i)
  elif numberx [i-1] == "0":
    num = num
  else:
    print("Letter", numberx[i-1], "is not allowed in binary string.")
    exit()

print("num =", num)        
exit()