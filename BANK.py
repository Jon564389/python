class BankAccount():
    def __init__(self, accountid, accountholder, totalbalance):
        self.accountid = accountid
        self.accountholder = accountholder
        self.totalbalance = totalbalance
    def show_details(self):
        print(self.accountholder)
        print(self.accountid)
        print(self.totalbalance)
    def withdraw(self):
        amount = int(input("How much would you like to withdraw?: "))
        if self.totalbalance < amount:
            print("Insufficient funds!")
        else:
            print("Withdrawel succesfully transacted!")
            self.totalbalance = self.totalbalance - amount
Account1 = BankAccount(647284627478, "James", 5400)
Account1.withdraw()
Account1.show_details()