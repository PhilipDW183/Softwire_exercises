def printFizzBuzz(number):

    multiple5 = number % 5 == 0
    multiple3 = number % 3 == 0
    multiple7 = number % 7 == 0
    multiple11 = number % 11 == 0
    multiple13 = number % 13 == 0
    multiple17 = number % 17 == 0

    output = ""

    if multiple11:
        output = "Bong"
    elif multiple5 and multiple3:
        output = "FizzBuzz"
    elif multiple3:
        output = "Fizz"
    elif multiple5:
        output = "Buzz"
    else:
        output = number

    if multiple7:
        if output == number:
            output = "Bang"
        elif output == "Bong":
            pass
        else:
            output = output + "Bang"

    if multiple13:
        if output == number:
            output = "Fezz"
        else:
            if "B" in output:
                b_index = output.find("B")
                output = output[0:b_index] + "Fezz" + output[b_index:]
            else:
                output = output+"Fezz"

    if multiple17:
        if output == number:
            pass
        else:
            split_output = [output[i:i+4] for i in range(0, len(output), 4)]
            reversed_split_output = split_output[::-1]
            reversed_output = "".join(reversed_split_output)
            return reversed_output


    return output

if __name__ == "__main__":
    for num in range(1, 300):
        output = printFizzBuzz(num)
        print(output)