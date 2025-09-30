
def get_name():
    while True:
        first_name = input("Please input first name: ")
        last_name = input("Please input last name: ")

        print(f"You wrote: {first_name} {last_name}")
        confirm = input("please confirm that this is correct (yes/no)").lower()

        if confirm == 'no':
            print("please input the name again")
        elif confirm == 'yes':
            break

get_name()
