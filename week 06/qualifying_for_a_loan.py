print("Hi! Be Welcome to our Loan Bot")
print("We'll ask you some questions to offer you the best option of our loans, ok? ")

loan_large_rate = int(input("From 1 to 10, how large is the loan? "))
cred_history_rate = int(input("From 1 to 10, how good is your credit history? "))
income_rate = int(input("From 1 to 10, how high is your income? "))
down_payment_rate = int(input("From 1 to 10, how large is your down payment? "))

is_loan_approved = False

if loan_large_rate >= 5:
    if cred_history_rate >= 7 and income_rate >= 7:
        print("Yes! 1")
        is_loan_approved = True
    elif cred_history_rate >= 7 or income_rate >= 7:
        if down_payment_rate >= 5:
            print("Yes! 2")
            is_loan_approved = True
        else:
            print("No! 2")
    else:
        print("No! 3")
elif cred_history_rate < 4:
    print("No! 4")
else:
    if income_rate >= 7 or down_payment_rate >=7:
        print("Yes! 3")
        is_loan_approved = True
    elif income_rate >= 4 and down_payment_rate >= 4:
        print("Yes! 4")
    else:
        print("No! 5")

if is_loan_approved:
    print("Your loan was approved!!")
else: 
    print("Your loan was not approved!")