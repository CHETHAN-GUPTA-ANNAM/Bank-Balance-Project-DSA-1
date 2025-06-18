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
        print("\n\n")
        print(self.name," your account details are as followed: ")
        print(" ")
        print("User Name: ",self.name)
        print("User Account Number: ",self.number)
        print("User Mobile Number: ",self.mobile)
        print("Gender: ",self.gen)
        print("-------------------------")
        print("User Bank Balance: Rs.",self.balance)
        print("-------------------------")
        print(" \n\n")

        
name=str(input("Enter your name: "))
acc_num=str(input("Enter your account number(16 DIGIT): "))
while len(acc_num)!=16:
    print("Wrong account number! Enter again!!")
    print(" ")
    acc_num=str(input("Enter your account number again (16 DIGIT): "))
mobile=str(input("Enter your mobile number(10 DIGIT): "))
while len(mobile)!=10:
    print("Wrong mobile number! Enter again!!")
    print(" ")
    mobile=str(input("Enter your mobile number again:(10 DIGIT) "))
gender=input("Enter you gender M/F/B: ")
balance=int(input("Enter the initial ammount: "))
b1=Bank(name,acc_num,balance,mobile,gender)
a=str(input("Enter your requirement(Withdraw/Deposit/Check Balance/Exit): "))
while a!="Stop":
    if a== "Withdraw":
        amm=int(input("Enter the ammount to be withdrawl: "))
        s=b1.withdraw(amm)
        if s==0:
            b1.display()
        else:
            print("Please Try again")
        a=str(input("Enter your requirement(Withdraw/Deposit/Check Balance/Exit): "))
    elif a=="Deposit":
        amm=int(input("Enter the ammount to be deposited: "))
        b1.deposit(amm)
        b1.display()
        a=str(input("Enter your requirement(Withdraw/Deposit/Check Balance/Exit): "))
    elif a=="Check Balance":
        b1.display()
        a=str(input("Enter your requirement(Withdraw/Deposit/Check Balance/Exit): "))
    elif a=="Exit":
        print("\nThankyou! Have a nice day ",name)
        break
    else:
        print("\n This is case sensitive please enter exact option with correct cases!! ")
        a=str(input("Enter your requirement(Withdraw/Deposit/Check Balance/Exit): "))
