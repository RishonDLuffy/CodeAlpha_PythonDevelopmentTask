#Simple stock Calculator
#By Rishon D'souza


#Few Declarations
import csv
availableStocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOGL": 2000,
    "MSFT": 330,
    "META": 300,
}
userStocks = {}



#Menu Loop
while True:
    print("1>View available stocks \n"                  #Menu
    "2>Add an investment \n" 
    "3>View your investments \n" 
    "4>Exit and Save investments \n")
    choice=input("Insert Choice (number):")

    if not choice.isdigit():                            #Checks if it's a number or letter
        print("Invalid, Enter single digit number choice.")
        continue

    if int(choice) == 1:                                #Choice 1,Print Predefined stocks
        print("Stock\tPrice")
        for stock, price in availableStocks.items():
            print(f"{stock}\t{price}")


    elif int(choice) == 2:                              #Choice 2,Input an investment
        newInvestment = input("Enter name of stock: ").upper()
        
        if newInvestment in availableStocks:            #Checks if its in predefined stocks
            while True:
                if newInvestment in userStocks:         #Checks if user already invested
                    print("You already own this stock.")
                    confirm = input("Do you want to update the quantity?(y/n): ").lower()
                    if confirm != "y" :
                        break

                quantity = input("Enter Quantity: ")
                if quantity.isdigit():
                    userStocks[newInvestment] = int(quantity)
                    print("Investment saved.")
                    break
                    

                else:
                    print("Enter a valid number.")
        else:
            print("Stock not found.")


    elif int(choice) == 3:                              #Choice 3,Displays User's investments
        print("Stock\tPrice\tQntty\tTotal")
        if userStocks == {}:                            #Prints this if no investement made
            print("--\t--\t--\t--")
        else:
            for stock,quantity in userStocks.items():
                
                print(f"{stock}\t{availableStocks[stock]}\t{quantity}\t{availableStocks[stock]*quantity}")


    elif int(choice) == 4:                              #Choice 4, Exit code and saves investment to a csv
        print("Saving and exiting.")
        with open("user_investments.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Stock", "Price", "Quantity", "Total"])
            for stock, quantity in userStocks.items():
                price = availableStocks[stock]
                writer.writerow([stock, price, quantity, price * quantity])
        print("Saved.")
        break


    else:                                                 #Any other invalid number choice
        print("Invalid, Enter single digit number choice.")
 