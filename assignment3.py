####
acc_bal = input("enter your acc bal")

if(int(acc_bal) > 100000 and int(acc_bal)<200000):
    acc_bal = int(acc_bal) - 25000
    print("we have deducted 25000")
elif (int(acc_bal) > 500000 and int(acc_bal) < 1000000):
    acc_bal = int(acc_bal) - (0.3 * int(acc_bal))
    print("we have deducted 30 percent from your account")
elif (int(acc_bal) > 1000000 ):
    acc_bal = int(acc_bal) - 15000
    print("we have deducted 15000")
