""" this program is a simple login system that checks the username and password against a predefined dictionary of users. 
    authors: Abdalla Farah
    date: 02/19/2026
"""
# Define a dictionary of usernames and passwords
username = {    
            "abdalla" : "Abdalla_123",
            "farah" : "Afarah_123",
            "william" : "Bill_12",
            "guest" : "guest"

            }
# Initialize the number of login attempts
attempts = 0
# Loop until the user has made 3 attempts
while attempts < 3:
    user_login = (input("Enter your username: "))
    #remove any white space and lower all cases.
    login = user_login.lower().strip()
    # if the username is not found in the dictionary, print an error message and increment the attempts counter
    if login not in username:
        print("\nUser not found. Please try again.")
        attempts += 1
        continue
    if login in username:
        # if the username is found, prompt the user for their password and check if it matches the password in the dictionary
        password = (input("Enter your password: "))
        if password == username[login]:
            # if the password is correct, assing security level for both guest and other users and print a welcome message with security level then exit the program. 
            if username[login] == "guest":
                security_level = "guest access"
            else:
                security_level = "security level 1"

            print(f"\nWelcome, {login}. You have {security_level}")
         
            exit()
        # if the password is incorrect then print denial message and exit the program.
        else:
            print("\nAccess denied.")
            
        break
            
   