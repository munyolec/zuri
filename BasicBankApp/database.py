#create record
#read record
#update record
#delete record

#find user 
import os #allows for the deletion of a file
import validation
user_db_path="./data/user_record/"

def create(account_number,user_details):

    completion_state=False

    try:
        f=open(user_db_path +str(account_number) + ".txt","x")
        
    except FileExistsError:
        
        print("That user already exists")
        #delete the already created file, and print out an error, then return false
        #check file contents before deleting

        # delete(account_number)
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
    #find user with acc number
    #fetch the file content
    try:
        f=open(user_db_path+str(user_acc_number)+ ".txt", "r")
        # return f.readline()
    except FileNotFoundError:
        return "User not found"
    except FileExistsError:
        return "User does not exist"
    
    else:
        return f.readline()


def delete(user_acc_number):

    is_delete_successful = False
    
    if os.path.exists(user_db_path + str(user_acc_number) + ".txt"):
       
        try:

            os.remove(user_db_path + str(user_acc_number) + ".txt")
            is_delete_successful=True
        except FileNotFoundError:
            print("Users not found")  
        finally:
            return is_delete_successful


    #find user with acc number
    #delete the user record (file)
    #return true

def does_email_exist(user_acc_number, email):
    all_users = os.listdir(user_db_path) #list everything in the db folder
    for user in all_users:
        print("user printed --->")
        print(user)
        print("\n")
     
    
    
# create(3567909922,['Claire','Munyole','munyolec@gmail.com','password', 200])
# print(read(9766774101))
does_email_exist(9766774101,'wandavision@marvel.com')