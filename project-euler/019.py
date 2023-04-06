
day_month = {1: 31, 2: 28, 3:31, 4: 30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
leap_day_month = {1: 31, 2: 29, 3:31, 4: 30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

monthPerYear = 12
yearsPerCentury = 100
dayPeryear =365
thisyear = 365
sundayCount = 0

for year in range(1, yearsPerCentury+1):
    for month in range(1, monthPerYear+1):
        if (thisyear+1) % 7 == 0:
            sundayCount += 1
        if (year) %4 == 0:
            thisyear += leap_day_month[month]
        else: 
            thisyear += day_month[month]
print(sundayCount)


