balance= 15000;

class Atm:
    def __init__ (self, card_no, pin_no):
        self.card_no = card_no;
        self.pin_no = pin_no;

def CheckBalance(self):
    print("Your balance is ", balance);

def CashWidrawal(self, amount):
    new_amount= balance - amount;
    print("You have widrawn amount " + str(amount) + ". Your remaining balance is" + str(new_amount));

def main():
    card_number = input("Enter your card number: ");
    pin_number  = input("Enter your pin number: ");

    new_user =  Atm(card_number ,pin_number);

    print("Please choose your activity: ");
    print("1.Check Your Balance");
    print("2.Withdrawl");
    activity = int(input("Enter activity number: "));

    if (activity == 1):
        new_user.check_balance();
    elif (activity == 2):
        amount = int(input("Enter the amount to be widrawn: "));
        new_user.withdrawl(amount);
    else:
        print("Please enter a valid number");

main()