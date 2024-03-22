
import datetime#date import built in library
from read import product_dict,user_need,user_requirement #importing dictionary,user need list and user_requirement from read module
#defining function for bill generation with parameter
def bill_generate(name,phone,now,user_need):
    
    '''This is a function which generates bill of buying laptops from manufacturers
        Takes name ,phone number of manufacturers and list as arguments
        returns empty'''
    
    status="the_lucky_buyer"
    year=str(datetime.datetime.now().year)
    month=str(datetime.datetime.now().month)
    day=str(datetime.datetime.now().day)#for unique textfile generation'''
    hour=str(datetime.datetime.now().hour)
    minute=str(datetime.datetime.now().minute)
    seconds=str(datetime.datetime.now().second)
    interesting_time=year+month+day+hour+minute+seconds
    total_price=0

    print("----------------------------------------------------------------------\n")
    print("\t\tBill of our shop | Apil electronics\n")
    print("\t\t\tDate: " + now.strftime("%Y-%m-%d %H:%M:%S") + "\n")
    print("\t\t--------------------------------------\n\n")
    print("\t\tname of  buyer is: ",end="")
    print("\t\t  "+str(name)+"\n")
    print("\t\tphone number of buyer is: ",end="")#displaying console bill'''
    print("\t  " +str(int(phone))+"\n")
    total_pric=0
    for product in user_need:
        
        laptop_name=product[0]#laptop name variable store laptops of user buyed
        laptop_quant=product[1]#quantity of laptops user has buyed
        total_price=product[2]#price of laptop user buyed
        total_fullamt=product[3]#user buyed prices total
        net_amount=int(product[1])*int(product[2])
        vat_amount=net_amount*0.13#calculating vat amount
        gross_amount=vat_amount+net_amount#gross amount calculating
        total_pric+=int(total_fullamt)#total price  added with prices
        
                
                
        print("\t\tThe name of laptop is\t\t",str(laptop_name)+"\n")#laptop name is displayed which user has buyed
        print("\t\tThe number of quantity is\t ",str(laptop_quant)+"\n")#quantity user has purchased
    print("\t\tnet_amount is: ",end="")
    print("\t\t\t ",net_amount)#displaying net amount
    print("\n")
    print("\t\tvat_amount is: ",end="")
    print("\t\t\t",vat_amount)
    print("\n")
    print("\t\tgross_amount is: \t\t ",gross_amount)
                
    print("\n")
    print("-----------------------------------------------------------------------------")
    print("\t\tThe total price is \t\t RS",total_pric)#toatl price is displayed
    print("-----------------------------------------------------------------------------")
    add = name + "_"+status+"_"+interesting_time+".txt"
    '''opening textfile and displaying bill in a textfile'''       
    with open(add,"w")as bill:
        
                
        bill.write("----------------------------------------------------------------------\n")
        bill.write("\t\tBill of our shop | Apil electronics\n")
        bill.write("\t\t\tDate: " + now.strftime("%Y-%m-%d %H:%M:%S") + "\n")
        bill.write("\t\t--------------------------------------\n\n")
        bill.write("\t\tname of  buyer is: " )
        bill.write("\t\t "+str(name)+"\n")
        bill.write("\t\tphone number of buyer is: ")#displaying name
        bill.write("\t " +str(int(phone))+"\n")
        for i in user_need:
            bill.write("\t\tThe name of laptop is\t\t"+str(i[0])+"\n")#itearting laptop name which user has buyed and displaying
            print("\n")
            bill.write("\t\tThe number of quantity is\t "+str(i[1])+"\n")#iterating all quantity 
        bill.write("\t\tnet_amount is:\t\t\t "+str(net_amount))#displaying net amount
        bill.write("\n")
        bill.write("\t\tvat_amount is:\t\t\t "+str(vat_amount))#displaying vat amount
        bill.write("\n")
        bill.write("\t\tgross_amount is: \t\t\t"+str(gross_amount))
                    
        bill.write("\n")
        bill.write("-----------------------------------------------------------------------------")
        bill.write("\n")
        bill.write("\t\tThe total price is \t\tRS "+str(total_pric))#displaying total price
        bill.write("\n")
        bill.write("-----------------------------------------------------------------------------")
        
        '''opening textfile and writting it to bill of updating stocks'''
        with open("update.txt","w")as billupdate:
            
            billupdate.write("\n")        
            billupdate.write("\t\t\t\t\t \t   Your || Details of shop")
            billupdate.write("\n")
            billupdate.write("----------------------------------------------------------------------------------------------------------------------------------|")
            billupdate.write("\n")   
            billupdate.write("\tbrandname       laptopname   \t        price   \tquantity      \t    processor   \t    graphics")
            billupdate.write("\n")   
            billupdate.write( "----------------------------------------------------------------------------------------------------------------------------------|")
                        
            for key, value in product_dict.items():
                billupdate.write("\n")#displaying all details in console'''
                billupdate.write("       \t".join([str(key) +"    "+ str(value[0])," "*(9-len(value[0]))+" "+str(value[1])+" "*(9-len(value[1]))+" \t\t  "+str(value[2])+"\t   "*(4-len(str(value[2])))+"   \t"+str(value[3])+" "*(7-len(str(value[3])))+"\t\t"+
                        str(value[4])+"\t "*(3-len(str(value[4])))+"\t\t  "+str(value[5])+"  \t"*(2-len(str(value[5])))+"\t"]))#taking length and displaying details
                billupdate.write("----------------------------------------------------------------------------------------------------------------------------------|")
                billupdate.write("\n")        
                             
                
            
                
           
        print("\n")        
        print("\t\t\t\t\t    Your || Details of shop")
        print("\n")
        print("----------------------------------------------------------------------------------------------------------------------------------|")
        print("\tbrandname |\t\tlaptopname |\t\t  price |\t\tquantity |\t  processor |\t  graphics")
        print( "----------------------------------------------------------------------------------------------------------------------------------|")
        #iterating over dictionary and displaying etails by talking length and using tabspaces            
        for key, value in product_dict.items():
            print("\n")
            print(str(key) +"    ", value[0]," "*(9-len(value[0]))+"\t\t ",value[1]," "*(9-len(value[1])),"\t\t",value[2],""*(4-len(str(value[2]))),"\t\t",value[3]," "*(7-len(str(value[3]))),"\t",
                    value[4]," "*(8-len(str(value[4]))),"\t",value[5]," "*(7-len(str(value[5]))))
            print("----------------------------------------------------------------------------------------------------------------------------------|")
            print("\n")        
                         
