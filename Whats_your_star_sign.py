# Write a Python program to display astrological sign for given date of birth.  Expected Output:
#Input birthday: 15                                                      
#Input month of birth (e.g. march, july etc): may                        
#Your Astrological sign is : Taurus 
#
user_birthday = int(input(f'What day of the month if your birthday'))
user_month_of_birth = input(f'What month was you born')
if user_month_of_birth == 'March':
    users_astrological_sign = 'pisces' if (user_birthday < 22) else 'Aries'
if user_month_of_birth == 'April':
    users_astrological_sign = 'Aries' if (user_birthday < 20) else 'Taurus'