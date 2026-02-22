# Project: List of Players
from pyscript import display, document


def show_team(team_list):
    document.getElementById("output").innerHTML = ""

    greens = [
        "1) ASEO, TESSA YSABELLE MARZAN",
        "2) BATAC, ANAKIN MIGUEL QUINTO",
        "3) CALANGLANG, NERIZA ALIPIO",
        "4) DEE, AARON JAMES GONZALO",
        "5) DE GUZMAN, VITO ANTONIO OLIVERA",
        "6) DOLOR, HARVEY WAYNE BATINO",
        "7) GALVEZ, SELENA MANSUETO",
        "8) GARCES, ADRIANNA MALANUM",
        "9) GROSPE, JILLIAN CUISON",
        "10) HIZON, EDUARDO ALONSO MAGSOMBOL",
        "11) INTALAN, MARGO ZERA FRANCISCO",
        "12) KO, ATASHA SOLEIL ROMERO",
        "13) LAGMAN, ALIJAH RAIN",
        "14) LAW, MARCUS CHRISTIAN PANLILIO",
        "15) MACABAGO, SITTIE AINAH MARIANO",
        "16) MARTINEZ, EUAN JUSTIN LIM",
        "17) MEDINA, KELSEY CLAIRE LAGO",
        "18) MENDOZA, MICHAELA YSABELLE CAYNO",
        "19) MERGAL, MANUEL JACINTO GUARINO",
        "20) NGO, SETH GARETT GOMEZ",
        "21) PADOJINOG, SOFIA LAURENCE FABELLA",
        "22) RIVERA, BENIGNO IGNACIO JHOCSON",
        "23) SHRESTHA, ISHAN JUSTICE QUIAMBAO",
        "24) UY, JENNIFER LORRAINE SANCHEZ",
        "25) YAO, FRANCESCA JEAN KHO"
    ]
    
    blues = greens
    reds = greens
    yellows = greens

    
for player in team_list:
    display(player, target="output")
    
def green_list(event):
    display(greens, target="output")

def blue_list(event):
    display(blues, target="output")

def red_list(event):
    display(reds, target="output")

def yellow_list(event):
    display(yellows, target="output")
