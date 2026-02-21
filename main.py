 #Skills Test
from pyscript import display, document


def sign_up_account(e):
    document.getElementById("output").innerHTML = ""
    username = document.getElementById("username").value.strip()
    password = document.getElementById("password").value

    # INFORMATION
    if username == "" and password == "":
        display("❌ Please fill in the information before creating account.", target="output")
    elif username == "":
        display("❌ Please input your username.", target="output")
    elif password == "":
        display("❌ Please input your password.", target="output")

    # CHARACTERS 
    elif len(username) < 7:
        display("❌ Username must contain at least 7 characters.", target="output")
    elif len(password) < 10:
        display("❌ Password must contain at least 10 characters.", target="output")

    # PASSWORD
    elif password.isalpha():
        display("❌ Password must contain at least one number.", target="output")
    elif password.isdigit():
        display("❌ Password must contain at least one letter.", target="output")
    
    else:
        display("✅ Account successfully created!", target="output")