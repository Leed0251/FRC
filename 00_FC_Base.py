# import libraries
import pandas
import math
import os

# *** Functions go here ***

# Shows instructions
def show_instructions():
    print("""
***** Instructions *****

This program will ask you for...
 - The name of the product you are selling
 - How many items you plan on selling
 - The costs for each component of the product
 - How much money you want to make

It will then output an itemised list of the costs
with subtotals for the variable and fixed costs.
Finally it will tell you how much you should sell
each item for to reach your profit goal.

The data will also be written to a text file which
has the same name as your product

*************************
    """)

# checks that input is either a float or an
# integer that is more than zero. Takes in custom error message
def num_check(question, error, num_type):
    valid = False
    while not valid:

        try:
            response = num_type(input(question))

            if response <= 0:
                print(error)
            else:
                return response
                
        except ValueError:
            print(error)


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


# Checks that string response is not blank
def not_blank(question, error):

    while True:
        response = input(question)

        # if the response is blank, outputs error
        if response == "":
            print(f"{error}. \nPlease try again.\n")
            continue
        
        return response


# Currency formatting
def currency(x):
    return f"${x:.2f}"


# currency formatting function
def currency(x):
    return f"${x:.2f}"


# Get expenses, returns list which has
# the data frame and sub total
def get_expenses(var_fixed):
    # Set up dictionaries and lists
    
    item_list = []
    quantity_list = []
    price_list = []

    variable_dict = {
        "Item": item_list,
        "Quantity": quantity_list,
        "Price": price_list
    }

    # loop to get component, quantity and price
    item_name = ""
    while True:

        print()
        # get name, quantity and item
        item_name = not_blank("Item name: ",
        "The component name can't be "
        "blank.")
        if item_name.lower() == "xxx":
            if item_list == []:
                print("You must have at least 1 item!")
                continue
            else:
                break

        if var_fixed == "variable":
            quantity = num_check("Quantity:",
            "The amount must be a whole number larger than zero",
            int)
        else:
            quantity = 1
        
        price = num_check("How much? $",
        "The price must be a number larger than zero",
        float)

        # add item, quantity and price to lists
        item_list.append(item_name)
        quantity_list.append(quantity)
        price_list.append(price)

    expense_frame = pandas.DataFrame(variable_dict)
    expense_frame = expense_frame.set_index("Item")

    # Calculate cost of each component
    expense_frame["Cost"] = expense_frame["Quantity"]\
        * expense_frame["Price"]

    # Find sub total
    sub_total = expense_frame["Cost"].sum()

    # Currency Formatting (uses currency function)
    add_dollars = ["Price", "Cost"]
    for item in add_dollars:
        expense_frame[item] = expense_frame[item].apply(currency)

    return [expense_frame, sub_total]

# Prints expense frames
def expense_print(heading, frame, subtotal):
    print()
    print(f"**** {heading} Costs ****")
    print(frame)
    print()
    print(f"{heading} Costs: ${subtotal:.2f}")


# work out profit goal and total sales required
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


# rounding function
def round_up(amount, roundto):
    return int(math.ceil(amount / roundto)) * roundto


# **** Main Routine goes here ****

displayInstructions = yes_no("Do you want to read the instructions (y/n): ")

if displayInstructions == "yes":
    show_instructions()

# Get product name
product_name = not_blank("Product name: ", "The product name cannot be blank")

how_many = num_check("How many items will you be producting? ",
"The number of items must be a whole number more than zero", int)

print()
print("Please enter your variable costs below...")
# Get variable costs
variable_expenses = get_expenses("variable")
variable_frame = variable_expenses[0]
variable_sub = variable_expenses[1]

print()
have_fixed = yes_no("Do you have fixed costs (y / n)? ")

if have_fixed == "yes":
    # Get fixed costs
    fixed_expenses = get_expenses("fixed")
    fixed_frame = variable_expenses[0]
    fixed_sub = fixed_expenses[1]
else:
    fixed_sub = 0

# work out total costs and profit target
all_costs = variable_sub + fixed_sub
profit_target = profit_goal(all_costs)

# Calculates total sales needed to reach goal
sales_needed = all_costs + profit_target

# Ask user for rounding
round_to = num_check("Round to nearest...? $", "Can't be 0 or under", float)

# Calculate recommened price
selling_price = sales_needed / how_many
print(f"Selling Price (unrounded): ${selling_price:.2f}")

recommended_price = currency(round_up(selling_price, round_to))

# Change frames to strings
variable_txt = pandas.DataFrame.to_string(variable_frame)

heading = f"**** {product_name} ****"

to_write = [heading, variable_txt,
currency(profit_target), recommended_price]

if have_fixed == "yes":
    fixed_txt = pandas.DataFrame.to_string(fixed_frame)
    to_write = [heading, variable_txt, fixed_txt,
    currency(profit_target), recommended_price]


# Write to file...
# create file to hold data (add .txt extension)
file_name = f"{product_name}.txt"
text_file = open(file_name, "w+")

# heading
for item in to_write:
    text_file.write(item)
    text_file.write("\n\n")

# close file
text_file.close()

# Print Stuff
for item in to_write:
    print(item)
    print()

print(f"Saved receipt to {os.path.realpath(text_file.name)}")