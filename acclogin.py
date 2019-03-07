import os
from Loginfun      import login_acc



def acc_login(a):
   i=a
   os.system('cls')
   print("                         ")
   print("                  -------------Plz Choose a Option-------------")
   print("                  |-> Press (1) To View Logs                  |")
   print("                  |-> Press (2) To Show amount in your Account|")
   print("                  |-> press (3) Back                          |")
   print("                  ---------------------------------------------")
   option = int(input("                         Choose your Option : "))
   while (option <=3):
     if (option==1 ):
      try:
        path=os.path.join("logs",i)
        with open(path+".txt", "r") as logs:
         content=logs.read()
         if not content:
              print(" ")
              print("                Since,No money is dep/wd,no logs found")
              print(" ")
              acc_login(i);
         else: 
              print(content)
              acc_login(i);
      except OSError:
        print("                         ")
        print("               Warning⚠There is no FILES regarding this Account.\n                    Eihter the Files are deleted or moved  ")
        print(" ")
        acc_login(i);
     elif(option == 2):
       try:
        mypath = os.path.join("Userdatabase",i)
        with open(mypath+".txt", "r") as amount:
         content=amount.read()
         if not content:
          print(" ")
          print("                   The Amount in your Account is : '0' ZERO-Rupees")
          print(" ")
          acc_login(i);
         else:
          print(" ")
          print("                   The Amount in your Account is :" ,content , " Rupees")
          print(" ")
          acc_login(i);
       except:
         print("                         ")
         print("               Warning⚠There is no FILES regarding this Account.\n                    Eihter the Files are deleted or moved  ")
         print(" ")
         acc_login(i);
     elif(option == 3):
          p=os.getcwd()
          exec(open(p+'\maincall.py').read())
     else:
        print("Invalid Option !! ")
