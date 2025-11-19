import json
import random


# look into how IDs work and is it necessary to add more parameters to check for partner, mother nad father.
def collect_info():
    while True:
        first_name = input("Please input first name: ")
        last_name = input("Please input last name: ")
        birthday = input("please input the date of birth (MM/DD/YYY): ")
        partner = input("please input the name of your partner: ")
        mother = input("please input the name of your Mother: ")
        father = input("please input the name of your Father: ")

        print(f"your first name is: {first_name}/n "
              f"last name is: {last_name} /n "
              f"birthday: {birthday} /n"
              f"partner: {partner} /n"
              f"mother: {mother} /n"
              f"father: {father} /n")

        confirm = input("please confirm that this is correct (yes/no)").lower()

        if confirm == 'no':
            # add a way to check and ask which part should be redone
            print("please input information again")
            continue
        elif confirm == 'yes':
            person = Person(first_name, last_name, birthday, partner, mother, father)
            return person
        else:
            print("invalid input, please type 'yes' or 'no'. ")
            continue


class Person:
    def __init__(self, birthday, first_name, last_name, partner=None, mother=None, father=None):
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.id = random.randint(0, 999999)
        self.mother_id = mother
        self.father_id = father
        self.partner_id = partner

    def save_to_json(self, file_name="ancestors.json"):
        user_data = {
            "f_name": self.first_name,
            "l_name": self.last_name,
            "b_day": self.birthday,
            "partner": self.partner_id,
            "mother": self.mother_id,
            "father": self.father_id,
            "id": self.id

        }
        with open(file_name, "w") as file:
            json.dump(user_data, file, indent=4)
        print("information saved.")


def load_people(filename="ancestors.json"):
    with open(filename, "r") as file:
        return json.load(file)


def convert_json(filename="ancestors.json"):
    people = load_people(filename)
    return [Person(**p) for p in people]


def link_prep(people):
    id_map = {}
    for p in people:
        id_map[p["id"]] = p


def main():
    ancestor = collect_info()
    ancestor.save_to_json()
    print("displaying tree")
    # tree_display()


def last_name_search(people, last_name):
    search_last_name = last_name
    for p in people.last_name:
        l_name = [p["last_name"]] = p
        if search_last_name == l_name:
            return "MATCH"
        else:
            continue
# use Pythonanywhere.com to host the server


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


# app.py from Theory's pokemondraft, copy to league app.py and can be used as mine

#
# python anwyere go to web tab,
# got to directory of source code, add/edit the app.py and paste it in
# upload the definition.html file
