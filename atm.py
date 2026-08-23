while True:
    person=input("Enter your name")
    amount=int(input(f"Hello {person} Enter the withdrawl amount"))
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
        else:value=1
        count=remain//value
        if count>0:
            print(count, " notes of", value, " dispensed")
            remain=remain%value
        i+=1
    anwser=input(" Next user? (y/n)")
    if anwser.lower()=="y":
        continue
    else:
        break
