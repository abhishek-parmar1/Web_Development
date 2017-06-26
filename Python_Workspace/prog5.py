loop_Variable = True
while (loop_Variable):
    print "Select the option : "
    print "1 : Update the status"
    print "2 : Quit the chat"
    spy_Choice = int(raw_input("Enter the option : "))
    if (spy_Choice == 1):
        print "spy chooses to update the status"
        spy_Status = raw_input("Enter the Status : ")
    elif (spy_Choice == 2):
        print "bye bye"
        loop_Variable = False
