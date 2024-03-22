from write import bill_generate,shippbill_generate#importing functions such as bill generate and shippbill generate from write module
import datetime#datetime module importing
'''defining function that takes user input for buying which takes parameter'''
def buy_products(product_dict,now,user_need):
    '''This is a buy products function in which user give their details including which lapop he wants to buy
         Takes dictionary date now and another list as arguments
        return name and phone of the user'''
    while True:
       
                            
        name=input("Enter name of our customer: ")#ask for name until name is valid it checks name is empty or invalid
        if name.strip():
            if name.isalpha():
                break
            else:
                
                print("please enter valid name")
                name=input("Enter name of our customer: ")
                     
                    
        else:
            print("Name cant be empty")                                      
                        
    while True:
        
        try:
            
            phone = int(input("Enter phone number of our customer: "))#ask for the phone number and checks if it is negative it checks until it is valid 
            if phone < 0:
                print("please enter positive value")
            else:
                break
        except:
            print("Please enter valid information") 
    loop = True  #assigning loop variable to true
    while loop == True:
        
                
        while True:
            try:
                product_id =int(input("Enter id for laptop you want to buy: "))#ask user for product id
                break
            except:
                print("please enter valid information")
            
        #checks product id  validity until it is valid    
        while int(product_id) <= 0 or int(product_id) > len(product_dict):
            print("Please enter valid id which is available in our stock")
            product_id =int(input("Enter id for laptop you want to buy: "))

        while True:
            
            try:
                user_quantity = int(input("Enter number of quantity you want to buy: "))#ask user for quantity
                break
               
            except:
                print("please enter integer value")
                
        get_quantity = int(product_dict[product_id][3])
            
         #update file
        product_dict[product_id][3] = int(product_dict[product_id][3]) + int(user_quantity)#updating for the quantity in the stock after user has buyed.
        product_name=product_dict[product_id][1]#getting name of product user has selected
        quantity_selected=int(user_quantity)#quantity selected
        each_price=product_dict[product_id][2].replace("$","").strip()#removing dollar sign from price
        total_price=int(quantity_selected)*int(each_price)#total price
        
        #putting this value in list and appending to user requirement
        
        full_item=[product_name,quantity_selected,each_price,total_price]#creating list
        user_need.append(full_item)#appending that list in this list
        print("\n\n")
        print("\t\t"+"user buyed item list")
        print("-----------------------------------------------------------------------|")
        print(""+"Laptopname"+" "+" quantity"+" "+"Individal price"+""+"   total price")
        print("-----------------------------------------------------------------------")
        for item in user_need:
            print("",str(item[0])," \t"+str(item[1]),"\t",str(item[2]),"\t\t"+str(item[3]),"\t\t\t  ")#displaying all user purvhased list
            print("-----------------------------------------------------------------------|")
            print("\n")
        
             
        choice= input("Do you want to buy another laptop(yes/No)Press 'y' for yes and 'n' for No: ")#ask for the user if they wants to buy more if yes loop continue ele break
        print("\n")
        if choice.lower() == 'n':
            loop = False#exit from the loop
            bill_generate(name,phone,now,user_need)#calling bill generate function to generate bill
                    
            print("\n")
            
    return name,phone #return variable name and phone to use it in other function
    


'''defining function that takes user input for selling products which takes parameter'''

def sell_products(product_dict,now,user_requirement):
    
    '''This is a sell products function which give the details of our customer what he wants to sell
        Takes dictionary date now and another list as arguments
        return name and phone number of the customer'''
    
    print("\n\n")
    while True:
                            
        name=input("Enter name of our customer: ")#ask for name until name is valid it checks name is empty or invalid
        if name.strip():
            
            if name.isalpha(): 
                break
            
            else:
                print("please enter valid name")
                name=input("Enter name of our customer: ")
        
        else:
            print("Name cant be empty")
                
    while True:
        
        try:      
            phone = int(input("Enter phone number of our customer: "))#ask for the phone number and checks if it is negative it checks until it is valid 
            if phone < 0:
                print("please enter positive value")
            else:
                break
                
            
        except:
            print("Please enter valid information")
   
    main=True #assigning main variable to true
    while main == True:

        while True:
            
        
            try:
                #checks product id  validity until it is valid  
                product_id =int(input("Enter id for laptop : "))
                break
            except:
                print("please enter valid information")#displays messages if exception found
        while int(product_id) <= 0 or int(product_id) > len(product_dict):
            print("Please enter valid id which is available in our stock")#displays message
            product_id =int(input("Enter id for laptop : "))#asks or user input again
                
        
                    

        while True:
                
            try:
                user_quantity = int(input("Enter number of quantity : "))#ask user for quantity
                break
            except:
                print("please enter integer value")#displays message
            
                
        take_quantity = int(product_dict[product_id][3])#takes quantity from users
                
            
             
        while int(user_quantity) <= 0 or int(user_quantity) > take_quantity:
            print("Please enter valid quantity available in our stock")#displays message if not valid quantity entered
            user_quantity = input("Enter number of quantity : " )#asks for quantity again



        product_name=product_dict[product_id][1]#getting name of product user has selected
        quantity_selected=int(user_quantity)#quantity selected
        each_price=product_dict[product_id][2].replace("$","").strip()#replaces dollar with empty string in price
        total_price=int(quantity_selected)*int(each_price)#calculating total price
            
        full_item=[product_name,quantity_selected,each_price,total_price]#creating list
        user_requirement.append(full_item)#appending list into list
           
           
        #total_cost = int(user_quantity) * int(product_dict[product_id][2].replace("$","").strip())
        
       
        
        #update quantity
        print("\n\n")
        product_dict[product_id][3]=int(product_dict[product_id][3])-int(user_quantity)#updating for the quantity in the stock after user has selled.
        print("\n\n")
        print("\t\t"+"user sell item list")#show user sell title
        print("-----------------------------------------------------------------------|")
        print(""+"Laptopname"+" "+" quantity"+" "+"Individal price"+""+"   total price")
        print("-----------------------------------------------------------------------")
        for item in user_requirement:
            print("",str(item[0])," \t"+str(item[1]),"\t",str(item[2]),"\t\t"+str(item[3]),"\t\t\t  ")#displaying all user purvhased list
            print("-----------------------------------------------------------------------|")
            print("\n") 
        choice=input("Do you want to sell any other laptops?(y/n): ")#asks user for if they wants to sll other laptops if yes it will continue only
        if choice.lower() == "n":
            main=False#it will break the loop            
            shippbill_generate(name,phone,now,user_requirement)#calling shippbill generate function to generate bill
                    
          
        

    return name,phone#return variable name and phone to use it in other function
    
