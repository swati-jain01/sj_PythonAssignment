#creating list to store user details
card_num = [100001,102002,103003,104004,105005,106006,107007,108008,109009,110010]
name = ['Test','test2','test3','test4','test5','test6','test6','test8','test9','test10']
acc_no = [1111,2222,3333,4444,5555,6666,7777,8888,9999,1010]
balance = [10000,10000,10000,10000,10000,10000,10000,10000,10000,6000]
card_pin = [1111,2222,3333,4444,5555,6666,7777,8888,9999,1010]
acc_type = 'saving'

card = None
## Function to check the balance
def check_balance(card):
    crd_indx = card_num.index(card)
    acc_balance = balance[crd_indx]
    return acc_balance


## Function to handle withdrawl process
def withdrawl(amt):
    crd_indx = card_num.index(card)
    acc_balance = balance[crd_indx]
    updtd_balnc = acc_balance - amt
    return updtd_balnc


# Function to update the pin
def pin_change(otp):
    if otp in range(1000,9999,1):
        crd_indx = card_num.index(card)
        new_pin = int(input("Enter four digit valid number for new PIN: "))
        card_pin[crd_indx] = new_pin
        x = card_pin[crd_indx]
    else:
        x = "Invalid OTP"
    return x


print('Hello User\nWelcome to ATM')
try:
    card = int(input("Enter your 6 digit card number : "))
except Exception:
    try:
        card = int(input("Card number is not valid, Enter your 6 digit card number"))
    except Exception:
        print("Card number is not valid, You can retry again!!")



if card in card_num:
    #print(card)
    print("\nPlease select option from below Menu \n")
    print("1 for Check Balance\n2 for Withdrawal\n3 for PIN Change\n4 for Card Block")
    selection = int(input("Enter valid option : "))
    if selection == 1:
        acc_balance = check_balance(card)
        print("Your account balance is :", acc_balance)

    elif selection == 2:
        amt = int(input("Enter amount in term of 200 : "))
        if amt%200 == 0 and amt < check_balance(card):
            updtd_blnce = withdrawl(amt)
            print("Transaction successful, your updated balance is {}".format(updtd_blnce))
        elif amt > check_balance(card):
            print("Low Balance")
        else:
            print("Invalid amount entered")

    elif selection == 3:
        otp = int(input("Enter four digit valid OTP between 1000 to 9999 : "))
        x = pin_change(otp)
        if len(str(x)) == 4:
            print("PIN changed successfully, updated PIN is - ", x)
        else:
            print("Invalid OTP or entry for new PIN")

    elif selection == 4:
        otp = int(input("Enter four digit valid OTP between 1000 to 9999 : "))
        if otp in range(1000, 9999, 1):
            c = input("Please confirm \n'Y' for block\n'N' for exit - ")
            if c == 'Y':
                print("Your ATM card blocked successfully")
            else:
                print("Card is not blocked")
        else:
            print("Invalid OTP for new card block")
    else:
        print("You entered an invalid option, kindly re-insert your card and select valid options from menu, Thank You!!")
else:
    print("card number not found in database, please visit nearest branch for more details")
