import random

# Functions to go here


def check_rounds():
    while True:
        response = input("How many rounds: ")

        round_error = "Please type either <enter> or an "\
                      "integer that is more than 0\n"

        # If infinite mode not chosen check response
        # if an integer is more than 0

        if response != "":
            try:
                response = int(response)

                # If response is too low, go back

                if response < 1:
                    print(round_error)
                    continue

            except ValueError:
                print(round_error)
                continue

            return response
