import random

s = input("Enter a phrase: ")
passlen = int(input("How long? "))
p = "".join(random.sample(s,passlen ))
print (p) 