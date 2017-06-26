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

user_categorie = int(raw_input("You Are : \n1. Owner \n2. Customer \nSelect Option : "))

# function to take food item name and validate it
def take_food_item(owner_restaurant_name):
    update_food_item_name = raw_input("Enter the Food Item name : ")
    if (update_food_item_name in (restaurant_dict[owner_restaurant_name]['Food List'].keys())):
        return update_food_item_name
    else:
        return "False"

# Owner Pannel
if(user_categorie == 1):
    owner_restaurant_name = raw_input("Please provide your restaurant name : ")
    owner_choice = raw_input("Do you want to update Yes/No : ")
    if(owner_choice == "Yes"):
        update_choice = int(raw_input("Update : \n1. Add a New Food Item \n2. Delete a Food Item \n3. Change Price of Food Item \nSelect : "))
        if(update_choice == 1):
            update_food_item_name = raw_input("Enter the Food Item name : ")
            if (update_food_item_name in (restaurant_dict[owner_restaurant_name]['Food List'].keys())):
                print update_food_item_name + " Already Present in the Food Item List \nBye"
                quit()
            else:
                update_food_item_price = int(raw_input("Please Enter the price for " + update_food_item_name + " : "))
                restaurant_dict[owner_restaurant_name]['Food List'][update_food_item_name] = update_food_item_price
                print "Food Item " + update_food_item_name + " added to menue \nThank You"
                #print restaurant_dict[owner_restaurant_name]['Food List']
        elif(update_choice == 2):
            update_food_item_name = take_food_item(owner_restaurant_name)
            if(update_food_item_name != "False"):
                del restaurant_dict[owner_restaurant_name]['Food List'][update_food_item_name]
                print "Food Item " + update_food_item_name + " deleted \nThank You"
                #print restaurant_dict[owner_restaurant_name]['Food List']
            else:
                print "Enter Valid Food Item name to Delete \nBye"
                quit()
        elif(update_choice == 3):
            update_food_item_name = take_food_item(owner_restaurant_name)
            if (update_food_item_name != "False"):
                update_food_item_price = int(raw_input("Please Enter the new price for " + update_food_item_name + " : "))
                restaurant_dict[owner_restaurant_name]['Food List'][update_food_item_name] = update_food_item_price
                print "Price Updated of " + update_food_item_name + " to " + str(update_food_item_price) + "\nThank You"
                #print restaurant_dict[owner_restaurant_name]['Food List']
            else:
                print "Food Item not present in the menu \nBye"
                quit()
    elif(owner_choice == "No"):
        print "Bye"
        quit()
# Customer Pannel
elif(user_categorie == 2):
    print "Restaurant  List :"
    index=0
    for restaurant_name in restaurant_dict.keys():
        print str(index+1) + "> " + restaurant_name
        index += 1
    customer_choice = int(raw_input("Do You Want to : \n1. Order Food \n2. Rate the restaurant \nSelect the option: "))
    if(customer_choice == 1):
        customer_choice_restaurant = raw_input("Enter the restaurant name for menue : ")
        print "Menu : "
        index = 0
        for food_item_name in (restaurant_dict[customer_choice_restaurant]['Food List'].keys()):
            print str(index+1) + "> " + food_item_name + " : rs " + str(restaurant_dict[customer_choice_restaurant]['Food List'][food_item_name])
            index += 1
        customer_total = 0
        print "Enter the name of the Food Items you want to order (Press ENTER to EXIT) : "
        while(True):
            customer_order_item_name = raw_input()
            if(len(customer_order_item_name) == 0):
                break
            else:
                if(customer_order_item_name in (restaurant_dict[customer_choice_restaurant]['Food List'].keys())):
                    customer_total += restaurant_dict[customer_choice_restaurant]['Food List'][customer_order_item_name]
                    print customer_order_item_name + " Food Item Added to order (Press ENTER to EXIT)"
                else:
                    print "Sorry uavailable order something else or Press ENTER to EXIT"
        if(customer_total != 0 ):
            customer_bill = customer_total + (customer_total * 0.1) + (customer_total * 0.06) + (customer_total * 0.15)
            print "Order Created Successfully"
        else:
            print "Empty Order \nBye"
            quit()
        customer_order_method = int(raw_input("Please choose the method for order :\n1> Walk-in \n2> Delivery \nSelect option : "))
        if(customer_order_method == 1):
            print "Choosen method is delivery"
            print "Your total is : " + str(customer_bill)
            quit()
        elif(customer_order_method == 2):
            print "Choosen method is Walk-in"
            print "Your total is : " + str(customer_bill)
            quit()
    elif(customer_choice == 2):
        customer_choice_restaurant = raw_input("Enter the restaurant name to rate : ")
        customer_rating = float(raw_input("Enter the rating : "))
        restaurant_dict[customer_choice_restaurant]['Restaurant Rating'] = customer_rating
        print "Restaurant Rating Updated \nThank You"
        #print restaurant_dict[customer_choice_restaurant]
        quit()
else:
    print "Bye"
    quit()

