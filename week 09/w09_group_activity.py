
bank_accounts = []
balances = []

name_bank_account = ""
account_balance = ""

while name_bank_account != "quit":
    name_bank_account = input("What is the name of this account? ")

    if name_bank_account != "quit":
        account_balance = float(input("What is the balance? "))
        bank_accounts.append(name_bank_account)
        balances.append(account_balance)


#Loop through the lists using an index and display the name of the account with the balance next to it.
index = 0


print("Account Information:")
for i in balances:
    # print(f"{index} - Name Account: {bank_accounts[index]} Balance: {balances[index]}")
    print(f"{bank_accounts[index]} - ${balances[index]}")
    index = index + 1