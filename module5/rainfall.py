# input number of years
num_years = int(input("Enter number of years: "))

# initialize total rainfall
total_rainfall = 0

# loop through each year
for year in range(1, num_years + 1):
    print(f"Year {year}:")
    # loop through each month
    for month in range(1, 13):
        # input rainfall for each month
        rainfall = float(input(f"Enter the rainfall for month {month}: "))
        # add rainfall to total rainfall
        total_rainfall += rainfall

# calculate average rainfall
average_rainfall = total_rainfall / (num_years * 12)

# print total number of months
total_months = num_years * 12
print(f"Total months: {total_months}")
# print total rainfall
print(f"Total rainfall: {total_rainfall:.2f} inches")
# print average rainfall per month
print(f"Average rainfall: {average_rainfall:.2f} inches per month")