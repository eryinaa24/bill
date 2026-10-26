SERVICE_CHARGE=0.1

bill=float(input("Enter bill amount in RM: "))
while bill<0 or bill>10000:
    print("Invalid bill amount. Please enter a non-negative bill number in a range 0 until 10000.")
    bill=float(input("Enter bill amount in RM: "))

person=int(input("Enter a number of person: "))
while person<1 or person>50:
    print("Invalid number of person. Please enter a number between 1 to 50.")
    person=int(input("Enter a number of person: "))

total_bill=bill+(bill*SERVICE_CHARGE)
each_pay=total_bill/person

#':' memulakan arahan format
#'.2f'memformatkan nombor perpuluhan kepada 2 tempat perpuluhan
print(f"Total bill amount with service charge is RM {total_bill:.2f}")
print(f"Each person need to pay RM {each_pay:.2f}")
