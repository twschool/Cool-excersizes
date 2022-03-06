import time
ticketloop = "true"
totalprice = 0
price = 0
while ticketloop == "true":
    yesno = input("Would you like to purchase a ticket \n(y)es or (n)o or (v)iew ticket prices: ")
    if yesno.upper() == "Y":
        age = int(input("How old is this person: "))
        if age >= 18:
            price = 15
            print("Adult prices")
        elif age >= 13:
            price = 10
            print("Teen prices")
        elif age >= 10:
            price = 10
            print("Child prices")
        elif age <= 10:
            price = 5
            print("5")
    if yesno.upper() == "V":
        print("Child price 5$ Teen price 10$ Adult price 15$")
    elif yesno.upper() == "N":
        print("You're final total is ", totalprice)
        exit("I will see you soon ...")
    elif yesno.upper() != "N" and yesno.upper() != "V" and yesno.upper() != "Y":
        print(str(f"Not a valid answer please answer y for yes\nn for no or v for view ticket prices\n your total price so far is {totalprice} \nRestarting.."))
        time.sleep(0.5)
    totalprice = price + totalprice
    print(price)
    runagain = input(f"Your total is {totalprice} so far\n(B)uy new ticket or (E)xit shop: ")
    if runagain.upper() == "E":
        exit(f"Final total was {totalprice}")
    else:
        print("Restarting")
        time.sleep(2)
