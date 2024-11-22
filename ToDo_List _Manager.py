def task():
    tasks=[]
    print("-----WELCOME TO TASK MANAGEMENT APP-----")

    total_task= int(input("Enter the number of tasks you want to add: "))
    for i in range(1,total_task+1):
        task_name=input(f"Enter task {i} = ")
        tasks.append(task_name)

    print(f"Tasks are\n{tasks}")

    while True:
        operation = int(input("Enter 1- Add\n2- View\n3- Delete\n4-Exit"))
        if operation==1:
            add=input("Enter task you want to add = ")
            tasks.append(add)
            print(f"Task {add} has been successfully added.....")

        elif operation==2:
            print(f"Tasks = {tasks}")

        elif operation==3:
            del_value = input("Enter the task you want to delete")
            if del_value in tasks:
                ind = tasks.index(del_value)
                del tasks[ind]
                print(f"Task {del_value} has been deleted.....")

        elif operation==4:
            print("Program has been ended")
            break

        else:
            print("Invalid Input")

task()