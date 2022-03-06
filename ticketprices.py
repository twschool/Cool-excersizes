import time

time_ = time.asctime()
displayed_time_ = time_[11:16]
ticket_loop = "true"
total_price = 0
price = 0
print(f"Movie ticket prices:\nChild price 5$ Teen price 10$ Adult price 15$")
while ticket_loop == "true":
    how_many = 0
    bad_answer = False
    yesno = input("Would you like to purchase a ticket \n(y)es or (n)o or (v)iew ticket prices: ")
    if yesno.upper() == "Y":
        try:
            age = int(input("How old is this person: "))
        except ValueError:
            print("Please enter a number")
            age = 0
            bad_answer = True
        if age >= 18 and bad_answer is not True:
            price = 15
            print(f"Adult prices ${price}")
        elif age >= 13 and bad_answer is not True:
            price = 10
            print(f"Teen prices ${price}")
        elif age >= 1 and bad_answer is not True:
            price = 5
            print(f"Child prices ${price}")
        elif age <= 0 and bad_answer is not True:
            print("Please enter a valid number over 0")
            bad_answer = True
    if yesno.upper() == "V":
        print("Child price 5$ Teen price 10$ Adult price 15$")
    elif yesno.upper() == "N":
        print(f"You're final total is {total_price}")
        exit(f"Program exited at {displayed_time_}")
    elif yesno.upper() != "N" and yesno.upper() != "V" and yesno.upper() != "Y":
        print(str(f"Please enter a valid answer"))
        bad_answer = True
        time.sleep(0.5)
    if yesno.upper() == "Y":
        try:
            how_many = 0
            if bad_answer is not True:
                how_many = int(input("How many of this ticket would you like to purchase: "))
        except ValueError:
            print("Please enter a number")
        price = how_many * price
    total_price = price + total_price
    run_again = input(f"Your total is {total_price} so far\n(B)uy new ticket or (E)xit shop: ")
    if run_again.upper() == "E":
        exit(f"Final total was {total_price}\nexited at {displayed_time_}")
    else:
        print("Restarting")
        time.sleep(1)
