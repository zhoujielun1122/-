# 银行账户管理系统

class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount
        print(f"存款成功！当前余额为: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"取款成功！当前余额为: {self.balance}")
        else:
            print("余额不足！取款失败。")

    def check_balance(self):
        print(f"当前余额为: {self.balance}")

# 主程序
while True:
    print("\n选择操作:")
    print("1. 创建新账户")
    print("2. 存款")
    print("3. 取款")
    print("4. 查看余额")
    print("5. 退出")

    choice = input("请输入选项数字: ")

    if choice == '1':
        account_holder = input("请输入账户持有人姓名: ")
        initial_balance = float(input("请输入初始存款金额: "))
        account = BankAccount(account_holder, initial_balance)
        print("账户创建成功！")

    elif choice == '2':
        amount = float(input("请输入存款金额: "))
        account.deposit(amount)

    elif choice == '3':
        amount = float(input("请输入取款金额: "))
        account.withdraw(amount)

    elif choice == '4':
        account.check_balance()

    elif choice == '5':
        print("感谢使用！")
        break

    else:
        print("无效的选项，请重新输入！")
