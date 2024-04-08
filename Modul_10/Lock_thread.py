
from  threading import  Thread
from  threading import  Lock

class BankAccount(Thread):
    def __init__(self, account, *args, **kwargs):
        super(BankAccount, self).__init__(*args, **kwargs)
        self.account = account

    def deposit_task(self, amount):
        with lock:
            for _ in range(5):
                self.account += amount
                print(f'Deposited {amount}, new balance is {self.account}')

    def withdraw_task(self, amount):
        with lock:
            for _ in range(5):
                self.account -= amount
                print(f'Withdrew {amount}, new balance is {self.account}')

account = 1000
lock = Lock()
bankAccount = BankAccount(account=account)

bankAccount.deposit_task(100)
bankAccount.withdraw_task(150)


bankAccount.start()
bankAccount.join()

