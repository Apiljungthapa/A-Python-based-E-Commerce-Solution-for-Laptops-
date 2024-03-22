user_requirement=[]#creating list of user selled item
user_need=[]#creating list of user buyed item
product_dict={}#creating dictionary to store details
def display_products():#defining function
    
    '''This program reads the textfile and display the quantity,products in tables format
    returns empty and does not contain any parameter or arguments'''
    print("\n\n\n\n")    
    id = 1#assign id as 1
    '''opening textfile and iterating over each line of the file using enumerate function'''
    with open("product_info.txt", "r") as file:   
        for id,line in enumerate(file,start=1):
            line1=line.strip()
            product_dict[id]=line1.split(",")
           

    print("\n\n\n\n")
    
 
      
    print("\t\t\t\t\t\t\tWelcome to our shop  "+"\n")
    print("----------------------------------------------------------------------------------------------------------------------------------|")
    print("\tbrandname |\t\tlaptopname |\t\t  price |\t\tquantity |\t  processor |\t  graphics")#title of details
    print( "----------------------------------------------------------------------------------------------------------------------------------|")
    '''using for loop to iterate with keys and values'''    
    for key, value in product_dict.items():
            
        print("\n")
        print(str(key) +"    ", value[0]," "*(9-len(value[0]))+"\t\t ",value[1]," "*(9-len(value[1])),"\t\t",value[2],""*(4-len(value[2])),"\t\t",value[3]," "*(7-len(value[3])),"\t",
                value[4]," "*(8-len(value[4])),"\t",value[5]," "*(7-len(value[5])))
        print("----------------------------------------------------------------------------------------------------------------------------------|")
        
    

