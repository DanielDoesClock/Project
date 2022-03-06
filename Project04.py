"""This project asks for names and number of days every employee has been
absent from work and gives the user valid information about the employees.
Made by Daniel Fraser
03/03/2022"""

name_list = []
days_list = []
no_absence = []
over_avg = []
over_avg_2 = []
num_people = 0
no_days = 0
number_ = 0


def integer_checker(question):
    error = "Please enter a number"
    number = ""
    while not number:
        try:
            number = int(input(question))
            return number
        except ValueError:
            print(error)


# I changed the system because it did not seem as user friendly as it could be
name = input("What is the name of the employee? >> ")
days = integer_checker(f"How many days has '{name}' been absent? >> ")
print(f"'{name}' has been added successfully")
name_list.append(name)
days_list.append(days)
continue_ = input("Would you like to continue? >> ").upper()
while continue_ != "NO":
    if continue_ == "YES":
        name = input("What is the name of the employee? >> ")
        days = integer_checker(f"How many days has '{name}' been absent? >> ")
        print(f"'{name}' has been added successfully")
        name_list.append(name)
        days_list.append(days)
        continue_ = input("Would you like to continue? >> ").upper()
    else:
        print("Please say 'Yes or No'")
        continue_ = input("Would you like to continue? >> ").upper()
else:
    while no_days != len(name_list):
        if days_list[no_days] == 0:
            no_absence.append(name_list[no_days])
        no_days += 1
    avg_days = sum(days_list) / len(days_list)
    most_days_pos = max(days_list)
    most_days_pos = days_list. index(most_days_pos)
    print("------------------------------------------------------------------")
    print(f"The average days off is: {avg_days:,.2f}")
    print("------------------------------------------------------------------")
    print(f"The person with the most days absent is: "
          f"'{name_list.pop(most_days_pos)}' \nWith: "
          f"'{days_list.pop(most_days_pos)}' days absent")
    print("------------------------------------------------------------------")
    print(f"The people with 0 days absent are:")
    print(*no_absence, sep='\n')
    print("------------------------------------------------------------------")
    print("People with an above average absence:")
    while number_ != len(name_list):
        print(f"Name: {name_list[number_]}")
        print(f"Days absent: {days_list[number_]}")
        number_ += 1
    print("------------------------------------------------------------------")
    print("Thank you for using our service!")
    print("------------------------------------------------------------------")
