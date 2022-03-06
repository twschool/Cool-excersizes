def calc_overdue(days_overdue_):
    base_charge = .5
    daily_charge = .8
    max_charge = 30
    price = (days_overdue_ * daily_charge) + base_charge
    if price >= max_charge:
        price = max_charge
    return price


# Main routine
days_overdue = int(input("Enter the number of days overdue: "))
print(f"for {days_overdue} days overdue please pay\n${calc_overdue(days_overdue):.2f}")
