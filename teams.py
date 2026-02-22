# Team Checker
from pyscript import document, display


def check_eligibility(e):
    registered_input = document.querySelector('input[name="registered"]:checked')
    medical_input = document.querySelector('input[name="medical"]:checked')
    grade_input = document.getElementById("grade").value
    section_input = document.getElementById("section").value.lower()

    document.getElementById("result").innerHTML = ""

    # INFORMATION
    if not grade and not section and not registered and not medical:
        display(f"❌ Please fill all fields.", target="result")

    grade = int(grade)
    registered = registered.value
    medical = medical.value

    if registered != "Yes":
        display(f"❌ You must register online.", target="result")
    if medical != "Yes":
        display(f"❌ You need medical clearance.", target="result")
    if grade < 7 or grade > 10:
        display(f"❌ Only Grades 7-10 are eligible.", target="result")

    teams = {
        "emerald": "Blue Bears 🐻",
        "ruby": "Yellow Tigers 🐯",
        "sapphire": "Red Bulldogs 🐶",
        "topaz": "Green Hornets 🐝"
    }

    if section in teams:
        display(f"🎉 Eligible! You are Team {teams[section]}!", target="result")
    else:
        display(f"❌ Invalid section.", target="result")



