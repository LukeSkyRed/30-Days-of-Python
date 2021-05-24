# Day 1: Numbers, Arithmetic, and Printing to the Console

#calculate the numbers of days,weeks, months in 27 years

years = 27
days = 365
weeks = 52
month = 12

days_per_years = years * days
weeks_per_years = years * weeks
months_per_years = years * month

print("Il numero di giorni in " + str(years) + " anni è " +
      str(days_per_years))
print("Il numero di settimane in " + str(years) + " anni è " +
      str(weeks_per_years))
print("Il numero di mesi in " + str(years) + " anni è " +
      str(months_per_years))

#calculate the area of a circle with radius 5

radius = 5

area = 3.14 * pow(radius, 2)