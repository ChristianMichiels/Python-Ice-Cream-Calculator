#This program calculates the cost of ice cream after tax, and tells you how much change you should recieve.
ice_cream_cost = input("How much did your ice cream cost?")
tax = .13
total_after_tax = float(ice_cream_cost) * float(tax) + float(ice_cream_cost)
#The next line rounds total_after_tax to the second decimal place
round_total_after_tax = round(total_after_tax, 2)
#Line 8 float converted to string so it can be read with "string"
print("after tax that comes to $" + str(round_total_after_tax))
cash = input("How much money did you give to the cashier for your ice cream?:")
cash_back = float(cash) - float(total_after_tax)
#The next line rounds cash_back to the second decimal place
cash_back_round = round(cash_back, 2)
print("The cashier should have given you $" + str(cash_back_round) + " back.")
input("Press enter to exit: ")

