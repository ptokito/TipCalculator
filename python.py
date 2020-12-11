print("welcome to the tip calculator!")
bill = float(input("What was the total bill? >>> $ "))
TIP_Percentage = float(input("How much would you like to tip? >>>"))
NumberOfGuest = int(input("How many are splitting the bill?>>> "))
bill_with_tip = TIP_Percentage / 100 * bill + bill
print(bill_with_tip)
bill_per_person = bill_with_tip / NumberOfGuest
final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay ${final_amount}")