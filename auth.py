#register

#-firstname,lastname,password, email
#-generate user id

#login
#-account number
#-account number and password

#bank operations

#initialize system
import random

database={
    1595892529:['Claire','Munyole','munyolec@gmail.com','123']
}

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

    is_valid_account_number=account_number_validation(accountNumberFromUser)

    if is_valid_account_number:

        passwordUser=input("Enter your password \n")

        for accountNumber, userDetails in database.items():
            if accountNumber==int(accountNumberFromUser):
                if userDetails[3]==passwordUser:
                    print("you are logged in")
                    bankOperation(userDetails)        
        
    print("Invalid details")
    login()

#validation
def account_number_validation(account_number):
    # check that acc number is not empty
    # check that acc number is 10 digits
    # check that acc number is an int

    if account_number:
        if len(str(account_number)) ==10:
            try:
                int(account_number)
            except ValueError:
                print("Invalid account number, account number should be an integer")
                return False
            except TypeError:
                print("Invalid account type")
                return False
        else:
            print("Account number should be 10 digits")
            return False
    
    else:
        print("account number is a required field")
        return False


    pass

def register():
    print("***** REGISTER ******")

    email=input("What is your email address? \n")
    first_name=input("What is your first name? \n")
    last_name=input("What is your last name? \n")
    password=input("Create a password \n")
    accountNumber=generateAccNumber()

    database[accountNumber]=[first_name,last_name,email,password]
    print("Your account has been created.")
    print("your account number is %d" % accountNumber)
    
    login()

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