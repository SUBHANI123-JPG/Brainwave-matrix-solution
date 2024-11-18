print("welcome to the canara bank \n\nInsert your card")

password = 1234
balance = 10000
choice = 0

print("welcome to the canara bank ATM")
pin = int(input("please Enter your four digit pin \n"))
if pin == password:
    print("logged in successfully")

while pin != password:
         print("invalid pin and try again")
         break

while choice != 5:

        print("\n\n **** Menu ****")
        print("1 == balance enquiry")
        print("2==deposit")
        print("3==withdraw")
        print("4==change_pin")
        print("5==cancel \n")

        choice = int(input("\n Enter your option:\n"))


        if choice ==1:
            print("balance = $",balance)
        elif choice==2:
            dep = int(input("Enter your deposit:$"))
            balance +=dep
            print("\n Enter your deposited amount:$",dep)
            print("Available Balance=$",balance)

        elif choice ==3:
            wit = int(input("Enter the amoount to withdraw:$"))

            balance -=wit
            print("\n withdrawn amount:$",wit)
            print("Available Balance = $",balance)

        elif choice==4:
            current_pin = int(input("Enter your current pin:"))

            if current_pin==password:
                new_pin = int(input("Enter your new 4-digit pin,"))
                confirm_pin=int(input("confirm your new pin"))

                if new_pin == confirm_pin:
                    password = new_pin
                    print("pin changed successfully")
                else:
                    print("pin do not match or invalid pin format")
            else:
                print("Incorrect pin")


        elif choice==5:
                print("Thank you for visiting to our canara bank ATM:")
