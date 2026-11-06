# Cijfers van de student
grade_1 = 7
grade_2 = 6
grade_3 = 8

# Bereken het gemiddelde
average = (grade_1 + grade_2 + grade_3) / 3

print("Gemiddelde:", average)

# Controleer of de student geslaagd is
if average >= 5.5 and grade_1 >= 4 and grade_2 >= 4 and grade_3 >= 4:
    print("Geslaagd!")
else:
    print("Gezakt!")
