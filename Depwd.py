import os
import sys
import datetime
from Loginfun      import login_acc

def depandwithdraw():
  print(" ")
  while(True): 
    i=str(input("                         Enter Your Acc Number     : "))
    j=str(input("                         Enter Your Password       : "))
    k=login_acc(i,j)
    if(k==True):
        os.system('cls')
        print(" ")
        print("                         Sucessfully Login !!!! " )
        print(" ")
        print("                  -----------Plz select an Option-----------")
        print("                  |  - > press(1) To Deposit Money         |")
        print("                  |  - > press(2) To WithDraw Money        |")
        print("                  |  - > press(3) To Back                  |")
        print("                  ------------------------------------------")
        choice = int(input("                         Enter Your  Option Number : " ))
        if (choice == 1):
          try:
            print(" ")
            put=int(input("                         Enter the Money to deposit :"))
            now = datetime.datetime.now()
            date=now.strftime("%d/%m/%Y")
            time=now.strftime("%I:%M:%S")
            mypath = os.path.join("Userdatabase",i)
            path= os.path.join("logs",i)
            f=open(mypath+".txt","r")
            if (os.stat(mypath+".txt").st_size == 0):
                numbers = 0;
            else:
                numbers = f.readline()
            k=int(numbers)
            a=(k+put)
            b=str(a)
            f.close()
            k=open(mypath+".txt","w")
            g=k.write(b)
            rohan=str(put)
            d=open(path+".txt","a")
            d.write("\n")
            d.write(rohan)
            d.write(" Rupees amount deposited ")
            d.write(date)
            d.write(" at ")
            d.write(time)
            d.close()
            print("Amount deposited in Your Account")
          except:
             print("                         ")
             print("               Warning⚠There is no FILES regarding this Account.\n                    Eihter the Files are deleted or moved  ")
        elif (choice == 2):
          try:
            pput=int(input("                         Enter the Money to With Draw :"))
            now = datetime.datetime.now()
            date=now.strftime("%d/%m/%Y")
            time=now.strftime("%I:%M:%S")
            mypath = os.path.join("Userdatabase",i)
            path= os.path.join("logs",i)
            f=open(mypath+".txt","r")
            if (os.stat(mypath+".txt").st_size == 0):
                numbers = 0;
            else:
                numbers = f.readline()
            k=int(numbers)
            a=(k-pput)
            b=str(a)
            f.close()
            k=open(mypath+".txt","w")
            g=k.write(b)
            rohan=str(pput)
            d=open(path+".txt","a")
            d.write("\n")
            d.write(rohan)
            d.write(" Rupees amount WithDraw on ")
            d.write(date)
            d.write(" at ")
            d.write(time)
            d.close()
            print("Amount is credit from Your Account")
          except:
             print("                         ")
             print("               Warning⚠There is no FILES regarding this Account.\n                    Eihter the Files are deleted or moved  ")
        elif (choice == 3):
             p=os.getcwd()
             exec(open(p+'\maincall.py').read())

    else:
         print("                         ")
         print("                  Error !!!!..Retry...In Correct Credential ⚠ ")
         print("                         ")
    

