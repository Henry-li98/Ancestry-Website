
def get_name():
    while True:
        first_name = input("Please input first name: ")
        last_name = input("Please input last name: ")

        print(f"You wrote: {first_name} {last_name}")
        confirm = input("please confirm that this is correct (yes/no)").lower()

        if confirm == 'no':
            print("please input the name again")
        elif confirm == 'yes':
            return first_name, last_name
def family_name():
    for i in range(1, len(names), 2):
        print(names[i])

#most likely once above def is executed, have it input into a list
names = []
find_name = get_name()
names.append(str(find_name))

print(f"Here is the current unordered list of names {', '.join(names)}")



# make a def that splits that reads and organizes the last names of each person in the list to different groups,
# def family_name(last_name):