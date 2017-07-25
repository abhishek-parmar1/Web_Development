print "ZOMATO"
# restaurant dictionary
restaurant_dict= {
    'Pizza Hut' : {
        'Qwner' : 'Dan and Frank Carney',
        'Restaurant Rating' : 4.1,
         'Food List' : {
             'Veggie Supreme' : 490,
             'Chicken Supreme' : 570,
             'Tandoori Paneer' : 460,
             'Chicken Tikka' : 490,
             'Double Cheese' : 370,
             'Chicken N Spicy' : 460,
             'Margherita' : 250,
             'Paneer Overloaded' : 269,
             'Spicy Chicken Overloaded' : 299
         }
    },
    "Domino's" : {
        'Qwner' : 'Tom Monaghan',
        'Restaurant Rating' : 4.3,
        'Food List' : {
            'Chicken Fajita' : 390,
            'Margherita' : 420,
            'Cheese & Tomato' : 290,
            'Cheese & Bbq Chicken' : 430,
            'Chicken Fiest' : 380,
            'Spicy Chicken' : 475,
            'Keema do Pyaaza' : 510,
            'Zesty Chicken ' : 510,
            'Non Veg Extravaganza' : 575,
            'Meatzaa' : 575
        }
    },
    "McDonald's" : {
        'Qwner' : 'Ray Kroc',
        'Restaurant Rating' : 4.0,
        'Food List' : {
            'McAloo Tikki' : 109,
            'Chicken McGrill' : 119,
            'McAloo Wrap with Chipotle Sauce' : 132,
            'Grill Chicken Wrap with Chipotle Sauce ' : 150,
            'Filet-O-Fish' : 189,
            'Chicken Maharaja Mac' : 204,
            'Chicken McNuggets' : 265,
            'Big Spicy Chicken Wrap' : 244,
            'Grilled Chicken Royale' : 231,
            'Hot Cakes (with Syrup & Butter) ' : 114
        }
    },
    'KFC' : {
        'Qwner' : ' Colonel Harland Sanders',
        'Restaurant Rating' : 4.7,
        'Food List' : {
            'Smoky Grilled or Hot and Crispy' : 295,
            'Duo Bucket Meal' : 399,
            'Zinger Delux' : 230,
            'Cheezy Crunch' : 154,
            "Chicken Rockin'" : 160,
            'Veg Zinger' : 174,
            'Chicken Zinger' : 194,
            'Mingles Bucket' : 199,
            'Longer' : 120,
            'Rice Bowlz' : 159
        }
    }
}
def input(string,x):
    if(x==0):
        return int(raw_input(string))
    if(x==1):
        return raw_input(string)
def print_list(list):
    for name in list:
        print name
def take_food_item(owner_restaurant_name):
    update_food_item_name = input("Enter the Food Item name : ",1)
    if (update_food_item_name in (restaurant_dict[owner_restaurant_name]['Food List'].keys())):
        return update_food_item_name
    else:
        return "False"
while(True):
    user_categorie = input("You Are : \n1. Owner \n2. Customer \n3. To Exit \nSelect Option : ",0)
    if(user_categorie == 1):
        print "Restaurant  List :"
        print_list(restaurant_dict.keys())
        owner_restaurant_name = input("Please provide your restaurant name : ",1)
        owner_choice = input("Do you want to update Yes/No : ",1)
        if(owner_choice == "Yes"):
            update_choice = input("Update : \n1. Add a New Food Item \n2. Delete a Food Item \n3. Change Price of Food Item \nSelect : ",0)
            if(update_choice == 1):
                update_food_item_name = input("Enter the Food Item name : ",1)
                if (update_food_item_name in (restaurant_dict[owner_restaurant_name]['Food List'].keys())):
                    print update_food_item_name + " Already Present in the Food Item List \nBye"
                else:
                    restaurant_dict[owner_restaurant_name]['Food List'][update_food_item_name] = input("Please Enter the price for " + update_food_item_name + " : ",0)
                    print "Food Item " + update_food_item_name + " added to menue \nThank You"
                    print restaurant_dict[owner_restaurant_name]['Food List']
            elif(update_choice == 2):
                update_food_item_name = take_food_item(owner_restaurant_name)
                if(update_food_item_name != "False"):
                    del restaurant_dict[owner_restaurant_name]['Food List'][update_food_item_name]
                    print "Food Item " + update_food_item_name + " deleted \nThank You"
                    print restaurant_dict[owner_restaurant_name]['Food List']
                else:
                    print "Enter Valid Food Item name to Delete \nBye"
            elif(update_choice == 3):
                update_food_item_name = take_food_item(owner_restaurant_name)
                if (update_food_item_name != "False"):
                    restaurant_dict[owner_restaurant_name]['Food List'][update_food_item_name] = input("Please Enter the new price for " + update_food_item_name + " : ",0)
                    print "Price Updated of " + update_food_item_name + " to " + str(restaurant_dict[owner_restaurant_name]['Food List'][update_food_item_name]) + "\nThank You"
                    print restaurant_dict[owner_restaurant_name]['Food List']
                else:
                    print "Food Item not present in the menu \nBye"
        elif(owner_choice == "No"):
            print "Bye"
    elif(user_categorie == 2):
        print "Restaurant  List :"
        print_list(restaurant_dict.keys())
        customer_choice = input("Do You Want to : \n1. Order Food \n2. Rate the restaurant \nSelect the option: ",0)
        if(customer_choice == 1):
            customer_choice_restaurant = input("Enter the restaurant name for menue : ",1)
            print "Menu : "
            for food_item_name in (restaurant_dict[customer_choice_restaurant]['Food List'].keys()):
                print food_item_name + " : rs " + str(restaurant_dict[customer_choice_restaurant]['Food List'][food_item_name])
            customer_total = 0
            print "Enter the name of the Food Items you want to order (Press ENTER to EXIT) : "
            while(True):
                customer_order_item_name = raw_input()
                if(len(customer_order_item_name) == 0):
                    break
                else:
                    if(customer_order_item_name in (restaurant_dict[customer_choice_restaurant]['Food List'].keys())):
                        customer_total += restaurant_dict[customer_choice_restaurant]['Food List'][customer_order_item_name]
                        print customer_order_item_name + " Food Item Added to order  \nEnter the name of the Food Items you want to order (Press ENTER to EXIT)"
                    else:
                        print "Sorry uavailable order something else or Press ENTER to EXIT"
            if(customer_total != 0 ):
                customer_bill = customer_total + (customer_total * 0.1) + (customer_total * 0.06) + (customer_total * 0.15)
                print "Order Created Successfully"
            else:
                print "Empty Order \nBye"
                exit()
            customer_order_method = input("Please choose the method for order :\n1> Walk-in \n2> Delivery \nSelect option : ",0)
            if(customer_order_method == 1):
                print "Choosen method is delivery \nYour total is : " + str(customer_bill)
                break
            elif(customer_order_method == 2):
                print "Choosen method is Walk-in \nYour total is : " + str(customer_bill)
                break
        elif(customer_choice == 2):
            customer_choice_restaurant = input("Enter the restaurant name to rate : ",1)
            customer_rating = float(raw_input("Enter the rating : "))
            restaurant_dict[customer_choice_restaurant]['Restaurant Rating'] = customer_rating
            print "Restaurant Rating Updated \nThank You"
            print restaurant_dict[customer_choice_restaurant]
    else:
        print "Bye"
        break
