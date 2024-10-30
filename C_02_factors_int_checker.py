# checks that a number is more than zero
def num_check(question):

    error = "Please enter a number that is between 1 and 200 inclusive\n"

    while True:

        response = input(question).lower()

        try:
            response = int(question)

            # checks response is more than zero
            if response > 0:
                return response

            # checks response is more than zero (other wise repeats question)
            else:
                print(error)

        except ValueError:
            print(error)

while True:
    to_factor = num_check("To factor: ")
    print("You chose to factor", to_factor)

    if to_factor == "xxx":
        break