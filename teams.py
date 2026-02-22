# Team Checker
from pyscript import document, display


def check_eligibility(e):
    registered_input = document.querySelector('input[name="registered"]:checked')
    medical_input = document.querySelector('input[name="medical"]:checked')
    grade_input = document.getElementById("grade").value
    section_input = document.getElementById("section").value.lower()

    document.getElementById("result").innerHTML = ""

    if not grade_input or not section_input or not registered_input or not medical_input:
        display("❌ Please fill all fields.", target="result")

    grades = int(grade_input)
    registered = registered_input.value
    medical = medical_input.value

    if registered != "Yes":
        display("❌ You must register online.", target="result")
    if medical != "Yes":
        display("❌ You need medical clearance.", target="result")
    if grades < 7 or grades > 10:
        display("❌ Only Grades 7-10 are eligible.", target="result")

    teams = {
        "emerald": "Blue Bears 🐻",
        "ruby": "Yellow Tigers 🐯",
        "sapphire": "Red Bulldogs 🐶",
        "topaz": "Green Hornets 🐝"
    }

    if section_input in teams:
        display(f"🎉 Congratulations! You are Eligible! You're Team {teams[section_input]}!", target="result")
    else:
        display("❌ Invalid section.", target="result")

