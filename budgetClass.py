
class Budget():  
    def __init__(self):        
        self.categories={'food':0,
            'entertainment':0,
            'clothing':0 }

    def deposit(self, deposit_amount, category):
        self.categories[category.lower()] = self.categories[category.lower()] + deposit_amount
    
    def withdraw(self,withdraw_amount,category):
        self.categories[category.lower()]=self.categories[category.lower()]-withdraw_amount
    
    def balance(self,category):
        bal=self.categories[category.lower()]
        print(f"Your balance for {category} is {bal}")

       
    def transfer(self,category,amount,category2):
        self.categories[category.lower()]=self.categories[category.lower()] -amount
        self.categories[category2.lower()]=self.categories[category2.lower()] +amount

        

def main():
    cat_map = {
        1: 'food',
        2: 'entertainment',
        3: 'clothing'
    }
    new_budget = Budget()     #instance of the class Budget
    print("Welcome \n")
    selection=(int(input("Select a category: Food (1) Clothing (2) Entertainment (3): \n")))
    option_values=[1,2,3]
    if selection not in option_values:
        print("Invalid Option, Please try again")
        main()

    option=int(input(f"What would you like to do to the {cat_map[selection]} Category? : Deposit (1) Withdraw (2) Check balance (3) Transfer funds (4) \n"))
    if option == 1:
        a=int(input("Enter the amount you would like to deposit: \n"))
        new_budget.deposit(a,cat_map[selection])
        print(new_budget.categories)
    if option ==2:
        b = int(input("How much would you like to withdraw? : \n"))
        new_budget.withdraw(b,cat_map[selection])
        print(new_budget.categories)
    if option==3:
        new_budget.balance(cat_map[selection])
        # print(new_budget.categories)
        
    if option==4:
        isValidOption=False
        while isValidOption==False:
            transfer_from=int(input("Transfer from :Food (1) Clothing (2) Entertainment (3) \n"))
            if transfer_from not in option_values:
                print("Invalid Option, Please try again")
                # isValidOption=False
            else:
                transfer_to=int(input("Transfer to: Food (1) Clothing (2) Entertainment (3)"))
                if transfer_to not in option_values:
                    print("Invalid Option, Please try again")
                else:
                    isValidOption=True
                    transfer_amount=int(input(f"How much would you like to transfer from the {cat_map[transfer_from]} to the {cat_map[transfer_to]}? \n"))
                    new_budget.transfer(cat_map[transfer_from],transfer_amount,cat_map[transfer_to])
                    print(new_budget.categories)

main()
