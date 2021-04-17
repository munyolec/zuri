import datetime
now = datetime.datetime.now()

name= input("what is your name?\n")
allowedUsers=['Seyi','Mike','Love']
allowedPassword=["passwordSeyi","passwordMike","passwordLove"]

if name in allowedUsers:
    password=input("your password?\n")
    userId=allowedUsers.index(name)
    if password==allowedPassword[userId]:
        print ("Welcome %s" %name)
        print ("The current date and time is:")
        print (now.strftime("%Y-%m-%d %H:%M:%S"))

        print("These are the available options:")
        print("1. Withdrawal")
        print("2. Cash Deposit")
        print("3. Complaint")

        selectedOption=int(input("Please select an option: "))

        if selectedOption==1:
            print("you selected option %s" %selectedOption)
            withdrawAmount=int(input("How much would you like to withdraw? "))
            print("Take your cash: %s" %withdrawAmount)
            
        elif selectedOption==2:
            print("you selected option %s" %selectedOption)
            depositAmount=int(input("How much would you like to deposit? "))
            print("Your current balance is: %s" %depositAmount)            
            
        elif selectedOption==3:
            print("you selected option %s" %selectedOption)
            complaint=input("What issue would you like to report?")
            print("Thank you for contacting us")
            pass
        else:
            print("Invalid option selected, please try again")
    else:
        print("Password incorrect, please try again")
else:
    print("Name not found, please try again")
