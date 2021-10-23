#Write a Python program to check whether an alphabet is a vowel or consonant. 
#Expected Output:
#Input a letter of the alphabet: k                                       
#This letter is a consonant.
vowel_check = input(f'Please enter a letter')
if vowel_check in ('a', 'e' , 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
    print('This is a vowel')
else: 
    print('This is a consonant')