###import###
import os
import sys
from Loginfun      import login_acc
from User_info_i   import create_acc
from Depwd         import depandwithdraw
from acclogin      import acc_login
#### Main Program ###
while(True):
     os.system('cls')
     print(" ")
     print(" ")
     print("                  -----------Plz select an Option-----------")
     print("                  |  - > press(1) To Create New Account    |")
     print("                  |  - > press(2) To Login in an Account   |")
     print("                  |  - > press(3) To Deposit or With Draw  |")
     print("                  |  - > press(4) To Exit                  |")
     print("                  ------------------------------------------")
     choice= int(input("                         Enter Your  Option Number : " ))
     if (choice == 1):
      os.system('cls')
      create_acc();
     elif (choice == 2):
      os.system('cls')
      while(True):
        print(" ")
        i=str(input("                         Enter Account Number : "))
        j=str(input("                         Enter Password       : "))
        k=(login_acc(i,j))
        if(k == True):
             acc_login(i);
        elif(k==False):
             print(" ")
             print("                         Wrong Password ⚠ ")
        elif(k==None):
             print("                         User Name is not present in database ⚠  ")
        
     elif(choice == 3):
      os.system('cls')
      depandwithdraw();

     elif(choice == 4):
      sys.exit(0)
     else:
      print("                  Invalid Option !!")

os.system("pause")

