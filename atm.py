while True:
    person=input("Enter your name")
    amount=int(input("Hello", person, "Enter the withdrawl amount"))
if amount<=0:
    print("Ivalid amount, try again")
else:
    print("Dispensing", amount, "for", person)
remain=amount
i=1
while i<=5:
    if i==1:value=100
    elif i==2:value=50
    elif i==3:value=20
    elif i==4:value=10
    elif i==5:value=1
    count=amount//value
    if count>0:
        print(count, " notes of", value, " dispensed")
        remaining=remaining%value
    anwser=input(" Next user? (y/n)")
    if awnser.lower()=="y":
        continue
    else:
        break
