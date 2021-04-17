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
            print("Account number should not be less than or more than 10 digits")
            return False
    
    else:
        print("account number is a required field")
        return False

def validate_registration_input(input):
    #check if it is a list
    #check each item in the list and be sure they are the correct data type
    pass
