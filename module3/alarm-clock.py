# Enter the current time in hours
current_time_hours = int(input("Enter current time in hours:"))

# Enter nuo. of hours to wait for alarm
alarm_wait_hours = int(input("Enter number of hours to wait for alarm:"))

# calculate time of alarm
alarm_time_hours = (current_time_hours + alarm_wait_hours) % 24

# print time of alarm
print('Time for alarm goes off (in 24-hour clock): {}'.format(alarm_time_hours))