import mysql.connector

mydb = mysql.connector.connect(host = 'localhost' , user = 'root' , password = '' , database = 'hoteldb')
mycursor = mydb.cursor()
total=0
item=[]
while(True):
    print("select an option")
    print("1 Tea-----10rs")
    print("2 coffee----15rs")
    print("3 burger----50rs")
    print("4 mandhi----180rs")
    print("5 sandwitch--60")
    print("6 generate bill")
    print("7 exit")
    choice=int(input("enter the choice"))
    if(choice==1):
        print("Added tea")
        qty=int(input("enter the quantity"))
        total+=10*qty
        item.append("tea x"+str(qty))
        #print("quantity",qty)
        #print("total",total)
        
    elif(choice==2):
        print("added coffee")
        qty=int(input("enter the quantity"))
        total+=15*qty
        item.append("coffee x"+str(qty))
        #print("quantity",qty)
        #print("total",total)
        
    elif(choice==3):
        print("addedburger")
        qty=int(input("enter the quantity"))
        total+=50*qty
        item.append("burger x"+str(qty))
        #print("quantity",qty)
        #print("total",total)
    elif(choice==4):
        print("added mandhi")
        qty=int(input("enter the quantity"))
        total+=180*qty
        item.append("mandhi x"+str(qty))
        #print("quantity",qty)
        #print("total",total)
        
    elif(choice==5):
        print("added sandwitch")
        
        qty=int(input("enter the quantity"))
        total+=60*qty
        item.append("sandwitch x"+str(qty))
        print("quantity",qty)
        print("total",total)
        
    elif(choice==6):
        print("generating bill")
        
    elif(choice==7):
        break
        
        
    