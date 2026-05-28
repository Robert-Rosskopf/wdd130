""" #Compare numbers
number1=input("Please enter a number:")
number2=input("Please enter a another number:")
number1=float(number1)
number2=float(number2)
if number1==number2 :
    print("They are th1e same number!")
elif number1>number2 :
    print("The first number is greater")
else :
    print("The second number is greater") """


    #Loan Program
loan_size=input("how large is the loan?(1-10)")
loan_size=int(loan_size)
credit_history=input("how good is your credit history?(1-10)")
credit_history=int(credit_history)
income_level=input("how high is your income?(1-10)")
income_level=int(income_level)
downpayment_size=input("how large is your down payment?(1-10)")
downpayment_size=int(downpayment_size)
is_qualified=False
if loan_size>=5 :
    if credit_history >=7 and income_level >= 7 :
        is_qualified=True
    elif credit_history >= 7 or income_level >= 7 :
        if downpayment_size >= 5 :
            is_qualified=True
        elif :
            is_qualified=False
elif :
    if credit_history < 4 :
        is_qualified=False
    elif :
        if income_level>=7 or downpayment_size >= 7 :
            is_qualified = True
        elif income_level>=4 and downpayment_size >= 4 :
            is_qualified = True
        else :
            is_qualified = False
if is_qualified :
    print("You are qualified!")
else :
    print("You are not qualfied.")