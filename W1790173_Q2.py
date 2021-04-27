progress=0
trailing=0
retriever=0
excluded=0
student_count=0
while True:
    def histogram():
        print("::::::::::::::::::::::::::::::::::::::::")
        print("Progress "," ",progress,": ",progress*"*")
        print("Trailing "," ",trailing,": ",trailing*"*")
        print("Retriever"," ",retriever,": ",retriever*"*")
        print("Excluded "," ",excluded,": ",excluded*"*")
        print(student_count,"outcomes in total")
        print("::::::::::::::::::::::::::::::::::::::::")
    def student_prompt():
        mark_range=[0,20,40,60,80,100,120]
        #input values and check conditions
        #mark_pass
        while True:
            try:
                global mark_pass
                mark_pass=int(input("Enter your pass mark:"))
                if type(mark_pass)==int and mark_pass in mark_range:
                        break
                else:
                    print("Range Error")
                    
            except ValueError:
                print("Integers required")
        #mark_defer    
        while True:
            try:
                global mark_defer
                mark_defer=int(input("Enter your defer mark:"))
                if type(mark_defer)==int and mark_defer in mark_range:
                    break
                else:
                    print("Range Error")
            except ValueError:
                print("Integers required")
        #mark_fail
        while True:
            try:
                global mark_fail
                mark_fail=int(input("Enter your fail mark:"))
                if type(mark_fail)==int and mark_fail in mark_range:
                    break
                else:
                    print("Range Error")
            except ValueError:
                print("Integers required")
        if mark_pass+mark_fail+mark_defer!=120:
            print("Total Incorrect, Reenter values again.")
            student_prompt()
        global student_count
        student_count+=1
    student_prompt()
    def progression_outcome():
        if mark_pass==120:
            print("Progression Outcome:Progress")
            global progress
            progress+=1
        elif mark_pass==100:
            print("Progression Outcome:Progress - module trailer")
            global trailing
            trailing+=1
        elif mark_pass<100 and mark_pass+mark_defer>40:
            print("Progression Outcome:Do not Progress - module retriever")
            global retriever
            retriever+=1
        elif mark_fail>=80:
            print("Progression Outcome:Exclude")
            global excluded
            excluded+=1
        
    progression_outcome()
    #asking user if loop needs to stop
    staff_command=input("press any key to continue program or press q to quit it:")
    if staff_command.lower()=="q":
        histogram()
        break 
       
