import time
print(time.asctime())
time_ = ""
while time_ != 1:
    time_ = time.asctime()
    displayed_time = int(time_[11:13])
    if int(displayed_time) <= 13:
        hour = displayed_time - 12
        day_period = "pm"
    else:
        hour = displayed_time
        day_period = "am"
    print(f"The time is {hour}{time_[13:16]} {day_period}")
    time.sleep(1)
