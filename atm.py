print("Welcome to Access Bank \n pls insert your card")
print("Insert your Pin")
pin = input()
if len(pin) == 4:
    pin = int(pin)
    print("""
    ENTER 1 >>>  WITHDRAWAL
    ENTER 2 >>>  CHECK BALANCE
    ENTER 3 >>> TRANSFER
    ENTER 4 >>> BUY AIRTIME
    """)
    Choice = int(input())
    if Choice == 1:
        print("""
        ENTER 1 >>> SAVINGS
        ENTER 2 >>> CURRENTS
        ENTER 3 >>> CREDIT
        ENTER 4 >>> NOT SURE
        """)
        Choice1 = int(input())
        if Choice1 == 1:
            print("""
        ENTER 1 >>> 1000
        ENTER 2 >>> 10000
        ENTER 3 >>> 20000
        ENTER 4 >>>  OTHERS
            """)
            Choice2 = int(input())
            if Choice2 == 1:
                print("""Pls take your cash 
                Would you like to perform another transaction
                ENTER 1 >> YES
                ENTER 2 >>NO""")
                Choice3 = int(input())
                if Choice3 == 1:
                    print("""
                    ENTER 1 >>>  WITHDRAWAL
                    ENTER 2 >>>  CHECK BALANCE
                    ENTER 3 >>> TRANSFER
                    ENTER 4 >>> BUY AIRTIME
                    """)
                else:
                    print("Thank you for choosing Access Bank \nKindly take your card")
            else:
                print("Thank you for choosing Access Bank \nKindly take your card")
        else:
            print("Service are not available now \nKindly take your card ")
    else:
        print("Thanks for choosing Access Bank \nKindly take your card ")
else:
    print("Incorrect Pin \n Please Retry")
