 #Sign Up
from pyscript import display, document


def sign_up_account(e):
    document.getElementById("output").innerHTML = ""  # clears previous answers
    username = document.getElementById("username").value.strip() 
    password = document.getElementById("password").value

    # INFORMATION
    if username == "" and password == "": 
        display("❌ Please fill in the information before creating account.", target="output") #Displays if no input in username and password
    elif username == "": 
        display("❌ Please input your username.", target="output") #Displays if no input in username
    elif password == "":
        display("❌ Please input your password.", target="output")  #Displays if no input in password

    # CHARACTERS 
    elif len(username) < 7: 
        display("❌ Username must contain at least 7 characters.", target="output") #Displays if username lower than or equal to 7 characters
    elif len(password) < 10:
        display("❌ Password must contain at least 10 characters.", target="output") #Displays if password lower than or equal 10 characters

    # PASSWORD
    elif password.isalpha(): 
        display("❌ Password must contain at least one number.", target="output") #Displays if password is only all letters
    elif password.isdigit(): 
        display("❌ Password must contain at least one letter.", target="output") #Displays if password is only all numbers
    
    else:
        display("✅ Account successfully created!", target="output")


