#Function to validate a phone number
import re
def phonenumbervalidator(number):
    pattern='^[6-9][0-9]{9}$|^[0][6-9][0-9]{9}$|^[+][9][1][6-9][0-9]{9}$'
    if re.match(pattern, str(number)):
        return True
    return False
phonenumbervalidator("+918985611833")

def emailvalidator(email):
    pattern = "^[0-9a-z][0-9a-z_.]{3,20}[0-9a-z][@][a-z0-9]{4,8}[.][a-z]{2,8}$"
    if re.match(pattern, str(email)):
        return True
    return False
emailvalidator("nimmanaprasanthlove@gmail.com")



# Function to append,edit,delete a contact in contacts dictionary
# first need to create a contacts dictionary

contacts={}

def addcontacts(name, phone):
    if name not in contacts:
        contacts[name]=phone
        print("contact %s added" % name)
        
    else:
        print("contact %s already exists" % name)
    return
        
addcontacts("prasanth", "7609999606")
    
