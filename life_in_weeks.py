def life_in_weeks(age):
    return (90 - age) * 52

age = int(input("How old are you? "))
weeks_left = life_in_weeks(age)

print(f"You have {weeks_left} weeks left")
