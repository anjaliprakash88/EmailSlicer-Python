def email(x):
    if "@" in x:
        username, domain = x.split("@")
        print("Username:", username)
        print("Domain:", domain)
    else:
        print("Invalid email address format")

x= input("Enter an email address: ") 
email(x)



