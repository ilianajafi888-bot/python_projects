print("welcome to the tip calculator.")
bill = int(input("what was the total bill? $"))
tip = int(input("what percentage tip would you you like to give? 10 , 12 or 15\n"))
for_10 = bill * 1.10
for_12 = bill * 1.12
for_15 = bill * 1.15
people = int(input("how many people to split the bill?\n "))
bill_with_tip = tip / 100 * bill + bill

finall_bill = round(bill_with_tip, 2)
new_bill_with_tip = str(bill_with_tip)
pay = (finall_bill / people)
print(f"each person should pay ${pay}")
