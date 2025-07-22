# print( "Welcome to the python tip calculator!" )
# bill = float(input("What was the total bill? $"))
# tip_percent = int(input( "What percentage tip would you like to give? 10 12 15 " )) /100
# tip_amount = bill * tip_percent
# people = int(input( "How many people to split the bill? " ))
# amount = (bill + tip_amount) / people
# amount = f"{amount:.2f}"
# print( amount )

print( "Welcome to the python tip calculator!")
bill = float(input("What was the total bill? $"))
tip_percent = int(input( "What percentage tip would you like to give? 10 12 15 " ))
people = int(input( "How many people to split the bill? " ))
final_bill = bill * ((tip_percent / 100 )+ 1)
amount_per_person = final_bill / 5
amount_per_person = f"{amount_per_person:.2f}"
print(amount_per_person)