# ATM Management System

pin = "1234"
balance = 10000

print("===== Welcome to ATM =====")

entered_pin = input("Enter your 4-digit PIN: ")

if entered_pin == pin:

    while True:
        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            print("Your Current Balance is: ₹", balance)

        elif choice == "2":
            amount = float(input("Enter Deposit Amount: ₹"))

            if amount > 0:
                balance += amount
                print("Deposit Successful!")
                print("Updated Balance: ₹", balance)
            else:
                print("Invalid Amount!")

        elif choice == "3":
            amount = float(input("Enter Withdrawal Amount: ₹"))

            if amount <= balance:
                balance -= amount
                print("Please Collect Your Cash.")
                print("Remaining Balance: ₹", balance)
            else:
                print("Insufficient Balance!")

        elif choice == "4":
            print("Thank You for Using Our ATM.")
            break

        else:
            print("Invalid Choice! Please Try Again.")

else:
    print("Incorrect PIN!")