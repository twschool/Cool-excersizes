def make_positive(number):
        new_number = abs(number)
        return new_number


number_to_check = int(input("Enter a number: "))
print(f"The absolute value to {number_to_check} is {make_positive(number_to_check)}")
