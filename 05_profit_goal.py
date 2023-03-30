# functions go here


# Checks that user has entered yes / no to a question
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

def profit_goal(total_costs):
    
    # Initialise variables and error message
    error = "Please enter a valid profit goal\n"

    while True:

        # ask for a profit goal...
        response = input("What is your profit goal (eg $500 or 50%) ")

        # check if first character is $...
        if response[0] == "$":
            profit_type = "$"
            # Get amount (everything after the $)
            amount = response[1:]

        # check if last character is %
        elif response[-1] == "%":
            profit_type = "%"
            # Get amount (everything before the %)
            amount = response[:-1]

        else:
            # set response to amount for now
            profit_type = "unknown"
            amount = response

        try:
            # Check amount is a number more than zero...
            amount = float(amount)
            if amount <= 0:
                print(error)
                continue

        except ValueError:
            print(error)
            continue

        if profit_type == "unknown" and amount >= 100:
            dollar_type = yes_no(f"Do you mean ${amount:.2f}. "
            f"ie {amount:.2f} dollars? ,"
            "y / n ")

            # Set profit type based on user answer above
            if dollar_type == "yes":
                profit_type = "$"
            else:
                profit_type = "%"

        elif profit_type == "unknown" and amount < 100:
            percent_type = yes_no(f"Do you mean {amount}%?, y / n ")
            if percent_type == "yes":
                profit_type = "%"
            else:
                profit_type = "$"

        # return profit goal to main routine
        if profit_type == "$":
            return amount
        else:
            goal = (amount / 100) * total_costs
            return goal

# Main Routine goes here
all_costs = 200

# Loop for quick testing...
for item in range(0, 6):
    profit_target = profit_goal(all_costs)
    print(f"Profit Target: ${profit_target:.2f}")
    print(f"Total Sales: ${all_costs+profit_target:.2f}")
    print()
