def age_increase():
    age = int(raw_input("Enter age : "))
    age += age
    return age

name=raw_input("Enter the name : ")

if(name=="Rajat"):
    print " hey Rajat"
    age=age_increase()
    print name + " your new age is : " + age
elif(name=="Abhinav"):
    print "Bye Abhinav"
    age=age_increase()
    print name + " your new age is : " + age
else:
    print "you are an idiot"





