import os
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

# add how the relative attached

# every person should be assigned with an ID/number the way the nodes should connect in the backend is pointers, with different types of pointers (parent,child), able add
# biggest data points to go for ==> birthday, mother, father, name
# logic should be traversing through the set and connect the pointers
# json file would be better to hold all the information as it is a dictionary
# have inputs that would suggest the parents name
# event listener that looks into user input to auto supply family names