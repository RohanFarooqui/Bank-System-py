import hashlib
def login_acc(acc,password):
  hash2= hashlib.md5(password.encode())
  hex_dig2 = hash2.hexdigest()
  with open('pswd.txt', "r") as file:
   for line in file:
    lis=[]
    k=(line.split(' '))
    lis.append(k[0])
    lis.append(k[1])
    lis.append(k[2])
    lis[-1] = lis[-1].strip()
    if (acc == k[0] and hex_dig2 == k[1]):
        print(" ")
        print("                         Welcome, "+k[2])
        print(" ")
        return True
        break
    elif (acc != k[0] and hex_dig2 != k[1]):
        return False
   else:
        return None
     
    
        
