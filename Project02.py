"""This is a project that helps the user drop off, pick up, pay for and show
 the names off all of the children in the daycare
 Made by Daniel Fraser
 25/02/2022"""


def integer_checker(question):
    error = "\nPlease enter a number\n"
    number = ""
    while not number:
        try:
            number = int(input(question))
            return number
        except ValueError:
            print(error)


highest = 0
item = input("What is the item you would like to sell? >> ")
reserve = integer_checker("What is the reserve price? >> $")
latest_bid = 0

while latest_bid >= 0:
    print(f"The highest price is ${highest:,.2f}")
    latest_bid = integer_checker("What would you like to bid? >> $")
    if latest_bid > highest:
        highest = latest_bid
    else:
        highest += 0

if highest <= reserve:
    print(f"So sorry, no one wanted '{item}' for the price of $"
          f"{reserve:,.2f}")
else:
    print(f"Congratulations! '{item}' sold for ${highest:,.2f}")
