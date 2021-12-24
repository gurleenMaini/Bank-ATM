class Atm:
    def __init__(self,cardnumber,pin):
        self.cardnumber = cardnumber
        self.pin = pin  

    def check_balance(self):
        print("Your balance is 80000")

    def withdrawl(self,amount):
        new_amount = 80000 - amount
        print("you have withdrawn amount "+str(amount)+"You're remaining amount is "+ str(new_amount))

def main():
    Card_number = input("Enter your card number: ")
    pin_number  = input("Enter your pin number: ")

    new_user = Atm(Card_number , pin_number)
    print("choose your activity")
    print(" 1.Check Balance  2.withdrawl")
    activity= int(input("Enter activity number: "))

    if (activity ==1):
        new_user.check_balance()
    elif (activity ==2):
        amount = int(input("Enter the amount: "))
        new_user.withdrawl(amount)
    else:
        print("Enter a valid number ")

if __name__== "__main__":
    main()
