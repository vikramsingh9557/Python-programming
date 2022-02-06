# write a program to create a dictionary of hindi words with values as their english translation  provide a option with user 

d={"tum" :  "you",
     "hum" :  "we",
     "hamara" :  "our",
     " kon" : " who"}
print("options are : ", d.keys())
a=input("enter the hindi word  ")
print("  english meaning is =", d.get(a))

