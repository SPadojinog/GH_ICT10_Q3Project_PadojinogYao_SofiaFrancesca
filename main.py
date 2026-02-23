 #Sign Up
from pyscript import display, document


def sign_up_account(e):
    document.getElementById("output").innerHTML = ""  # clears previous answers
    username = document.getElementById("username").value.strip() 
    password = document.getElementById("password").value

    # INFORMATION
    if username == "" and password == "": #Displays if no input in username and password
        display("❌ Please fill in the information before creating account.", target="output")
    elif username == "": #Displays if no input in username
        display("❌ Please input your username.", target="output")
    elif password == "": #Displays if no input in password
        display("❌ Please input your password.", target="output")

    # CHARACTERS 
    elif len(username) =< 7: #Displays if username lower than or equal to 7 characters
        display("❌ Username must contain at least 7 characters.", target="output")
    elif len(password) =< 10: #Displays if password lower than or equal 10 characters
        display("❌ Password must contain at least 10 characters.", target="output")

    # PASSWORD
    elif password.isalpha(): #Displays if password is only all letters
        display("❌ Password must contain at least one number.", target="output")
    elif password.isdigit(): #Displays if password is only all numbers
        display("❌ Password must contain at least one letter.", target="output")
    
    else:
        display("✅ Account successfully created!", target="output")

