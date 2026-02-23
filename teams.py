# Team Checker
from pyscript import document, display


def check_eligibility(e):
    registered_input = document.querySelector('input[name="registered"]:checked') 
    medical_input = document.querySelector('input[name="medical"]:checked') 
    grade_input = document.getElementById("grade").value 
    section_input = document.getElementById("section").value.lower() 

    #clears previous answers
    document.getElementById("result").innerHTML = "" 

    # Check if fields are empty
    if not grade_input or not section_input or not registered_input or not medical_input:   
        display(f"❌ Please fill all fields.", target="result") #

    else:
        grade = int(grade_input) 
        registered = registered_input.value 
        medical = medical_input.value

        if registered != "Yes":
            display(f"❌ You must register online.", target="result") #Displays if they have not registered
        elif medical != "Yes":  
            display(f"❌ You need medical clearance.", target="result") #Displays if they have no medical clearance
        elif grade < 7 or grade > 10:
            display(f"❌ Only Grades 7-10 are eligible.", target="result")  #Displays that only grade 7-10 are allowed
        else:
            teams = { 
                "emerald": "Blue Bears 🐻",
                "ruby": "Yellow Tigers 🐯",
                "sapphire": "Red Bulldogs 🐶",
                "topaz": "Green Hornets 🐝"
            }  #Displays if they input emerald in the section field, they are in Blue Bears

            #Displays all fields are filled and correct
            if section_input in teams:  
                display(f"🎉 Congratulations! You are Eligible! You're Team {teams[section_input]}!", target="result") 
            else: 
                display(f"❌ Invalid section.", target="result")  #Displays if incorrect section given


