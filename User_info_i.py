from random import randint
import hashlib
import os
def create_acc():
    user_pswd=open("User Data  Base.txt" , "a")
    ###################Input Details###
    print("                  ----------Enter Customer Details----------")
    a=str(input("                 |Enter Customer Name : " ))
    j=a.replace(" ","")
    b=str(input("                 |Enter Father  Name  : " ))
    k=b.replace(" ","")
    c=str(input("                 |Enter Date-of-Birh  : " ))
    d=str(input("                 |Enter CNIC          : " ))
    e=str(input("                 |Enter Address       : " ))
    l=e.replace(" ",",")
    f=str(input("                 |Enter Phone Number  : " ))
    g=str(input("                 |Enter Account Type  : " ))
    ####################
    ####################User Acc No generator####
    #userpswd=open("password.txt" , "r")
    h=randint(1,1000)
    convert = str(h)
    print("                 |Your Acc Number is  :",h )
    ####################
    ####################Remain Info####   
    i=str(input("                 |Enter Password      : " ))
    print("                 |------------------------------------------")
    hash2= hashlib.md5(i.encode())
    hex_dig2 = hash2.hexdigest()
    print(" ")
    ####################
    user_pswd.write('\n')
    user_pswd.write("Name : " + j)
    user_pswd.write('\n')
    user_pswd.write("Father Name : " + k)
    user_pswd.write('\n')
    user_pswd.write("CNIC Number :  " + d)
    user_pswd.write('\n')
    user_pswd.write("Residential Addresss : " +l)
    user_pswd.write('\n')
    user_pswd.write("Phone No : " + f)
    user_pswd.write('\n')
    user_pswd.write("Account Type : "+ g)
    user_pswd.write('\n')
    user_pswd.write("Account No : " + convert)
    user_pswd.write('\n')
    user_pswd.write("Account Pswd : " + hex_dig2)
    user_pswd.write('\n')
    user_pswd.write("                              =======================        ")
    user_pswd.close()
    ###################Password Witing#####
    pswd=open("pswd.txt","a")
    with open("pswd.txt") as aaa:
     first = aaa.read(1)
     if not first:
       pswd.write(convert)
       pswd.write(":")
       pswd.write(hex_dig2)
     else:
       pswd.write('\n' + convert)
       pswd.write(" ")
       pswd.write(hex_dig2)
       pswd.write(" ")
       pswd.write(j)
    #########################
    mypath = os.path.join("Userdatabase",convert)
    path= os.path.join("logs",convert)
    try:
        file=open(mypath+".txt","w+")
        fil=open(path+".txt","w+")
        file.close()
        fil.close()
    except OSError:
        print("               Account is Not Created...⚠ Please Delete User Entry")
    else:
        print("                     Account is Sucessfully Created!!")
    return True

