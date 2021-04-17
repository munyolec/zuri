#register

#-firstname,lastname,password, email
#-generate user id

#login
#-account number
#-account number and password

#bank operations

#initialize system
import random
import datetime
import validation
import database

# database={
#     1111111111:['Claire','Munyole','munyolec@gmail.com','password',200]
#     }

def init():
    print("Welcome to bankPHP")
    haveAccount= int(input("Do you have an account with us? : 1(yes) or : 2(no) \n"))
    if haveAccount==1:
        login()
    elif haveAccount==2:
        print(register())
    else:
        print("Invalid option selected")
        init()

def login():
    print("********** Login **********")

    accountNumberFromUser=input("Enter your account number \n")

    is_valid_account_number=validation.account_number_validation(accountNumberFromUser)

    if is_valid_account_number:

        passwordUser=input("Enter your password \n")

        for accountNumber, userDetails in database.items():
            if accountNumber==int(accountNumberFromUser):
                if userDetails[3]==passwordUser:
                    print("you are logged in")
                    bankOperation(userDetails)        
        
        print("Invalid account number or password")
        login()
    else:
        init()


def register():
    print("***** REGISTER ******")

    email=input("What is your email address? \n")
    first_name=input("What is your first name? \n")
    last_name=input("What is your last name? \n")
    password=input("Create a password \n")

    accountNumber=generateAccNumber()

    # database[accountNumber]=[first_name,last_name,email,password]
    is_user_created=database.create(accountNumber,[first_name,last_name,email,password])

    if is_user_created:
        print("Your account has been created.")
        print("="*100)
        print("your account number is %d" % accountNumber)
        print("="*100)
        
        login()
    else:
        print("something went wrong, please try again")
        register()

def bankOperation(user):

    print("Welcome %s %s" % (user[0], user[1]))

    option=int(input("What would you like to do? (1) Deposit (2) Withdraw (3)Logout "))
    if option ==1:
        deposit()
    elif option ==2:
        withdrawal()
    elif option ==3:
        logout()
    elif option ==4:
        exit()
    else:
        print("Invalid option selected")
        bankOperation(user)

def withdrawal():
    print("Withdrawal operation")

def deposit():
    print("deposit operation")

def generateAccNumber():
    return random.randrange(1111111111,9999999999)

def logout():
    login()

#INITIALISE SYSTEM 
init()
# print(generateAccNumber())
# print(database)