names = []
while True:
    choice = input("1. Add aa student name\n2. Diplay student names\n3. Update a student name\n4. Remove a student\n5. Exit\nEnter")
    match choice:
        case "1":
            name = input("Enter the name:")
            names.append(name)
        case "2":
            print(f"{'s1. No.':<10}{'Name':<10}")
            for index,name in enumerate(names):
                print(f"{index+1:<10}{name:<10}")
            print(f"Total names:{len(names):>5}")
        case "3":
            print(f"{'s1. No.':<10}{'Name':<10}")
            for index,name in enumerate(names):
                print(f"{index+1:<10}{name:<10}")
            edit_index = int(input("Enter the S1. No. of the name you want to edit:")) - 1
            new_name = input("Enter the new name: ")
            names[edit_index]=new_name
        case "4":
            print(f"{'s1. No.':<10}{'Name':<10}")
            for index,name in enumerate(names):
                print(f"{index+1:<10}{name:<10}")
            delete_index = int(input("Enter the S1. No. of the name you want to remove: "))-1
            names.pop(delete_index)
        case "5":
            print("Exiting...")
            break
        case _:
            print("invalid Entry")

