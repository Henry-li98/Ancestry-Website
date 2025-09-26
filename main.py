while True:
    response = input("is there someone to add to the ancestry tree? (yes/no)").lower()
    if response == 'no':
        break
    elif response == 'yes':
        name = input("Please input name of the person")
        date = input("please input the month of birth and death of the person (in this format MM/YYYY) ")
    else:
        print("invalid input, please type yes or no")