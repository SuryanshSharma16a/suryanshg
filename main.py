# 1.create class bank and perform CRUD operations
# C --> create
# R --> read
# u --> update
# d --> delete
from pathlib import Path
import json
import random
import string

class bank:
    database = "data.json"
    data = []
    try:
        if Path(database).exists():
            print("database exists...!")
            with open(database) as fs:
                data = json.loads(fs.read())
        else:
            print("no such file exists")

    except Exception as err:
        print ("error occurd")

    @classmethod
    def update(cls):
        with open(bank.database,"w") as fs:
            fs.write(json.dumps(cls.data))

    @staticmethod
    def generateACC(self):  # generating random account no
        digit = random.choices(string.digits, k = 4)
        alpha = random.choices(string.ascii_letters, k = 4)
        id = digit + alpha
        random.shuffle(id)
        return "".join(id)

    # creating user
    def createaccount(self):
        info = {
            'name': input("enter your name"),
            'age': int(input("enter your age")),
            'email' : input("enter your email"),
            'pin' : int(input("enter your pin")),
            'phon_no' : int(input("enter your phone no")),
            'accountno' : bank.generateACC(self) ,
            'balance': 0                  }
        
        if info['age']> 18 and len(str(info['pin'])) == 4 and len(str(info['phon_no'])) == 10:
            bank.data.append(info)
            bank.update()
            print("data added to list")
            print(bank.data)
        else:
            print("credintials are not valid !")
    def deposite(self):
        accountno = input("enter your account no:")
        pin = int(input("enter yur pin:"))
        user_data = [i for i in bank.data if i['accountno'] == accountno and i["pin"] == pin]
        if user_data == False:
            print("user not fount")
        else:
            amount = int(input("enter amount you want to add"))
            if amount <= 0 :
                print("invalid amount")
            elif amount > 10000:
                print("greater than 10000 ")
            else:
                user_data[0] ['balance'] += amount
                bank.update()
                print("amount credited")

    def withdraw(self):
        accountno = input("enter your account no:")
        pin = int(input("enter yur pin:"))
        user_data = [i for i in bank.data if i['accountno'] == accountno and i["pin"] == pin]
        if user_data == False:
            print("user not fount")
        else:
            amount = int(input("enter amount you want to withdraw"))
            if amount <= 0 :
                print("invalid amount")
            elif amount > 10000:
                print("greater than 10000 ")
            else:
                if user_data[0]['balance']< amount:
                    print("insufficient balance")
                else:
                        user_data[0] ['balance'] += amount
                        bank.update()
                        print("amount credited")      

                    
    def details(self):
        accountno = input("enter your account no:")
        pin = int(input("enter yur pin:"))
        user_data = [i for i in bank.data if i['accountno']== accountno and i['pin'] == pin]
        if user_data == False:
            print("user not found")
        else:
            for i in user_data[0]:
                print(i, user_data[0][i])  

    def delete(self):
        accountno = input("enter your account no:")
        pin = int(input("enter yur pin:"))
        user_data = [i for i in bank.data if i['accountno']== accountno and i['pin'] == pin]
        if user_data == False:
            print("user not found")
        else:
            print("are you sure you want to delete your account ? (yes/no) ")
            choice = input()
            if choice == "yes" or "Yes":
                ind = bank.data.index(user_data[0])
                bank.data.pop(ind)
                bank.update()
                print("account deleted successfully")
            else:
                print("operation terminated")
    def update_user(self):
        accountno = input("enter your account no:")
        pin = int(input("enter yur pin:"))
        user_data = [i for i in bank.data if i['accountno']== accountno and i['pin'] == pin]
        if user_data == False:
            print("user not found")

        else:
            print("your account no  and pin can't be change once it is created")
            print("enter your details to update them otherwise press enter to skip them")
            new_data = {
                "name" : input("enter your name"),
                "age" : input("enter age"),
                "email": input("enter your email"),               
                "phone_no" : input("enter email"),
                "pin" : (input("Enter your pin: ")) }
    # we take the contact info and pin in str and later typecast to int type                
    ## we take the contact info and pin in string and later tpe cast it into int type
    ## yaha string is liy ele rhe kyunki main database me contact au rpin int me hai aur jab kuch input nhi denge tab wo hap string me save hoga
    ## jab int aur string concatinate hoga to error milegi - literal erroe i.ie not sam edata type  , isliye type caste krwayenge

            if new_data ['name'] == "":
                new_data ['name'] = user_data[0]['name']

            if new_data ['age'] == "":
                new_data ['age'] = user_data[0]['age']

            if new_data ['email'] == "":
                new_data ['email'] = user_data[0]['email']

            if new_data ['phon_no'] == "":
                new_data ['phon_no'] = user_data[0]['phon_no']
            else :
                new_data ['phon_no'] = int (new_data["phone_no"]) ## yaha type casting horhi hai string to int 

            if new_data ['pin'] == "":
                new_data ['pin'] = user_data[0]['pin']
            else:
                new_data ['pin'] = int (new_data["pin"])

            new_data ['accountno.'] = user_data [0]['accountno.']
            new_data['balance'] = user_data [0]['balance']

            user_data[0].update(new_data)
            bank.update()

            print ("Updated Successfully !!! ")

obj = bank()
# MENU
print("press 1 for creating account")
print("press 2 for depositing money")
print("press 3 for withdrawing money")
print("press 4 for account details")
print("press 5 for updating account details")
print("press 6 for deleting account")
choice = int(input("enter what function you want to perform"))
if choice == 1:
    obj.createaccount()
elif choice == 2:
    obj.deposite()
elif choice == 3:
    obj.withdraw()
elif choice == 4:
    obj.details()
elif choice == 5:
    obj.update_user()
elif choice == 6:
    obj.delete()


    


