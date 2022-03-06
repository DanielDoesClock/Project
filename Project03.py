"""This project takes, calculates and then prints off information for a
taxi driver
Made by Daniel Fraser
02/03/2022"""

BASE_PRICE = 10
PRICE_MIN = 2
total_time = 0
income = 0
times = []
costs = []
income_list = []
trip_num = 0


def integer_checker(question):
    error = "Please enter a number"
    number = ""
    while not number:
        try:
            number = int(input(question))
            return number
        except ValueError:
            print(error)


name = input("What is your name? >> ")
trip = input("Would you like to start a new trip? >> ").upper()
while trip != "NO":
    if trip == "YES":
        time = integer_checker("How long was the trip? (In minutes) >> ")
        total_time += time
        income = time * PRICE_MIN
        income += BASE_PRICE
        income_list.append(income)
        costs.append(income)
        times.append(time)
        trip_num = 1
        print("Time successfully added")
    else:
        print("Please say 'Yes' or 'no'")
    trip = input("Would you like to start a new trip? >> ").upper()
if trip_num > 0:
    avg_time = sum(times) / len(times)
    avg_cost = sum(costs) / len(costs)
    total_income = sum(income_list)
    print(f"Name = {name}\n")
    print(f"Total time over all trips: {total_time}m\n")
    print(f"Average time of trip: {avg_time:,.2f}m\n")
    print(f"Total income: ${total_income:,.2f}\n")
    print(f"Average cost of trip: ${avg_cost:,.2f}\n")
    print("Thank you for using our service!")
else:
    print("I don't see the point in having no trips, but thanks for your "
          "service anyway")
