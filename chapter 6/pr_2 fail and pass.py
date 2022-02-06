a=int(input(" enter your marks subject1 : \n"))
b=int(input(" enter your marks subject2 : \n"))
c=int(input(" enter your marks subject3 : \n"))

if(a<33 or b<33 or c<33):
    print(" You are fail because you have less than 33% in one of the subjects")
elif(a+b+c)/3<40:
    print("You are fail due to total percentage less than 40")
else:
    print("congratulations you are passed in exam")
