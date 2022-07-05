from random import randint
import os

def read_in_file(filename):
    """Read in a file and seperate the lines

    input:
        filename - destination of a chosen file

    output:
        lines - list of all lines in file

    """
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            lines = file.readlines()
        return lines
    else:
        exit()

def clean_lines(lines):
    """Strip whitespace and remove new line indentation

    inputs:
        lines - list of lines

    outputs:
        cleaned_lines - list of lines cleaned
    """
    cleaned_lines = []

    for index, line in enumerate(lines):

        cleaned_lines[index] = line.strip().split()

    return cleaned_lines

def ask_for_valid_input(input_type):
    """Asks user for a string input of a given type

    input:
        input_type - type of word that we require from the user

    output:
        user_input - returns the valid input from the user
    """

    while True:
        try:
            user_input = input(f"Please can you provide a {input_type}: ")
            user_input = str(user_input)
        except:
            print("Sorry that is an invalid value, try again")
            continue
        else:
            break

    return user_input


if __name__ == "__main__":

    print("You are about to play a madlib generator")
    print("For this you will need to know:")
    print("Noun: is an object, place or person")
    print("Verb: is an action")
    print("Adjective: is something describing an a noun")
    print("Adverb: is something describing a verb")

    input_types = ["noun", "verb", "adjective", "adverb"]

    lines = read_in_file("madlibs.txt")
    cleaned_lines = clean_lines(lines)

    random_int = randint(0, len(cleaned_lines)-1)

    line_selected = cleaned_lines[random_int]

    line_inputs = {}
    for index, word in enumerate(line_selected):
        if word in input_types:
            line_inputs[index] = word

    for key, value in line_inputs.items():
        user_input = ask_for_valid_input(value)
        line_inputs[key] = user_input

    for key, value in line_inputs.items():
        line_selected[key] = value

    final_statement = " ".join(line_selected)
    print(f"Your final statement is: {final_statement}")






