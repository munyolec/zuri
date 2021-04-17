#create record
#read record
#update record
#delete record

#find user 

def create(account_number,user_details):

    completion_state=False

    try:
        f= open("BasicBankApp/data/user_record/" +str(account_number) + ".txt","x")
        
    except FileExistsError:
        
        print("That user already exists")
        #delete the already created file, and print out an error, then return false
        return completion_state
        f.close()

    else:
        f.write(str(user_details))
        f.close()
        completion_state=True

    # finally:
    #     f.close()

    return completion_state



    #create a file
    #name of the file would be an account_number.txt
    #add the user details to the file
    #return true
    #if saving to file fails, then delete created file



def update(user_acc_number):
    print("update a new user record")
    #find user with acc number
    #fetch the file content
    #update the file content
    #save the file

def read(user_acc_number):
    print("read user record")
    #find user with acc number
    #fetch the file content

def delete(user_acc_number):
    print("delete user record")
    #find user with acc number
    #delete the user record (file)
    #return true

def find(user_acc_number):
    print("find user")
    #find user record in the data folder
    

# create(3567909922,['Claire','Munyole','munyolec@gmail.com','password', 200])