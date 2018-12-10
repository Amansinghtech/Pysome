#This prgram is created by AMAN SINGH
#Try To modify it by your own
from cryptography.fernet import Fernet
import os

file = open(input("enter your key file location"),"rb")  
key = file.read()
file.close()
import os

def filelist():
    mylist = []
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".encrypted"):
                mylist.append(os.path.join(root, file))

    return mylist

print(filelist())

local = filelist()




def file_decrypt(key, files):
    
    for name in files:
        if (name!="Ransom_decrypt.py"): 
            with open(name,'rb') as f:
                data = f.read()

            fernet = Fernet(key)
            decrypted = fernet.decrypt(data)
            decrypted_file = name + ".decrypted"
            try:
                with open(decrypted_file, 'wb') as f:
                    f.write(decrypted)
                    os.remove(name)
            except:
                continue

file_decrypt(key, local)
