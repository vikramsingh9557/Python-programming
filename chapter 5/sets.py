
# sets

#s=set()  #empty set
s=set({1,2,3,99,67,87,988})

print(len(s)) # find the length of sets
s.remove(3)   #removing the elements
#s.pop()       # remove randomaly  any element
#s.clear()
s.union({1,2})
s.intersection({99})

print(s)


