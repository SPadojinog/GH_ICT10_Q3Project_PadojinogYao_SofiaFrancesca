# Seatwork #2: Intramurals Eligibility Checker
from pyscript import document, display


def check_eligibility(e):
    registered = document.querySelector('input[name="registered"]:checked')
    medical = document.querySelector('input[name="medical"]:checked')
    grade = document.getElementById("grade").value
    section = document.getElementById("section").value.lower()

    document.getElementById("result").innerHTML = ""

    # Check for missing info
    if registered and medical and grade and section == "":
        display("Please answer if you are registered online.", target="result")
    
    if registered == "":
        display("Please answer if you are registered online.", target="result")
    elif medical == "":
        display("Please answer if you have a medical clearance.", target="result")
    elif grade == "":
        display("Please enter your grade level.", target="result")
    elif section == "":
        display("Please enter your section.", target="result")
    else:
        registered = registered.value
        medical = medical.value
        grade = int(grade)

    # Medical and Eligible Checker
    if registered != "Yes":
        display("❌ Please register online to join the Intramurals.", target="result")
    elif medical != "Yes":
        display("❌ Please secure a medical clearance before joining.", target="result")
    elif grade < 7 or grade > 10:
        display("❌ Only students from Grades 7–10 are eligible.", target="result")
    elif section == "emerald":
        display("🎉 Congratulations! You are eligible! You are Team Blue Bears! 🐻", target="result")
    elif section == "ruby":
        display("🎉 Congratulations! You are eligible! You are Team Yellow Tigers! 🐯", target="result")
    elif section == "sapphire":
        display("🎉 Congratulations! You are eligible! You are Team Red Bulldogs! 🐶", target="result")
    elif section == "topaz":
        display("🎉 Congratulations! You are eligible! You are Team Green Hornets! 🐝", target="result")
    else:
        display("❌ Invalid section.", target="result")

