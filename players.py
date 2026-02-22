# Project: List of Players
from pyscript import display, document


def players_list (e):
    document.getElementById('output').innerHTML = " "

    greens = [
        "1) ASEO, TESSA YSABELLE MARZAN", "2) BATAC, ANAKIN MIGUEL QUINTO", "3) CALANGLANG, NERIZA ALIPIO", "4) DEE, AARON JAMES GONZALO", "5) DE GUZMAN, VITO ANTONIO OLIVERA",
        "6) DOLOR, HARVEY WAYNE BATINO", "7) GALVEZ, SELENA MANSUETO", "8) GARCES, ADRIANNA MALANUM", "9) GROSPE, JILLIAN CUISON", "10) HIZON, EDUARDO ALONSO MAGSOMBOL",
        "11) INTALAN, MARGO ZERA FRANCISCO", "12) KO, ATASHA SOLEIL ROMERO", "13) LAGMAN, ALIJAH RAIN", "14) LAW, MARCUS CHRISTIAN PANLILIO", "15) MACABAGO, SITTIE AINAH MARIANO",
        "16) MARTINEZ, EUAN JUSTIN LIM", "17) MEDINA, KELSEY CLAIRE LAGO", "18) MENDOZA, MICHAELA YSABELLE CAYNO", "19) MERGAL, MANUEL JACINTO GUARINO", "20) NGO, SETH GARETT GOMEZ",
        "21) PADOJINOG, SOFIA LAURENCE FABELLA", "22) RIVERA, BENIGNO IGNACIO JHOCSON", "23) SHRESTHA, ISHAN JUSTICE QUIAMBAO", "24) UY, JENNIFER LORRAINE SANCHEZ", "25) YAO, FRANCESCA JEAN KHO"
    ]

    blues = [
        "1) Aseo", "2) Batac", "3) Calanglang", "4) Dee", "5) De Guzman",
        "6) Dolor", "7) Galvez", "8) Garces", "9) Grospe", "10) Hizon",
        "11) Intalan", "12) Ko", "13) Lagman", "14) Law", "15) Macabago",
        "16) Martinez", "17) Medina", "18) Mendoza", "19) Mergal", "20) Ngo",
        "21) Padojinog", "22) Rivera", "23) Shrestha", "24) Uy", "25) Yao"
    ]

    yellows = [
        "1) Aseo", "2) Batac", "3) Calanglang", "4) Dee", "5) De Guzman",
        "6) Dolor", "7) Galvez", "8) Garces", "9) Grospe", "10) Hizon",
        "11) Intalan", "12) Ko", "13) Lagman", "14) Law", "15) Macabago",
        "16) Martinez", "17) Medina", "18) Mendoza", "19) Mergal", "20) Ngo",
        "21) Padojinog", "22) Rivera", "23) Shrestha", "24) Uy", "25) Yao"
    ]

    reds = [
        "1) Aseo", "2) Batac", "3) Calanglang", "4) Dee", "5) De Guzman",
        "6) Dolor", "7) Galvez", "8) Garces", "9) Grospe", "10) Hizon",
        "11) Intalan", "12) Ko", "13) Lagman", "14) Law", "15) Macabago",
        "16) Martinez", "17) Medina", "18) Mendoza", "19) Mergal", "20) Ngo",
        "21) Padojinog", "22) Rivera", "23) Shrestha", "24) Uy", "25) Yao"
    ]

    for greens in greens:
        display(greens, target='output')
    for blues in blues:
        display(blues, target='output')
    for yellows in yellows:
        display(yellows, target='output')
    for reds in reds:
        display(reds, target='output')




