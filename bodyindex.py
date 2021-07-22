name = str (input ("name : "))
kg= float (input ("kg"))
hg= float (input ("height"))

index=(kg/(hg)**2)
print ("{} your body index : {}".format(name,index))

if (index>=0) and (index<=18):
    print ("you are not overweight.")
elif (18<index<=27):
    print("you are normal")
else:
     print ("you are overweight.")
     
     
