# The %age of the church's offering
bills = 0.30
allowance = 0.50
member_needs = 0.10
miscellaneous = 0.10
bills_amount = int(input("Enter total bill amount for electricity and water : "))

# The total amount of money collected
total_collected = int(input("Total Offerings:\nKsh."))

# Calculate the amount collected for bills
bills_collected = bills * total_collected
print(f"Amount collected for bills: \nKsh.{bills_collected}")

# Calculate the excess bill balance if the amount collected for bills is less than or equal to the bills amount
def calculate_excess_balance():
    if bills_amount < bills_collected:
        excess_bill_balance = bills_collected - bills_amount
        print(f"Excess balance for bills is : \nKsh.{excess_bill_balance}")
    else:
        print("No Excess bill balance")
    return 0

excess_balance = calculate_excess_balance()

# Calculate the amount collected for the allowance
allowance_collected = allowance * total_collected
print(f"Amount collected for Bishop: \nKsh.{allowance_collected}")

# Calculate the amount collected for miscellaneous
miscellaneous_collected = miscellaneous * total_collected
print(f"Amount collected for miscellaneous: \nKsh.{miscellaneous_collected}")

# Calculate the miscellaneous used up

def miscellaneous_rem():
    mis = int(input("Enter amount used for miscellaneous activity: \nKsh. "))
    if mis < miscellaneous_collected:
        miscellaneous_used_up = miscellaneous_collected - mis
        print(f"Miscellaneous used up: \nKsh.{miscellaneous_used_up}")
    else:
        print(f"Stay in Budget please!")
        overdraw = mis - miscellaneous_collected
        if overdraw <= excess_balance:
            new_excess = excess_balance - overdraw
            print(f"Ksh.{overdraw} has been used from the excess bill balance")
            print(f"The new excess balance is now Ksh.{new_excess}")
        else:
            print(f"Overdraw exceeds the available excess balance amount by Ksh.{overdraw - excess_balance}")

miscellaneous_rem()


# Calculate the amount collected for member needs
member_needs_collected = member_needs * total_collected
print(f"Amount collected for member needs: \nKsh.{member_needs_collected}")
print(input("Press enter to input number of needy members."))

# Calculate the amount for giving needy members
def za_member():
    number = int(input("Number of members needing help: "))
    if number > 0:
        wape = member_needs_collected/number
        print(f"Give each needy member: Ksh.{wape}")
    else:
        saved = member_needs_collected + miscellaneous_collected
        print(f"No need for giving to needy members. Instead, save \nKsh.{saved}")
    return
za_member()

print("#In His Presence!")