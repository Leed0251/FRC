# import libraries
import pandas

# *** Functions go here ***

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
    while item_name.lower() != "xxx":

        print()
        # get name, quantity and item
        item_name = not_blank("Item name: ",
        "The component name can't be "
        "blank.")
        if item_name.lower() == "xxx":
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

# **** Main Routine goes here ****
# Get product name
product_name = not_blank("Product name: ", "The product name cannot be blank")

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

# Find Total Costs

# Ask user for profit goal

# Calculate recommended price

# Write data to file

# *** Printing Area ***

print()
print(f"**** Fund Raising - {product_name} ****")
print()
expense_print("Variable",variable_frame,variable_sub)

if have_fixed == "yes":
    expense_print("Fixed", fixed_frame[["Cost"]], fixed_sub)
    