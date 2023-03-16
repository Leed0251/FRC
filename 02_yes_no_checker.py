def yes_no(question):

    responses = ["yes","no"]

    valid = False
    while not valid:

        response = input(question).lower()

        if response != "":
            for item in responses:
                if response in item:
                    return item

        print("Please enter either yes or no...\n")

# Loops to make testing faster...
for item in range(0,6):
    want_help = yes_no("Do you want to read the instructions? ")
    print(f"You said '{want_help}'\n")