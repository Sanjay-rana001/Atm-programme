Enter=input("press enter to continue: ")
print("welcome to ATM")

AccNo=int(input("please input your account no : "))
if AccNo>999:
        PinNo=int(input("please input your pin no : "))
        print("Logged in successfully")
        print("""services to avail
        1. Balance Eniry
        2. Cash Withdrawl
        3. Check Statement
        4. Help & Support""")
        services=int(input("please enter service number: "))
        if services==1:
            print("your  account balance is 5000 rupees")
        elif services==2:
            withdrawl=int(input("please enter your withdrawl amount: "))  
            if withdrawl<5000:
                print("withdrawl sucessfully") 
            else:
                print("sorry your account blance is low")
        elif services==3:
            FromDate=input("From :")
            ToDate=input("To :")
            print("here is your statment")
        elif services==4:
            print("thank your for choosing help & support we will get back to you shortly")
        else:    
             print("sorry for the inconvenince cause ")

        
       
else:

        print("sorry for the inconvenince cause ")