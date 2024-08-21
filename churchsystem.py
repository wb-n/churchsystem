# The %age of the church's offering
bills = 0.30
allowance = 0.40
member_needs = 0.20
miscellaneous = 0.10
bills_amount = int(input("Enter total for electricity and water bill amount: "))

# The total amount of money collected
total_collected = int(input("Total Offerings: "))

# Calculate the amount collected for bills
bills_collected = bills * total_collected
print(f"Amount collected for bills: Ksh.{bills_collected}")

# Calculate the excess bill balance if the amount collected for bills is less than or equal to the bills amount
def calculate_excess_balance():
    if bills_amount <= bills_collected:
        excess_bill_balance = bills_collected - bills_amount
    else:
        print("No Excess bill balance")
    return excess_bill_balance
excess = calculate_excess_balance()
print(f"Excess balance for bills is : Ksh.{excess}")

# Calculate the amount collected for the allowance
allowance_collected = allowance * total_collected
print(f"Amount collected for Bishop: Ksh.{allowance_collected}")

# Calculate the amount collected for member needs
member_needs_collected = member_needs * total_collected
print(f"Amount collected for member needs: Ksh.{member_needs_collected}")
def member_needs_collected():


# Calculate the amount collected for miscellaneous
miscellaneous_collected = miscellaneous * total_collected
print(f"Amount collected for miscellaneous: Ksh.{miscellaneous_collected}")
