# Team Checker
from pyscript import document, display


def check_eligibility(event):
    registered_input = document.querySelector('input[name="registered"]:checked')
    medical_input = document.querySelector('input[name="medical"]:checked')
    grade_input = document.getElementById("grade").value
    section_input = document.getElementById("section").value.lower()

    document.getElementById("result").innerHTML = ""

    # INFORMATION
    if registered_input is None:
        display("❌ Please answer if you are registered online.", target="result")
        return
    if medical_input is None:
        display("❌ Please answer if you have a medical clearance.", target="result")
        return
    if grade_input.strip() == "":
        display("❌ Please enter your grade level.", target="result")
        return
    if section_input.strip() == "":
        display("❌ Please enter your section.", target="result")
        return

    # Convert values
    registered = registered_input.value
    medical = medical_input.value
    try:
        grade = int(grade_input)
    except ValueError:
        display("❌ Invalid grade. Please enter a number.", target="result")
        return

    # Eligibility checks
    if registered != "Yes":
        display("❌ Please register online to join the Intramurals.", target="result")
        return
    if medical != "Yes":
        display("❌ Please secure a medical clearance before joining.", target="result")
        return
    if grade < 7 or grade > 10:
        display("❌ Only students from Grades 7–10 are eligible.", target="result")
        return

    # Section → Team mapping
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
