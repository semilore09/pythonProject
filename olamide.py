class BankAccount:
    def __init__(self, AccNo, AccName, Accbalance):
        self.AccNo = AccNo
        self.AccName = AccName
        self.Accbalance = Accbalance
    def withdrawal(self):
     Amount=int(input("Input amount to withdraw"))
     if Amount <= self.Accbalance:
         print("Transaction successful \n Pls take your cash")
         print("your total balance is", self.Accbalance - Amount)
     elif Amount > self.Accbalance:
         print("Insufficient funds")
     else:
         print("Take your card")
    def Deposit(self):
        Amount1= (int(input("Enter amount to deposit")))
        print(Amount1, "has been successful deposited into your account")
        print("your total balance is",Amount1 + self.Accbalance)
    def Bankfees(self):
        fee= (0.05*self.Accbalance)
        print("your bank charges for the month", fee)
        print("your total balance is",self.Accbalance - fee)
    def Display(self):
        print("Your Account name is", self.AccName)
        print("Your Account number is", self.AccNo)
        print("Your total Balance stands at",self.Accbalance)
Account = BankAccount("0728268861","Olabisi Rejoice",100000)
Account.withdrawal()
Account.Deposit()
Account.Bankfees()
Account.Display()
#Inheritting a class
class customer(BankAccount):
    def __init__(self,AccNo, AccName, Accbalance):
        self.AccNo = AccNo
        self.AccName = AccName
        self.Accbalance = Accbalance
user1=customer(3425712016, "Rejoice Olabisi", 50000)
user1.withdrawal()




