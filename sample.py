# LIST COMPREHENSION
[{}, {"name": "djnw", "age": 33, "email": "u2h4", "pin": 324, "accountno": "abs@123", "balance": 0}, {"name": "hjdf", "age": 321, "email": "wef", "pin": 1212, "phon_no": 1231231234, "accountno": "x7W9i45V", "balance": 0}]
account = input("enter account no")
pin = int(input("enter your pin"))
user_data = [i for i in data if i ['accountno'] == account and i['pin'] == pin]
print(user_data)
if user_data == False :
    print("no such user")
else:
    balance = int(input("enter amount"))
    user_data[0]['balance'] += balance
    print(user_data)
    

