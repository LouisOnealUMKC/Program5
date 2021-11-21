#Louis ONEAL
#CS 101
#Program 5


class House:
    def __init__(self, year = 0, price = 0,location = 'none'):
        self.YearBuilt = int(year)
        self.price = int(price)
        self.location = location
        self.currentValue = 0

    #Sets its current value to calculated thing
    def Calculate_Current_Value(self, currentYear):       
        Appreciation_Rate = 0.08
        self.currentValue = int(self.price * (pow((1 + Appreciation_Rate),(int(currentYear) - self.YearBuilt))))
    
    def __str__(self):
        return f'House Information:\n\tYear Built: {self.YearBuilt}\n\tPurchase Price: {self.price}\n\tCurrent Value of House: {self.currentValue}\n\tLocation: {self.location}'
        

    def Money_earned(self):
        return int(self.currentValue - self.price)
    #self, year, price, location, value

def Main():
    YearBuilt = input("Enter House model year: ")
    while (int(YearBuilt) < 0):
        print("Enter a valid Year")
        YearBuilt = input("Enter House model year: ")
    
    Price = input("Price of the house: ")
    while (int(Price) <= 0):
        print("Enter a valid price")
        Price = input("Price of the house: ")

    CurrentYear = input("Enter the correct current year: ")
    while (int(CurrentYear) != 2021):
         CurrentYear = input("Enter the correct current year: ")
    
    Location = input("Enter your house Location: ")
    while Location == "":
        print("Enter a valid Location")
        Location = input("Enter your house Location: ")     

    myHouse = House(YearBuilt, Price, Location)
    myHouse.Calculate_Current_Value(CurrentYear)
    print(myHouse)
    print('Total value you will earn:\n', myHouse.Money_earned())
    anotherGo = input("Do you want to try another house? (Y/N)")
    while(anotherGo.upper() != 'Y' and anotherGo.upper() != 'N' ):
            anotherGo = input("Valid inputs are Y or N. \n Do you want to try another house? (Y/N)")
    
    if(anotherGo.upper() == 'Y'):
        Main()
    else:
        return


# STARTO
Main()
    


