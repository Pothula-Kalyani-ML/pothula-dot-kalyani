from grocery import Grocery
import yaml
from user import User


class Super_market():
    def __init__(self):
        self.available_grocery = []
        self.user=[]
   

    def sort_grocery(self):
        index=len(self.available_grocery)-1
        while index>0 and (self.available_grocery[index].price_per_unit < self.available_grocery[index-1].price_per_unit):
            self.available_grocery[index],self.available_grocery[index-1]=self.available_grocery[index-1],self.available_grocery[index]
            index -= 1     

    def add_grocery(self, grocery):
        for item in self.available_grocery:
            if item.name == grocery.name:
                item.price_per_unit = grocery.price_per_unit
                return 1
        self.available_grocery.append(grocery)
        self.sort_grocery()

    def display_available_products(self):
        print("products")
        for item in self.available_grocery:
            print(f" {item.name} , price: {item.price_per_unit}")
        print()


    def check_product_availability_update_quantity(self,product_name,product_quanitity):
        for index, grocery in enumerate(self.available_grocery):
            if grocery.name == product_name and grocery.no_of_units_available >= product_quanitity:
                order_price = product_quanitity*grocery.price_per_unit
                order_details = {"product_name":product_name,"quantity":product_quanitity,"price":order_price}
                return index ,order_details
        return print("item not available") 

    def in_budget_suggestions(self,budget_left):
        for item in self.available_grocery:
            if item.price_per_unit < budget_left:
                print(f"amount left can buy you  {item.name} , price: {item.price_per_unit}")
            elif item.price_per_unit > budget_left:
                break


    def user_options_and_access(self,user):
        try:
            user.budget = int(input("enter budget : "))
            user.budget_left=user.budget
            User.update_user_info_users(user)
            print("to add an item enter 1 ")
            print("to exit enter 0")
            user.option = input("enter an option : ")
            while user.option:
                try:
                    if int(user.option)==1:
                        print()
                        knl_super_market.display_available_products()
                        print()
                        try:
                            product_name = input("enter product name:")
                            product_quantity = int(input("enter quantity : "))
                            print()
                            index,order_details = knl_super_market.check_product_availability_update_quantity(product_name,product_quantity)
                            valid_purchase = User.user_purchase_and_budget_update(order_details,user)
                            if valid_purchase :
                                self.available_grocery[index].no_of_units_available -= product_quantity
                            else: 
                                print("insufficient budget")
                        except:
                            print("inavlid input")    
                    elif int(user.option)== 0:
                        print()
                        print("exit")
                        self.in_budget_suggestions(user.budget_left)                       
                        break    
                except: 
                    print("invalid option")
                print("to add an item enter 1 ")
                print("to exit enter 0")
                user.option=input("enter an option: ")
        except:
                print("invalid input")
                          


if __name__ == "__main__":
    knl_super_market = Super_market()
    with open('super_market.yaml') as file:
        try:
            database = yaml.safe_load(file)
            for data in database:
                grocery = Grocery(**data)
                knl_super_market.add_grocery(grocery)
        except yaml.YAMLError as exception:
            print(exception)
    

    user1=User()
    knl_super_market.user_options_and_access(user1)
    print()
    print(" purchased products by user ")
    print()
    user1.purchased_products()
    
