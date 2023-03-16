import pandas

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

# Gets expenses, returns list which has
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

    # Get user data
    product_name = not_blank("Product name: ", "The product name cannot be blank")

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

        quantity = num_check("Quantity:",
        "The amount must be a whole number larger than zero",
        int)
        
        price = num_check("How much for a single item? $",
        "The price must be a number larger than zero",
        float)

        # add item, quantity and price to lists
        item_list.append(item_name)
        quantity_list.append(quantity)
        price_list.append(price)

    expense_frame = pandas.DataFrame(variable_dict)
    expense_frame = variable_frame.set_index("Item")

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

# *** Main routine starts here ***

variable_expenses = get_expenses("variable")
variable_frame = variable_expenses[0]
variable_sub = variable_expenses[1]

# *** Printing Area ***

print()
print(variable_frame)
print()

print(f"\nVariable Costs: ${variable_sub:.2f}")