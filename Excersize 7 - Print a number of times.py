# Function to print a number of times
import time


def print_name(name, number):
    for item in range(0, number):
        print(name)
    print("You are the king here")

# Main routine
name_ = input("Name to print: ")
number_ = int(input("Times to print: "))
print_name(name_, number_)
time.sleep(5)
exit(f"Just kidding {name_} is the worst name I have ever heard\nlol legally change your name please")

