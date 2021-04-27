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
        except:
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
        except:
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
        except :
            print("Integers required")
    if mark_pass+mark_fail+mark_defer!=120:
        print("Total Incorrect, Reenter values again.")
        student_prompt()
student_prompt()
#recalling functions
def progression_outcome():
    if mark_pass==120:
        print("Progression Outcome:Progress")
    elif mark_pass==100:
        print("Progression Outcome:Progress - module trailer")
    elif mark_pass<100 and mark_pass+mark_defer>40:
        print("Progression Outcome:Do not Progress - module retriever")    
    elif mark_fail>=80:
        print("Progression Outcome:Exclude")
progression_outcome()
 

