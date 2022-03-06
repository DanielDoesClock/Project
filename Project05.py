"""This project asks for name and speed over the limit to fine people
Made by Daniel Fraser
06/03/2022"""

total_fine = 0
initial_fine = 0
num_fines = 0
name_list = []
fine_list = []
number = 0
fine = 0


def integer_checker(question):
    error = "Please enter a number"
    number_ = ""
    while not number_:
        try:
            number_ = int(input(question))
            return number
        except ValueError:
            print(error)


continue_ = "YES"
while continue_ != "NO":
    if continue_ == "YES":
        num_fines += 1
        name = input("Input the name of the speeder >> ").title()
        speed = integer_checker("Input the amount over the speed limit >> ")
        if speed < 10:
            total_fine += 30
            initial_fine += 30
        elif speed <= 14:
            total_fine += 80
            initial_fine += 80
        elif speed <= 19:
            total_fine += 120
            initial_fine += 120
        elif speed <= 24:
            total_fine += 170
            initial_fine += 170
        elif speed <= 29:
            total_fine += 230
            initial_fine += 230
        elif speed <= 34:
            total_fine += 300
            initial_fine += 300
        elif speed <= 39:
            total_fine += 400
            initial_fine += 400
        elif speed <= 44:
            total_fine += 510
            initial_fine += 510
        else:
            total_fine += 630
            initial_fine += 630
        if name == "James Wilson" or name == "Helga Norman" or name ==\
                "Zachary Conroy":
            print(f"{name} - WARRANT TO ARREST")
        print(f"{name} to be fined: ${initial_fine}")
        continue_ = input("Would you like to continue? >> ").upper()
        name_list.append(name)
        fine_list.append(initial_fine)
        initial_fine = 0
    else:
        print("Please say 'yes or no'")
        continue_ = input("Would you like to continue? >> ").upper()
else:
    print("--------------------------------------------------------------")
    print(f"Number of fines: {num_fines}")
    while number != len(name_list):
        print("--------------------------------------------------------------")
        print(f"{number}) Name: {name_list[number]}")
        print(f"Amount over: {fine_list[number]}")
        print("--------------------------------------------------------------")
        number += 1
    print(f"Total amount of fines: ${total_fine}")
    print("--------------------------------------------------------------")
