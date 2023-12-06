def leap_year(year):
    '''return True if leap year False for non leap years'''

    return year % 4 == 0 and (year % 400 == 0 or year %100 != 0) 

print(leap_year(2020))

month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31 , 30, 31] 

def days_in_month(year, month):

    if not 1<= month <= 12:
        return "Invalid Month"
    if month == 2 and leap_year(year):
        return 29
    
    return month_days[month]
print(days_in_month(2024,2))