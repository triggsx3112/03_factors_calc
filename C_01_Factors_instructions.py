# checks that a number is more than zero
def num_check(question):

    error = "please enter a number that is more then zero\n"

    while True:

        try:
            response = float(input(question))

            # checks response is more than zero
            if response > 0:
                return response

            # checks response is more than zero (other wise repeats question)
            else:
                print(error)

        except ValueError:
            print(error)

# Asks user for width, loops for testing purposes
for item in range(0, 2):
    width = num_check("width ")
    print(width)

