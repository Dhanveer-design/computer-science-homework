tasks = []

while True:
    print("===== HOMEWORK TRACKER =====")
    print("1. Add homework")
    print("2. View homework")
    print("3. Mark homework as completed")
    print("4. Show progress")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        print("--- Add Homework ---")
        subject = input("Enter the subject: ")
        homework = input("Enter the homework task: ")
        deadline = input("Enter the deadline: ")

        task = [subject, homework, deadline, False]
        tasks.append(task)

        print("Homework added successfully!")

    elif choice == "2":
        print("--- Your Homework ---")

        if len(tasks) == 0:
            print("There are no homework tasks yet.")
        else:
            for number in range(len(tasks)):
                print("Task", number + 1)
                print("Subject:", tasks[number][0])
                print("Homework:", tasks[number][1])
                print("Deadline:", tasks[number][2])

                if tasks[number][3] == True:
                    print("Status: Completed")
                else:
                    print("Status: Pending")

    elif choice == "3":
        if len(tasks) == 0:
            print("There are no tasks to complete.")
        else:
            for number in range(len(tasks)):
                print(number + 1, tasks[number][1])

            task_number = int(input("Which task number is completed? "))

            if task_number >= 1 and task_number <= len(tasks):
                tasks[task_number - 1][3] = True
                print("Task marked as completed!")
            else:
                print("That task number does not exist.")

    elif choice == "4":
        total = len(tasks)
        completed = 0

        for task in tasks:
            if task[3] == True:
                completed = completed + 1

        pending = total - completed

        print("\n--- Progress Summary ---")
        print("Total tasks:", total)
        print("Completed:", completed)
        print("Pending:", pending)

    elif choice == "5":
        print("Good luck with your homework!")
        break

    else:
        print("Invalid choice. Please try again.")
