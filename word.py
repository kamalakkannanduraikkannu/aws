import random
word =str("banane")
print(word.replace("e","a"))
print(word[::-1])
for a in word[::1]:
 print(a,end="")
print("")

i = random.sample(range(0,10),4)
print("==========\\n==============",i)