'''defining function and passsing desired parameters in it'''   
def shippbill_generate(name,phone,now,user_requirement):
    
    
        '''This function generates bill of selling including shipping cost to an item,it also takes values as a parameter such as name ,phone number
            datetime now with list as arguments or parameter
                also returns empty'''
        
        status="the_lucky_customer"
        year=str(datetime.datetime.now().year)
        month=str(datetime.datetime.now().month)
        day=str(datetime.datetime.now().day)#conacatinating all deatils foir unique textfile'''
        hour=str(datetime.datetime.now().hour)
        minute=str(datetime.datetime.now().minute)
        seconds=str(datetime.datetime.now().second)
        interesting_time=year+month+day+hour+minute+seconds
                
        add = name + "_"+status+"_"+interesting_time+".txt"#concatinating  all details 
                    
        print("\n")
       
                   
        shipped = input("Dear user will you be allowing us to add shipping cost to your pc(y/N)?  :  ")#asks for the users for shipping cost or not
        print("\n\n\n")
        if shipped == "y":
            
                                
            DElivery_cost=1000#shipping cost
            total =0
                           
            #amount_total=int(total_cost)
            print("\t\tBill with shipping cost included ")
            print("----------------------------------------------------------------------\n")
            print("\t\tBill of our shop | Apil electronics\n")
            print("\t\t\tDate: " + now.strftime("%Y-%m-%d %H:%M:%S") + "\n")#details with titile of the shop, date.
            print("\t\t--------------------------------------\n\n")
            print("\t\tname of  our customer is: ",end="")#name of customer
            print("\t\t  "+str(name)+"\n")
            print("\t\tphone number of our customer is: ",end="")
            print("\t  " +str(int(phone))+"\n")#phone number of customer
            
                            
            for pc in user_requirement:
                    
                laptops_is=str(pc[0])#displaying laptop name user selled
                quantity_is=int(pc[1])#customer needed quantity
                indiv_qu=int(pc[2])#price of laptop
                cost_is=int(pc[3])#prices obtained after multip,kying quantity
                total+=int(pc[3])#total price oa all selled laptops
                                
                total_cost_is=int(total)+int(DElivery_cost)
                                
                print("\t\tThe name of laptop is\t\t\t",str(laptops_is)+"\n")#name of laptop
                print("\t\tThe number of quantity is\t\t ",str(quantity_is)+"\n")#quantity of laptop
            print("\t\tShipping cost is: ",end="")
            print("\t\t\t ",DElivery_cost)#shipping cost added
            print("\n")
            print("-----------------------------------------------------------------------------")    
            print("\t\tThe total price is \t\t\tRS ",total_cost_is)#total price with shipping cost added
            print("-----------------------------------------------------------------------------")
           
            #opening textfile in write mode for bill
            with open(add,"w")as customerbill:
                        
                                
                               
                ("Bill with shipping cost included ")
                customerbill.write("----------------------------------------------------------------------\n")
                customerbill.write("\t\tBill of our shop | Apil electronics\n")
                customerbill.write("\t\t\tDate: " + now.strftime("%Y-%m-%d %H:%M:%S") + "\n")
                customerbill.write("\t\t--------------------------------------\n\n")
                customerbill.write("\t\tname of  our customer is: ")
                customerbill.write("\t       "+str(name)+"\n")#writting name
               
                customerbill.write("\t\tphone number of our customer is: ")
                customerbill.write("\t " +str(int(phone))+"\n")#writting phone
              
                for j in user_requirement:
                    
                    customerbill.write("\t\tThe name of laptop is\t\t      "+str(j[0])+"\n")# writting laptops all selled 
                    customerbill.write("\t\tThe number of quantity is\t\t "+str(j[1])+"\n")#writting quantity of all selled laptops
                    
                   
                customerbill.write("\t\tThe shipping cost is: ")    
                customerbill.write("\t\t\t "+str(DElivery_cost))#shipping cost adding
                customerbill.write("\n\n")
                customerbill.write("-----------------------------------------------------------------------------")
                customerbill.write("\n")
                customerbill.write("\t\tThe total price is \t\t\tRS "+str(total_cost_is))#total cost with shipping included
                customerbill.write("\n")
                customerbill.write("-----------------------------------------------------------------------------")


                with open("update.txt","w")as billupdatesell:
                    
            
                    billupdatesell.write("\n")        
                    billupdatesell.write("\t\t\t\t\t \t   Your || Details of shop")
                    billupdatesell.write("\n")#details with titile of the shop, date.
                    billupdatesell.write("----------------------------------------------------------------------------------------------------------------------------------|")
                    billupdatesell.write("\n")   
                    billupdatesell.write("\tbrandname       laptopname   \t        price   \tquantity      \t    processor   \t    graphics")#details top
                    billupdatesell.write("\n")   
                    billupdatesell.write( "----------------------------------------------------------------------------------------------------------------------------------|")
                                
                    for key, value in product_dict.items():
                        billupdatesell.write("\n")#writting stock to the file
                        billupdatesell.write("       \t".join([str(key) +"    "+ str(value[0])," "*(9-len(value[0]))+" "+str(value[1])+" "*(9-len(value[1]))+" \t\t  "+str(value[2])+"\t   "*(4-len(str(value[2])))+"   \t"+str(value[3])+" "*(7-len(str(value[3])))+"\t\t"+
                                str(value[4])+"\t "*(3-len(str(value[4])))+"\t\t  "+str(value[5])+"  \t"*(2-len(str(value[5])))+"\t"]))#displaying updated stock in file
                        billupdatesell.write("----------------------------------------------------------------------------------------------------------------------------------|")
                        billupdatesell.write("\n")        
                                     







                
                print("\n\n\n")        
                print("\t\t\t\t\t    Your || Details of shop")#titile of the shop
                print("\n")
                print("----------------------------------------------------------------------------------------------------------------------------------|")
                print("\tbrandname |\t\tlaptopname |\t\t  price |\t\tquantity |\t  processor |\t  graphics")
                print( "----------------------------------------------------------------------------------------------------------------------------------|")
                                            
                for key, value in product_dict.items():
                    print("\n")
                    print(str(key) +"    ", value[0]," "*(9-len(value[0]))+"\t\t ",value[1]," "*(9-len(value[1])),"\t\t",value[2],""*(4-len(str(value[2]))),"\t\t",value[3]," "*(7-len(str(value[3]))),"\t",
                            value[4]," "*(8-len(str(value[4]))),"\t",value[5]," "*(7-len(str(value[5]))))#displaying details in console with updated stock
                    print("----------------------------------------------------------------------------------------------------------------------------------|")
                    print("\n")

                    
                        
                                    
                                
                                
                                                    
                                
                       
                                
                                                     
                                                   
            
        else:
                
                                            
            totals=0#set total to zero
            print("----------------------------------------------------------------------\n")
            print("\t\tBill without shipping cost ")
            print("----------------------------------------------------------------------\n")
            print("\t\tBill of our shop | Apil electronics\n")
            print("\t\t\tDate: " + now.strftime("%Y-%m-%d %H:%M:%S") + "\n")
            print("\t\t--------------------------------------\n\n")#titile with date for non shipping item
            print("\t\tname of  buyer is: ",end="")
            print("\t\t\t  "+str(name)+"\n")#name of the customer
            print("\t\tphone number of buyer is: ",end="")
            print("\t\t  " +str(int(phone))+"\n")#phone of customer
                            
            for pc in user_requirement:
                laptops_is=str(pc[0])#displaying selled laptop name
                quantity_is=int(pc[1])#selled quantity
                indiv_qu=int(pc[2])#individual price
                cost_is=int(pc[3])# quantity multiply to price and calcuated it
                totals+=int(pc[3])#total full price
                                
                total_cost_is=int(totals)
                                
                print("\t\tThe name of laptop is\t\t\t",str(laptops_is)+"\n")#laptop name displaying
                print("\t\tThe number of quantity is\t\t ",str(quantity_is)+"\n")#displaying quantity
                
            print("-----------------------------------------------------------------------------")    
            print("\t\tThe total price is \t\t\t RS ",total_cost_is)#displaying total cost 
            print("-----------------------------------------------------------------------------")  

                            

            print("\n")        
            print("\t\t\t\t\t    Your || Details of shop")#titile of the shop
            print("\n")
            print("----------------------------------------------------------------------------------------------------------------------------------|")
            print("\tbrandname |\t\tlaptopname |\t\t  price |\t\tquantity |\t  processor |\t  graphics")
            print( "----------------------------------------------------------------------------------------------------------------------------------|")
                                        
            for key, value in product_dict.items():
                print("\n")
                print(str(key) +"    ", value[0]," "*(9-len(value[0]))+"\t\t ",value[1]," "*(9-len(value[1])),"\t\t",value[2],""*(4-len(str(value[2]))),"\t\t",value[3]," "*(7-len(str(value[3]))),"\t",
                        value[4]," "*(8-len(str(value[4]))),"\t",value[5]," "*(7-len(str(value[5]))))#displaying details in console with updated stock
                print("----------------------------------------------------------------------------------------------------------------------------------|")
                print("\n")                 
                            
            #creating textfile             
            with open(add,"w")as customerbill:
                               
                                
                ("Bill without shipping cost included ")
                customerbill.write("----------------------------------------------------------------------\n")
                customerbill.write("\t\tBill of our shop | Apil electronics\n")
                customerbill.write("\t\t\tDate: " + now.strftime("%Y-%m-%d %H:%M:%S") + "\n")#date with title of the shop
                customerbill.write("\t\t--------------------------------------\n\n")
                customerbill.write("\t\tname of  our customer is: ")
                customerbill.write("\t      "+str(name))#name of customer
                customerbill.write("\n")
                customerbill.write("\t\tphone number of our customer is: ")
                customerbill.write("   "+str(int(phone))+"\n")#phone number of customer
             


                                
                               
                for j in user_requirement:    
                    customerbill.write("\t\tThe name of laptop is\t\t     "+str(j[0])+"\n")#displaying laptop name selled to customer  
                    customerbill.write("\t\tThe number of quantity is\t\t"+str(j[1])+"\n")#displaying quantity selled to customer
                    
                customerbill.write("\n")
                customerbill.write("\n")
                customerbill.write("-----------------------------------------------------------------------------")
                customerbill.write("\n")
                customerbill.write("\t\tThe total price is\t\t\tRS "+str(total_cost_is))#displaying total price 
                customerbill.write("\n")
                customerbill.write("-----------------------------------------------------------------------------")
                #opening textfile for writting stock updated after selled in textfile
                with open("update.txt","w")as billupdatesellother:
                    
                    
                    billupdatesellother.write("\n") #new line sepearator       
                    billupdatesellother.write("\t\t\t\t\t \t   Your || Details of shop")#title
                    billupdatesellother.write("\n")
                    billupdatesellother.write("----------------------------------------------------------------------------------------------------------------------------------|")
                    billupdatesellother.write("\n")   
                    billupdatesellother.write("\tbrandname       laptopname   \t        price   \tquantity      \t    processor   \t    graphics")
                    billupdatesellother.write("\n")   
                    billupdatesellother.write( "----------------------------------------------------------------------------------------------------------------------------------|")
                                
                    for key, value in product_dict.items():
                        billupdatesellother.write("\n")
                        billupdatesellother.write("       \t".join([str(key) +"    "+ str(value[0])," "*(9-len(value[0]))+" "+str(value[1])+" "*(9-len(value[1]))+" \t\t  "+str(value[2])+"\t   "*(4-len(str(value[2])))+"   \t"+str(value[3])+" "*(7-len(str(value[3])))+"\t\t"+
                                str(value[4])+"\t "*(3-len(str(value[4])))+"\t\t  "+str(value[5])+"  \t"*(2-len(str(value[5])))+"\t"]))#using .join method and proper tabspaces details is writen in textfile
                        billupdatesellother.write("----------------------------------------------------------------------------------------------------------------------------------|")
                        billupdatesellother.write("\n")#new line seperator
                 
                                 
                                 

                   
                
           
