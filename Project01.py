"""This is a project that helps the user drop off, pick up, pay for and show
 the names off all of the children in the daycare
 Made by Daniel Fraser
 24/02/2022"""

import time


def integer_checker(question):
    error = "\nPlease enter a number\n"
    number = ""
    while not number:
        try:
            number = int(input(question))
            return number
        except ValueError:
            print(error)


children_list = []
CHILD_COST = 12


def drop_off():
    add_child = input("What is the name of the child you would like to drop "
                      "off?\n>> ")
    children_list.append(add_child)
    print("Child successfully added!")
    time.sleep(1)


def pick_up():
    pickup_child = input("What is the name of the child you would like to "
                         "pick up?\n>> ")
    if pickup_child in children_list:
        children_list.remove(pickup_child)
        print("Child successfully removed!")
        time.sleep(1)
    else:
        print("This child is not currently in our system")
        time.sleep(1)


def calc_cost():
    num_hours = 0
    another_child = "YES"
    while another_child == "YES":
        time_ = integer_checker("How many hours has your child been under our "
                                "care? >> ")
        num_hours += time_
        another_child = input("Do you have another child to pay for? "
                              ">> ").upper()
    else:
        tot_cost = num_hours * CHILD_COST
        print(f"This comes to a total of ${tot_cost:,.2f}")
        time.sleep(1)


def print_roll():
    print(*children_list, sep='\n')
    time.sleep(1)


# Main routine
choice = 0
while choice != 5:
    print("------------------------------------------------------------------")
    print("Welcome to MGS Childcare")
    print("What would you like to do? Please choose one of the items below")
    print("------------------------------------------------------------------")
    print()
    print("1 Drop off a child")
    print("2 Pick up a child")
    print("3 Calculate cost")
    print("4 Print roll")
    print("5 Exit the system")
    print()
    choice = integer_checker("Enter your choice (number between 1 and 5) >> ")
    print()
    if choice == 1:
        drop_off()
    elif choice == 2:
        pick_up()
    elif choice == 3:
        calc_cost()
    elif choice == 4:
        print_roll()
    else:
        print("Thank you for using MGS ChildCare!")
