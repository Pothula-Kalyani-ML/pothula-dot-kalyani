


class User():
    users=[]
    user_count=0
    def __init__(self):
        self.user_id=User.user_count
        self.budget=0
        self.grocery_purchased_by_user=[]
        self.budget_left=0
        self.in_budget_suggesitions=[]
        self.option= 0
        User.user_count +=1
    def user_info(self):
        print("Amount left",self.budget_left)
    @classmethod
    def update_user_info_users(self,user):
        self.users.append(user)
        
    @classmethod             
    def user_purchase_and_budget_update(self,grocery_taken,user):
        print(grocery_taken)
        for user_data in self.users:
            if user_data.user_id == user.user_id:
                if user_data.budget_left >= grocery_taken.get("price"):
                    user_data.budget_left -= grocery_taken.get("price")
                    user_data.grocery_purchased_by_user.append(grocery_taken)
                    user=user_data
                    print("Amount left ",user_data.budget_left)
                    print()
                    return 1
        return 0  

    def purchased_products(self):
        for item in self.grocery_purchased_by_user:
            print(item)          
