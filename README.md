# Font-Fancy-Generator
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/shabir-mp/Image-Background-Remover/blob/main/LICENSE)

Create an engaging and visually appealing representation of your text using different font styles and colors. The output is random-based, so you'll get a unique text art each time you run the application. Enjoy experimenting with various text inputs and experience the magic of random fancy font generator!

## How it works ?

1. After launching the application, you will see a decorative greeting message along with a copyright note.
2. The application then prompts you to input a text string of your choice. You can type in any text you'd like to convert into a fancy font text art.
3. Once you've entered the text, press Enter, and the application will clear the console.
4. The application will then generate a random font style and color for your text art and display it on the console.
5. After the text art is displayed, you will see a completion message with an option to generate another art.

## Code Explain
This Python script is a simple text decoration tool that generates a fancy font text art using the help of pyfiglet and termcolor libraries. Here's a breakdown of the code:

### a. Importing necessary libraries

1. `pyfiglet`: A Python library to create text banners or ASCII art using Figlet font.
2. `termcolor`: A Python library to colorize your terminal output.
3. `random, os`: Built-in Python libraries for random selection and system operations.

### b. Function definitions
1. `get_random_font_style()`: Returns a random Figlet font style from the available list.
2. `get_random_color()`: Returns a random color string from the predefined list.
3. `print_text(text)`: Takes a text input, selects a random font style and color, converts the text to ASCII art using the chosen font style, and prints the colored ASCII art on the console.

### c. Main program
The script prints a decorative greeting with a random-based copyright message.
It prompts the user to input a text string for generating the fancy font text art.
After generating the ASCII art, it prints a completion message with an option to generate another art.
The script uses random font styles and colors to create a visually appealing text art. It is important to note that the output may vary each time the script is executed due to the randomness introduced by the random_font_style and random_color variables.

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

-----------------------------------------------------------------------------------------
![Github Footer](https://github.com/shabir-mp/Kereta-Api-Indonesia-Booking-System/assets/133546000/c1833fe4-f470-494f-99e7-d583421625be)


