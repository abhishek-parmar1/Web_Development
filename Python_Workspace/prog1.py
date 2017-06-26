print "let's get started "

spy_name = raw_input("What's your name : ")
if len(spy_name)!=0:
    print "welcome to a secret mission " + spy_name
else:
    print" You are not James Bond"

spy_status = raw_input("Are you online True/False : ")
if(spy_status == True):
    spy_rating = float(raw_input("enter the rating in 0 - 10 : "))
    if(spy_rating>=0 and spy_rating<=10):
        print "your rating is " + str(spy_rating*10) + " %"
    else:
        print " enter valid rating ... Try again !!!"
else:
    print "You are ofline"

