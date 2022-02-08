def calculatePay():
    # Implement your solution in between the two comment blocks
    print("calculating pay")
    # This first line is provided for you
    try:
        sHours = input("Enter Hours: ")
        fHours = float(sHours)
        sRate = input("Enter Rate: ")
        fRate = float(sRate)
        if(fHours < 0 or fRate < 0):
            raise ArithmeticError
        pay = fHours * fRate
        print(pay)
    except ValueError:
        print("Error, please enter numeric input")
    except ArithmeticError:
        print("Error, please enter a value that is zero or greater")
    
    # end assignment

## if you want to test locally before you try to sync
## uncomment calculatePay() and run > python payCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
#calculatePay()