from colorama import Fore, Style
#TASK: Favourite Color Personality Test
## Create a simple program that asks the user for their favourite color.
## Requirements:
# 1. Ask the user to enter their favourite color.
# 2. Convert the input to lowercase.
# 3. For each color provided by the user, print a short personality description.
## Example:
# red   -> "You are passionate and energetic."
# blue  -> "You are calm and trustworthy."
# green -> "You are balanced and nature-loving."
# yellow -> "You are cheerful and optimistic."
# any other option -> "You have a unique personality!"

#elif

""" color = input("What is your favourite color? ").lower()

if color == "red":
    print("You are passionate and energetic.")
elif color == "blue":
    print("You are calm and trustworthy.")
elif color == "green":
    print("You are balanced and nature-loving.")
elif color == "yellow":
    print("You are cheerful and optimistic.")
else:
    print("You have a unique personality!") """

#match
color = input("What is your favourite color? ").lower()

match color:
    case "red":
        print(Fore.RED + "assionate and energetic.")
    case "blue":
        print(Fore.BLUE + "You are calm and thoughtful.")
    case "green":
        print(Fore.GREEN + "You are balanced and nature-loving")
    case "yellow":
        print(Fore.YELLOW + "ou are cheerful and optimistic.")
    case _:
        print(Fore.MAGENTA + "You have a unique personality!")