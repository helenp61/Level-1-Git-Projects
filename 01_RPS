def string_checker(question, to_check):

    valid = False
    while not valid:

        response = input(question).lower()

        for item in to_check:
            if response == item:
                return response
            elif response == item[0]:
                return item

        print("sorry that is not a valid response")

#  *** Main Routine starts here ***


yes_no = ["yes", "no"]
rps = ["rock", "paper", "scissors"]

mood = string_checker("Are you happy? ", yes_no)
print(mood)

choose = string_checker("Choose: ", rps)
print(choose)
