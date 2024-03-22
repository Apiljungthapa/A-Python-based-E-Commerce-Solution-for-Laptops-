from read import product_dict,user_need,user_requirement #importing dictionary named product dict, list named user need and user requirements from read.py module
from operations import buy_products#importing buy products funtion from operations.py module
from write import bill_generate#importing bill_generate funtion from operations.py module
import read#import read.py module
import operations#import operations.py module
import write#import write.py module
import datetime#import datetime library


now = datetime.datetime.now()
print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
print("\t\t\t\t\t\t\t\t\tApil Laptop and Pc shop || 9867004146\n")#date and titile of the shop
print("\t\t\t\t\t\t\t\t----------------------------------------------------")



while True:
    user_menus=('1','2','3')#menus for users
    print("\n")
    print("------------------------------|")
    print("Welcome to our laptop shop ")#welcome screen
    print("------------------------------|")
    print("1. buy_products")#buy products for 1
    print("2. sell_products")#sell products for 2
    print("3. exit")#exit for 3
    print("\n")
    print("------------------------------|"+"\n")
    user_value = input("please choose an option: ")#ask user for their choices
    
    if user_value in user_menus:
        
        if user_value == '1':
            
            read.display_products()#call display products function from read.py module
            print(read.display_products.__doc__)#print docstrings of read.py module

            
            name ,phone = operations.buy_products(product_dict,now,user_need)#calling buy products function and get name and phone variable.
            print(operations.buy_products.__doc__)#print docstrings of operations.py module
                
            
                
                
                
                
        elif user_value == '2':
            read.display_products()#call display products function from read.py module
            
            print(read.display_products.__doc__)#print docstrings of read.py module
                
            operations.sell_products(product_dict,now,user_requirement)#called sell products function from operations.py module
            print(operations.sell_products.__doc__)#print docstrings of operations.py module
                
           
                
                
                
        else:
            exit()   # exit the program                                      
    else:
        print("\n")
        print("Option Not available ")#options entered beyond  option in menus              
                   
    

    
            
        
