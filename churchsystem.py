# The %age of the church's offering
bills = 0.30
allowance = 0.40
member_needs = 0.20
miscellaneous = 0.10
bills_amount = input("Enter total for electricity and water bill amount")
Member_need = True

# The total amount of money collected
total_collected = input("Total Offerings")

# Calculate the amount collected for bills
bills_collected = bills * total_collected
print(f"Amount collected for bills: Ksh.{bills_collected}")

# Calculate the amount collected for the allowance
allowance_collected = allowance * total_collected
print(f"Amount collected for allowance: Ksh.{allowance_collected}")

# Calculate the amount collected for member needs
member_needs_collected = member_needs * total_collected
print(f"Amount collected for member needs: Ksh.{member_needs_collected}")

# Calculate the amount collected for miscellaneous
miscellaneous_collected = miscellaneous * total_collected
print(f"Amount collected for miscellaneous: Ksh.{miscellaneous_collected}")

def allocation():
    return {
        "Bills": bills_collected,
        "Allowance": allowance_collected,
        "Member Needs": member_needs_collected,
        "Miscellaneous": miscellaneous_collected,
        "Total Collected": total_collected
    }

def excess_bill():
    while True:
        if bills_amount < bills:
            excess_bill_balance = bills - bills_amount
            print(f"Excess bill balance: Ksh.{excess_bill_balance}")
        else:
            print("No Excess bill balance")
    return excess_bill

# Call the functions
print(total_collected)
