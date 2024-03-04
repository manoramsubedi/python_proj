import random
import string

def generate_passowrd(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters

    if numbers:
        characters += digits
    if special_characters:
        characters += special
    
    pwd = ""

    meet_criteria = False
    has_number = False
    has_special = False

    if meet_criteria or len(pwd)<min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True

        if new_char in special:
            has_special = True
            
        
        meet_criteria = True
        if numbers:
            meet_criteria = has_number
        if special_characters:
            meet_criteria = meet_criteria and has_special

    


def main():
    length = int(input("Input minimun length for password: "))
    generate_passowrd(length, False, False)