from datetime import datetime
import sched
import time
from collections import defaultdict
# LEVEL 1: Balances

class Bank:
    def __init__(self):
        self.balance = {}
        self.users = []
        self.transaction_tracker = defaultdict(int)

    def create_account(self, user):
        self.users.append(user)
        self.balance[user] = 0.0
        self.transaction_tracker[user] = 0
        print(f"Account created for user {user}!")

    def deposit(self, user, amount):
        if amount<=0:
            raise ValueError("invalid amount")
            
        if user not in self.balance.keys():
            print(f"The user {user} does not have an account")
            print("Creating new account....")
            self.create_account(user)
            print("Account created!")
            print("Making deposit...")
            self.balance[user]+=amount
            print(f"Deposit success.\n New balance: {self.balance[user]}")
        else:
            self.balance[user] += amount
            print(f"Deposit sucess.\n New balance: {self.balance[user]}")
        self.transaction_tracker[user] += 1

        if self.transaction_tracker[user] >= 10:
            print(f"Congratulations {user}! You have made 10 transactions and earned a 2% bonus!")
            self.balance[user] += (amount * 0.02)
            self.transaction_tracker[user] = 0
            print(f"New balance after bonus: {self.balance[user]}")

    def withdraw(self,user, amount):
        if user not in self.users:
            raise ValueError("User does not have an account")
        else:
            if self.balance[user] < amount:
                raise ValueError("Insufficient balance to make withdrawal!")
            else:
                self.balance[user] -= amount
                print(f'Widthrawal success!\n New balance: {self.balance[user]}')
                self.transaction_tracker[user] += 1
        if self.transaction_tracker[user] >= 10:
            print(f"Congratulations {user}! You have made 10 transactions and earned a 2% bonus!")
            self.balance[user] += (amount * 0.02)
            self.transaction_tracker[user] = 0
            print(f"New balance after bonus: {self.balance[user]}")
            

# Level 2: Transfer
    def transfer(self, user_from, user_to, amount):
        if user_from not in self.users or user_to not in self.users:
            raise ValueError("One of the users does not have an account")
        elif self.balance[user_from] < amount:
            raise ValueError("Insufficient balance to make transfer")
        else:
            self.balance[user_from] -= amount
            self.balance[user_to] += amount
            print(f"Transfer success!\n New balance of {user_from}: {self.balance[user_from]}\n New balance of {user_to}: {self.balance[user_to]}")
            self.transaction_tracker[user_from] += 1
            self.transaction_tracker[user_to] += 1
        if self.transaction_tracker[user_from] >= 10:
            print(f"Congratulations {user_from}! You have made 10 transactions and earned a 2% bonus!")
            self.balance[user_from] += (amount * 0.02)
            self.transaction_tracker[user_from] = 0
            print(f"New balance after bonus: {self.balance[user_from]}")
        if self.transaction_tracker[user_to] >= 10:
            print(f"Congratulations {user_to}! You have made 10 transactions and earned a 2% bonus!")
            self.balance[user_to] += (amount * 0.02)
            self.transaction_tracker[user_to] = 0
            print(f"New balance after bonus: {self.balance[user_to]}")
# Level 3: Scheduled Tasks

    def schedule_payment(self, user_from, user_to, amount, datetime_time):
        target_time = datetime.strptime(datetime_time,"%Y-%m-%d %H:%M:%S").timestamp()

        scheduler = sched.scheduler(time.time,time.sleep)
        scheduler.enterabs(target_time,1,self.transfer,argument=(user_from,user_to,amount))
        print(f"Scheduled a transfer of {amount}, from {user_from} to {user_to}")
        scheduler.run()

       

        

if __name__ == "__main__":
    IandM_bank = Bank()

    IandM_bank.create_account("Bruno")
    IandM_bank.deposit('Bruno',2000000000)
    IandM_bank.deposit("Bruno",2000000)
    IandM_bank.withdraw('Bruno',9000)
    IandM_bank.create_account("Alice")
    print(IandM_bank.users)
    IandM_bank.deposit("Alice",5000)
    IandM_bank.transfer("Bruno","Alice",1000000)
    IandM_bank.transfer("Alice","Bruno",2000)
    print(IandM_bank.balance)


    # Schedule a payment (uncomment to test)
    IandM_bank.schedule_payment("Bruno","Alice",500,"2026-01-30 22:08:00")

    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    IandM_bank.transfer("Bruno","Alice",1000000)
    IandM_bank.transfer("Bruno","Alice",1000000)
    IandM_bank.transfer("Bruno","Alice",1000000)
    IandM_bank.transfer("Bruno","Alice",1000000)
    IandM_bank.transfer("Bruno","Alice",1000000)
    

    print(IandM_bank.transaction_tracker)



    
