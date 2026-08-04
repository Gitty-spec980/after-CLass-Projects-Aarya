
tw = 4
oc = tw
print(f"You have {oc} homework tasks to finish today!\n")
 

cc = 0
task_num = 1
 

while task_num <= tw:
 
    
    if task_num == 1:
        next_task = "Math worksheet"
    elif task_num == 2:
        next_task = "Science reading"
    elif task_num == 3:
        next_task = "English writing"
    else:
        next_task = "Coding practice"
 
    answer = input(f"Have you finished: {next_task}? (yes/no): ")
 
    
    if answer == "yes":
        cc += 1
        task_num += 1
        print("Great job! Homework task completed.")
    else:
        print("Okay, finish it and check again!")
 
    
    print("Homework tasks remaining:", tw - cc)
    print()
 

print("===== ALL HOMEWORK COMPLETE! =====")
print("Nice\n")
 
 

print("\n===== HW summary. =====")
print("Homework Assigned Today:", oc)
print("Homework Completed:", cc)
print("Homework Remaining:", tw - cc)
print("=======================================")
