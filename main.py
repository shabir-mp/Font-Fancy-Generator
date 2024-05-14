import pyfiglet
import termcolor
import random, os

def get_random_font_style():
    """Get a random Figlet font style"""
    return random.choice(pyfiglet.FigletFont.getFonts())

def get_random_color():
    """Get a random color"""
    return random.choice(['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white'])

def print_text(text):
    """Print the decorative greeting in a random font style and color"""
    random_font_style = get_random_font_style()
    random_color = get_random_color()
    font = pyfiglet.Figlet(font=random_font_style)
    ascii_art = font.renderText(text)
    print(termcolor.colored(ascii_art, random_color))
   
print("RANDOM FANCY FONT GENERATOR")
print("Copyright 2024 - @shabir-mp")
print()
text = input("Input Text: ")
os.system("clear")
print_text(text)
print()
print("Your Fancy Font art has finish. If you want another art, please retry again. \nThis Program if random-based code. Error may occur.")
print("Copyright 2024 - @shabir-mp")
