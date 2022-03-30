
#Car Rental System
print("-----------------------------------------------------------------------CAR RENTAL SYSTEM-----------------------------------------------------------------------")
def main():
    print("\t Want a car on rent")
    print(" \n \t Please select car type ")
    print('''
         1.Family
         2.SUV
         3.Sedan
         4.Sports
         ''')
    customer_choice = input(" \t Enter your choice: ")
    if customer_choice == "Family":
        class family_cars:
            def __init__(self, car_name1, car_name2, car_name3):
                self.car_name1 = car_name1
                self.car_name2 = car_name2
                self.car_name3 = car_name3

            def fc(self):
                print("\t 1.Suzuki", self.car_name1)
                print("\t 2.TATA", self.car_name2)
                print("\t 3.Hyundai", self.car_name3)

        class car_stock(family_cars):
            def __init__(self, car_name1, car_name2, car_name3, s1, s2, s3):
                super().__init__(car_name1, car_name2, car_name3)
                self.s1 = s1
                self.s2 = s2
                self.s3 = s3

            def show_stock(self):
                print("\n \t Available stock")
                print("\t ", self.car_name1, ":", self.s1)
                print("\t ", self.car_name2, ":", self.s2)
                print("\t ", self.car_name3, ":", self.s3)

        stock_obj = car_stock("swift", "NEXON", "i20", 20, 40, 25)
        print("\n \t Available cars")
        stock_obj.fc()

        print("\n \t Want to see stock")
        stock_choice = input("\t Enter your choice(in caps):")
        if stock_choice == "YES":
            stock_obj.show_stock()
        else:
            pass
        car_on_rent = input("\n \t Which car you want on rent: ")
        if car_on_rent == "swift":
            Rent = 1000
            print("\t Rent: 1000/Day")
            quantity = int(input("\n \t Enter total number of car which you want on rent: "))
            rent_days = int(input("\t Enter no. of days for rent: "))
            customer_name = input("\t Enter you name: ")
            customer_no = int(input("\t Enter your mobile number: "))
            Rent_Bill = Rent * quantity * rent_days
            print("\n \t Your total rent bill: ", Rent_Bill)
        elif car_on_rent == "NEXON":
            Rent = 2000
            print("\t Rent: 2000/Day")
            quantity = int(input("\n \t Enter number of car which you want on rent: "))
            rent_days = int(input("\t Enter no. of days for rent: "))
            customer_name = input("\t Enter you name: ")
            customer_no = int(input("\t Enter your mobile number: "))
            Rent_Bill = Rent * quantity * rent_days
            print("\n \t Your total rent bill: ", Rent_Bill)
        elif car_on_rent == "i20":
            Rent = 1500
            print(" Rent: 1500/Day")
            quantity = int(input("\n \t Enter number of car which you want on rent: "))
            rent_days = int(input("\t Enter no. of days for rent: "))
            customer_name = input("\t Enter you name: ")
            customer_no = int(input("\t Enter your mobile number: "))
            Rent_Bill = Rent * quantity * rent_days
            print("\n \t Your total rent bill: ", Rent_Bill)
        else:
            print("\t This car is not available yet")
            print("\t Please select from above stock")


    elif customer_choice == "SUV":
        class SUV_cars:
            def __init__(self, car_name1, car_name2, car_name3):
                self.car_name1 = car_name1
                self.car_name2 = car_name2
                self.car_name3 = car_name3

            def fc(self):
                print("\t 1.Hyundai", self.car_name1)
                print("\t 2.TATA", self.car_name2)
                print("\t 3.Toyota", self.car_name3)

        class car_stock(SUV_cars):
            def __init__(self, car_name1, car_name2, car_name3, s1, s2, s3):
                super().__init__(car_name1, car_name2, car_name3)
                self.s1 = s1
                self.s2 = s2
                self.s3 = s3

            def show_stock(self):
                print("\t ", self.car_name1, ":", self.s1)
                print("\t ", self.car_name1, ":", self.s2)
                print("\t ", self.car_name1, ":", self.s3)

        stock_obj = car_stock("creta", "HARRIER", "FORTUNER", 20, 20,15)
        print("\n \t Available cars")
        stock_obj.fc()
        print("\n \t Want to see stock")
        stock_choice = input("\t Enter your choice(in caps):")
        if stock_choice == "YES":
            stock_obj.show_stock()
        else:
            pass
        car_on_rent = input("\n \t Which car you want on rent: ")
        if car_on_rent == "creta":
            Rent = 3000
            print("\t Rent: 3000/Day")
            quantity = int(input("\n \t Enter number of car which you want on rent: "))
            rent_days = int(input("\t Enter no. of days for rent: "))
            customer_name = input("\t Enter you name: ")
            customer_no = int(input("\t Enter your mobile number: "))
            Rent_Bill = Rent * quantity * rent_days
            print("\n \t Your total rent bill: ", Rent_Bill)
        elif car_on_rent == "HARRIER":
            Rent = 5000
            print("\t Rent: 5000/Day")
            quantity = int(input("\n \t Enter number of car which you want on rent: "))
            rent_days = int(input("\t Enter no. of days for rent: "))
            customer_name = input("\t Enter you name: ")
            customer_no = int(input("\t Enter your mobile number: "))
            Rent_Bill = Rent * quantity * rent_days
            print("\n \t Your total rent bill: ", Rent_Bill)
        elif car_on_rent == "FORTUNER":
            Rent = 6000
            print("\t Rent: 6000/Day")
            quantity = int(input("\n \t Enter number of car which you want on rent: "))
            rent_days = int(input("\t Enter no. of days for rent: "))
            customer_name = input("\t Enter you name: ")
            customer_no = int(input("\t Enter your mobile number: "))
            Rent_Bill = Rent * quantity * rent_days
            print("\n \t Your total rent bill: ", Rent_Bill)
        else:
            print("\t This car is not available yet")
            print("\t Please select from above stock")


    elif customer_choice == "Sedan":
        class Sedan_cars:
            def __init__(self, car_name1, car_name2, car_name3):
                self.car_name1 = car_name1
                self.car_name2 = car_name2
                self.car_name3 = car_name3

            def fc(self):
                print("\t 1.Suzuki", self.car_name1)
                print("\t 2.Hyundai", self.car_name2)
                print("\t 3.Honda", self.car_name3)

        class car_stock(Sedan_cars):
            def __init__(self, car_name1, car_name2, car_name3, s1, s2, s3):
                super().__init__(car_name1, car_name2, car_name3)
                self.s1 = s1
                self.s2 = s2
                self.s3 = s3

            def show_stock(self):
                print("\t ", self.car_name1, ":", self.s1)
                print("\t ", self.car_name1, ":", self.s2)
                print("\t ", self.car_name1, ":", self.s3)

        stock_obj = car_stock("Ciaz", "verna", "City", 15, 20, 10)
        print("\n \t Available cars")
        stock_obj.fc()
        print("\n \t Want to see stock")
        stock_choice = input("\t Enter your choice(in caps):")
        if stock_choice == "YES":
            stock_obj.show_stock()
        else:
            pass
        car_on_rent = input("\n \t which car you want on rent: ")
        if car_on_rent == "Ciaz":
            Rent = 6000
            print("\t Rent: 6000/Day")
            quantity = int(input("\n \t Enter number of car which you want on rent: "))
            rent_days = int(input("\t Enter no. of days for rent: "))
            customer_name = input("\t Enter you name: ")
            customer_no = int(input("\t Enter your mobile number: "))
            Rent_Bill = Rent * quantity * rent_days
            print("\n \t Your total rent bill: ", Rent_Bill)
        elif car_on_rent == "verna":
            Rent = 6500
            print("\t Rent: 6500/Day")
            quantity = int(input("\n \t Enter number of car which you want on rent: "))
            rent_days = int(input("\t Enter no. of days for rent: "))
            customer_name = input("\t Enter you name: ")
            customer_no = int(input("\t Enter your mobile number: "))
            Rent_Bill = Rent * quantity * rent_days
            print("\n \t Your total rent bill: ", Rent_Bill)
        elif car_on_rent == "City":
            Rent = 6000
            print("\t Rent: 6000/Day")
            quantity = int(input("\n \t Enter number of car which you want on rent: "))
            rent_days = int(input("\t Enter no. of days for rent: "))
            customer_name = input("\t Enter you name: ")
            customer_no = int(input("\t Enter your mobile number: "))
            Rent_Bill = Rent * quantity * rent_days
            print("\n \t Your total rent bill: ", Rent_Bill)
        else:
            print("\t This car is not available yet")
            print("\t Please select from above stock")


    elif customer_choice == "Sports":
        class Sports_cars:
            def __init__(self, car_name1, car_name2, car_name3):
                self.car_name1 = car_name1
                self.car_name2 = car_name2
                self.car_name3 = car_name3

            def fc(self):
                print("\t 1.Audi", self.car_name1)
                print("\t 2.Ford", self.car_name2)
                print("\t 3.Porsche", self.car_name3)

        class car_stock(Sports_cars):
            def __init__(self, car_name1, car_name2, car_name3, s1, s2, s3):
                super().__init__(car_name1, car_name2, car_name3)
                self.s1 = s1
                self.s2 = s2
                self.s3 = s3

            def show_stock(self):
                print("\t ", self.car_name1, ":", self.s1)
                print("\t ", self.car_name1, ":", self.s2)
                print("\t ", self.car_name1, ":", self.s3)

        stock_obj = car_stock("R8", "Mustang", "911", 10,5,7)
        print("\n \t Available cars")
        stock_obj.fc()
        print("\n \t Want to see stock")
        stock_choice = input("\t Enter your choice(in caps):")
        if stock_choice == "YES":
            stock_obj.show_stock()
        else:
            pass
        car_on_rent = input("\n \t which car you want on rent: ")
        if car_on_rent == "R8":
            Rent = 15000
            print("\t Rent: 15000/Day")
            quantity = int(input("\n \t Enter number of car which you want on rent: "))
            rent_days = int(input("\t Enter no. of days for rent: "))
            customer_name = input("\t Enter you name: ")
            customer_no = int(input("\t Enter your mobile number:"))
            Rent_Bill = Rent * quantity * rent_days
            print("\n \t Your total rent bill: ", Rent_Bill)
        elif car_on_rent == "Mustang":
            Rent = 20000
            print("\t Rent: 20000/Day")
            quantity = int(input("\n \t Enter number of car which you want on rent: "))
            rent_days = int(input("\t Enter no. of days for rent: "))
            customer_name = input("\t Enter you name: ")
            customer_no = int(input("\t Enter your mobile number: "))
            Rent_Bill = Rent * quantity * rent_days
            print("\n \t Your total rent bill: ", Rent_Bill)
        elif car_on_rent == "911":
            Rent = 18000
            print("\t Rent: 18000/Day")
            quantity = int(input("\n \t Enter number of car which you want on rent: "))
            rent_days = int(input("\t Enter no. of days for rent: "))
            customer_name = input("\t Enter you name: ")
            customer_no = int(input("\t Enter your mobile number:"))
            Rent_Bill = Rent * quantity * rent_days
            print("\n \t Your total rent bill: ", Rent_Bill)
        else:
            print("\t This car is not available yet")
            print("\t Please select from above stock")


    else:
        print("Connection Error")

    print("---------------------------------------------------------------------Thankyou for visiting---------------------------------------------------------------------")
    main()

main()
