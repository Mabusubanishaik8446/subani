def phonenum(phonenum):
    import re
    phonenum=input("enter phone number")
    pattern='^[6-9][0-9]{9}$|^[+][9][1][6-9][0-9]{9}$'
    if re.match(pattern,phonenum):
        print("valid number")
    else:
        print("not valid")
        
        
    
def email():   
    import re
    email=input("enter email id: ")
    pattern='^[0-9a-z][0-9a-z_.]{5,20}[@][a-z]{5,10}[.][a-z]{2,5}$'
    if re.match(pattern,email):
        print("valid email")
    else:
        print("not valid")
        