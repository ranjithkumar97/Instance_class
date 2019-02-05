username=input("enter the name")
password=""
hello=0
world=0
while(hello!=3):
    password=input("enter the password")
    if(password=="admin"):
        world=1
        break
    else:
        hello=hello+1
        if(hello==3):
            print("you have tried maximum number of time so pllz stop")
if(world==1):
    print("Thank you",username)