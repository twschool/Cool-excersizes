def is_num():
    is_number_ = True
    num_ = input("Enter a number or word: ")
    try:
        int(num_) + 1
    except ValueError:
        is_number_: bool = False
        return [is_number_, num_]
    if is_number_:
        return [is_number_, num_]

# Main routine
func_list = is_num()
print(f"It is {func_list[0]} that {func_list[1]} is a number")
