
def user_current_hr():
    current_hr = -1
    while (current_hr < 0 or current_hr >= 24):
        current_hr = int(input("Enter the current hour (0-23): "))
        if (current_hr < 0 or current_hr >= 24):
            print("The current hour must be between 0 and 23.")
    return current_hr

def user_delay_hr():
    delay_hr = -1
    while delay_hr < 0:
        delay_hr = int(input("How long after do you want to set an alarm? (in hrs): "))
        if delay_hr < 0:
            print("The delay must be a positive number.")
    return delay_hr

user_current_hr = user_current_hr()
user_delay_hr = user_delay_hr()

alarm_hr = (user_current_hr + user_delay_hr) % 24

print("The alarm will go off at {}.".format(alarm_hr))