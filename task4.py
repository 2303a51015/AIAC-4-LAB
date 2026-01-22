'''
indian Zodiac Order
March → Mesha
April → Vrishabha
May → Mithuna
June → Karka
July → Simha
August → Kanya
September → Tula
October → Vrischika
November → Dhanu
December → Makara
January → Kumbha
February → Meena
diaply the zodiac sign based on the month input by the user.
'''

def get_zodiac_sign(month):
    zodiac_signs = {
        "March": "Mesha",
        "April": "Vrishabha",
        "May": "Mithuna",
        "June": "Karka",
        "July": "Simha",
        "August": "Kanya",
        "September": "Tula",
        "October": "Vrischika",
        "November": "Dhanu",
        "December": "Makara",
        "January": "Kumbha",
        "February": "Meena"
    }
    return zodiac_signs.get(month, None)

month = input("Enter the month: ")
sign = get_zodiac_sign(month)
if sign:
    print(f"The zodiac sign for {month} is {sign}")
else:
    print("Invalid month")