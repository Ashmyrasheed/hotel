import mysql.connector

mydb = mysql.connector.connect(host = 'localhost' , user = 'root' , password = '' , database = 'hoteldb')
mycursor = mydb.cursor()
total=0
item=[]
l=[]
while(True):
    print("select an option")
    print("1 Tea-----10rs")
    print("2 coffee----15rs")
    print("3 burger----50rs")
    print("4 mandhi----180rs")
    print("5 sandwitch--60")
    print("6 generate bill")
    print("7 display the transaction details")
    print("8 display the transaction summary of particular day")
    print("10 exit")
    choice=int(input("enter the choice"))
    if(choice==1):
        print("Added tea")
        qty=int(input("enter the quantity"))
        total=10*qty
        l.append(total)
        item.append("tea x"+str(qty))
        #print("quantity",qty)
        #print("total",total)
        
    elif(choice==2):
        print("added coffee")
        qty=int(input("enter the quantity"))
        total=15*qty
        l.append(total)
        item.append("coffee x"+str(qty))
        #print("quantity",qty)
        #print("total",total)
        
    elif(choice==3):
        print("addedburger")
        qty=int(input("enter the quantity"))
        total=50*qty
        l.append(total)
        item.append("burger x"+str(qty))
        #print("quantity",qty)
        #print("total",total)
    elif(choice==4):
        print("added mandhi")
        qty=int(input("enter the quantity"))
        total=180*qty
        l.append(total)
        item.append("mandhi x"+str(qty))
        #print("quantity",qty)
        #print("total",total)
        
    elif(choice==5):
        print("added sandwitch")
        
        qty=int(input("enter the quantity"))
        total=60*qty
        l.append(total)
        item.append("sandwitch x"+str(qty))
        #print("quantity",qty)
        #print("total",total)
        
    elif(choice==6):
       
        print('You enter into billing section')

        name = input('Enter the name : ')

        phone = input('Enter the phone number : ')

        #dates = input('Enter the date in the form of yyyy-mm-d : ')

        l1 = []

        l1.extend(l)

        count = 0

        for i in l1:

           count = count + i

           l.remove(i)

        amount = count

        # #print(f'Total amount {count} ')

        sql = "INSERT INTO `bill`(`name`, `phno`, `amount`,`date`) VALUES (%s,%s,%s,now())"

        data = (name,phone,amount)

        mycursor.execute(sql,data)

        mydb.commit()

        print('Thank you Welcome to next time ')
        
    elif(choice==7):
        print("display the transaction details ")
        date = input('enter the date where you need the transaction details (yyyy-mm-dd):')
        sql = "SELECT * FROM `bill` WHERE `date` ='"+date+"'"
        mycursor.execute(sql)
        result=mycursor.fetchall()
        print(result)
        

    elif(choice==10):
        break
    
        
        
    