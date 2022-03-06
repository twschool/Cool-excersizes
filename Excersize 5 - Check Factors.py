def factor_check(number_1, number_2):
    return number_1 % number_2 == 0


# Main routine
big = int(input("Bigger number: "))
small = int(input("Smaller number: "))
if factor_check(big, small):
    print(f"{small} is a factor of {big}")
else:
    print(f"{small} is NOT a factor of {big}")
