# Team Checker
from pyscript import document, display


def check_eligibility(e):
    registered_input = document.querySelector('input[name="registered"]:checked')
    medical_input = document.querySelector('input[name="medical"]:checked')
    grade_input = document.getElementById("grade").value
    section_input = document.getElementById("section").value.lower()

    document.getElementById("result").innerHTML = ""

    # ACCOUNT INFORMATION
    if registered_input == "":
        display("❌ Please answer if you are registered online.", target="result")
    if medical_input  == "":
        display("❌ Please answer if you have a medical clearance.", target="result")
    if grade_input == "":
        display("❌ Please enter your grade level.", target="result")
    if section_input == "":
        display("❌ Please enter your section.", target="result")
    else:
        registered = registered.value
        medical = medical.value
        grade = int(grade)

    # Eligibility checks
    if registered != "Yes":
        display("❌ Please register online to join the Intramurals.", target="result")
    if medical != "Yes":
        display("❌ Please secure a medical clearance before joining.", target="result")
    if grade < 7 or grade > 10:
        display("❌ Only students from Grades 7–10 are eligible.", target="result")

    teams = {
        "emerald": "Blue Bears 🐻",
        "ruby": "Yellow Tigers 🐯",
        "sapphire": "Red Bulldogs 🐶",
        "topaz": "Green Hornets 🐝"
    }

    if section_input in teams:
        display(f"🎉 Congratulations! You are eligible! You are Team {teams[section_input]}!", target="result")
    else:
        display("❌ Invalid section.", target="result")
