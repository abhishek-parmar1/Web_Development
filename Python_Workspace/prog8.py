print " Acadview's attendance management "
teacher_name = raw_input("Enter your name : ")
flag = True
while(flag):
    print "Select : \nA. Mark attendance \nB. Quit"
    teacher_choice = raw_input("Enter your choice : ")
    if(teacher_choice == "A"):
        students_count = int(raw_input(" Enter the number of students : "))
        students_name_list = []
        while(len(students_name_list)<students_count):
            student_name = raw_input(" Enter student name : ")
            if (student_name in students_name_list):
                check_status =  raw_input(" The name already exist. Are you sure ? Yes/No : ")
                if(check_status == "Yes"):
                    students_name_list.append(student_name)
                else:
                     continue
            else:
                students_name_list.append(student_name)
        for name in students_name_list:
            print name
    elif(teacher_choice == "B"):
        flag = False
        print "Bye"