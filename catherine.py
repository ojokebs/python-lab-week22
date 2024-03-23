"""zip = input("please enter your zip code: ")
l = len(zip)
if l==5 :
    print("your entry is valid")
else:
    print("please enter a valid zip code")
"""

email = input("what is your email address: ")
e = "@" in email
if e:
    print("the email is valid")
else:
    print("email is invalid")