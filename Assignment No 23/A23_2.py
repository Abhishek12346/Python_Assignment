class BankAccount:
    RIO=10.5

    def __init__(self,Name,Amount):
        self.Name=Name
        self.Amount=Amount

    def  display(self):
        print("Account Holder Name=>",self.Name)
        print("Amount of Account=>",self.Amount)


    def Deposit(self):
        print("-"*45)
        Deposit_Money=int(input("Enter the Amoount of Deposit=>"))
        self.Amount=self.Amount+ Deposit_Money
        print("Deposit Balance Completed")
        print("-"*45)


    def Withdraw(self):
        WithDrawl_Money = int(input("Enter amount to withdraw => "))
        if WithDrawl_Money <= self.Amount:
            self.Amount = self.Amount - WithDrawl_Money
            print("withdrawal Amount is successfully")
        else:
            print("Insufficient balance ")

    def CalculateInterest(self):
        Interest = (self.Amount * BankAccount.RIO) / 100
        return Interest
    

B1=BankAccount("Abhishek",10000)

B1.display()
B1.Deposit()
B1.Withdraw()
print("-"*45)
print("Interest Total",B1.CalculateInterest())

