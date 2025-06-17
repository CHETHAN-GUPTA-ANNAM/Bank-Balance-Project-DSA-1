class Bank:
    def __init__(self,acc_name,acc_number,acc_balance,mobile_no,gender):
        self.name=acc_name
        self.number=acc_number
        self.balance=acc_balance
        self.mobile=mobile_no
        self.gen=gender
    def deposit(self,ammount):
        self.balance=self.balance+ammount
    def withdraw(self,ammount):
        if ammount>self.balance:
            print("Insufficient Bank Balnace")
            print("Here is your Balance details: ")
            self.display()
            return 1
        else:
            self.balance=self.balance-ammount
            return 0
    def display(self):
        print(" ")
        print(self.name," your account details are as followed: ")
        print(" ")
        print("User Name: ",self.name)
        print("User Account Number: ",self.number)
        print("User Mobile Number: ",self.mobile)
        print("Gender: ",self.gen)
        print("-------------------------")
        print("User Bank Balance: ",self.balance)
        print("-------------------------")
        print(" ")

        
name=str(input("Enter your name: "))
acc_num=str(input("Enter your account number: "))
while len(acc_num)!=12:
    print("Wrong account number! Enter again!!")
    print(" ")
    acc_num=str(input("Enter your account number again: "))
mobile=str(input("Enter your mobile number: "))
while len(mobile)!=10:
    print("Wrong mobile number! Enter again!!")
    print(" ")
    mobile=str(input("Enter your mobile number again: "))
gender=input("Enter M/F/B: ")
balance=int(input("Enter the balance ammount: "))
b1=Bank(name,acc_num,balance,mobile,gender)
a=str(input("Enter your requirement(Withdraw/Deposit/Check Balance/Stop): "))
while a!="Stop":
    if a== "Withdraw":
        amm=int(input("Enter the ammount to be withdrawl: "))
        s=b1.withdraw(amm)
        if s==0:
            b1.display()
        else:
            print("Please Try again")
        a=str(input("Enetr your requirement(Withdraw/Deposit/Check Balance/Stop): "))
    elif a=="Deposit":
        amm=int(input("Enter the ammount to be deposited: "))
        b1.deposit(amm)
        b1.display()
        a=str(input("Enetr your requirement(Withdraw/Deposit/Check Balance/Stop): "))
    elif a=="Check Balance":
        b1.display()
        a=str(input("Enetr your requirement(Withdraw/Deposit/Check Balance/Stop): "))
    elif a=="Stop":
        break
    
        
