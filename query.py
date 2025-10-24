import os
import json


class InfoCollect:

    def __init__(self):
        self.first_name = None
        self.last_name = None
        self.birthday = None
        self.mother = None
        self.father = None

    def get_name(self):
        while True:
            self.first_name = input("Please input first name: ")
            self.last_name = input("Please input last name: ")
            self.birthday = input("please input the date of birth (MM/DD/YYY): ")
            self.mother = input("please input the name of your Mother: ")
            self.father = input("please input the nae of your father: ")

            print(f"your first name is: {self.first_name}/n "
                  f"last name is: {self.last_name} /n "
                  f"birthday: {self.birthday} /n"
                  f"mother: {self.mother} /n"
                  f"father: {self.father} /n")

            confirm = input("please confirm that this is correct (yes/no)").lower()

            user_data = {
                "f_name": self.first_name,
                "l_name": self.last_name,
                "b_day": self.birthday,
                "mother": self.mother,
                "father": self.father
            }

            if confirm == 'no':
                # add a way to check and ask which part should be redone
                print("please input the name again")
            elif confirm == 'yes':
                return user_data

    def save_to_json(self, data, file_name="ancestors.json"):

        with open(file_name, "w") as file:
            json.dump(data, file, indent=4)

    json_string = json.dumps(data)


def display_json(data, file_name="ancestors.json"):
    with open(file_name, "r") as file:
        data = json.load(file)
        print(data)
        return data


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
