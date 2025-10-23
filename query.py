import os
import json


def get_name():
    while True:
        first_name = input("Please input first name: ")
        last_name = input("Please input last name: ")
        birthday = input("please input the date of birth (MM/DD/YYY): ")

        print(f"You wrote: {first_name} {last_name} {birthday}")
        confirm = input("please confirm that this is correct (yes/no)").lower()

        user_data = {
            "f_name": first_name,
            "l_name": last_name,
            "b_day": birthday
        }

        if confirm == 'no':
            # add a way to check and ask which part should be redone
            print("please input the name again")
        elif confirm == 'yes':
            return user_data


def save_to_json(data, file_name="ancestors.json"):
    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)
    json_string = json.dumps(data)


def display_json(data, file_name="ancestors.json"):
    with open(file_name, "r") as file:
        data = json.load(file)
        print(data)
        return data
0

def main():
    ancestor = get_name()
    save_to_json(ancestor)
    print("Ancestor information saved. ")

# def relation():
#     connection = input("how is this person related within the family tree?")


# make a def that splits that reads and organizes the last names of each person in the list to different groups,
# def family_name(last_name):

# add how the relative attached

# every person should be assigned with an ID/number the way the nodes should connect in the backend is pointers, with different types of pointers (parent,child), able add
# biggest data points to go for ==> birthday, mother, father, name
# logic should be traversing through the set and connect the pointers
# json file would be better to hold all the information as it is a dictionary
# have inputs that would suggest the parents name
# event listener that looks into user input to auto supply family names
