import byeBish
from byeBish import Avantages
def ordering():
    user={}
    order=[]
    counts=tuple(input("which ones u wanna order").split())
    order.append(counts)
    name=input("enter your name")
    address=input("enter your address")
    order.append(address)
    user[name]=order
    print(user)

while(True):
    info=int(input("enter which product you want to know about(only num)"))
    if(info in byeBish.products):
        if(info==1):
            Avantages.honey()
        elif(info==2):
            Avantages.coffee()
        elif(info==3):
            Avantages.baking()
        else:
            Avantages.greenTea()
    else:
        print("The product u want is not available")
    option=input("enter q to quit/o to order/p for prices")
    if(option=='q'):
        break
    elif(option=='p'):
        byeBish.prices()
    else:
        ordering()
        option = input("enter q to quit")
        if (option == 'q'):
            break



