# Project: List of Players
from pyscript import display, document


def player_list (e):
    document.getElementById('output').innerHTML = " "

    players = [
        "1) Aseo", "2) Batac", "3) Calanglang", "4) Dee", "5) De Guzman",
        "6) Dolor", "7) Galvez", "8) Garces", "9) Grospe", "10) Hizon",
        "11) Intalan", "12) Ko", "13) Lagman", "14) Law", "15) Macabago",
        "16) Martinez", "17) Medina", "18) Mendoza", "19) Mergal", "20) Ngo",
        "21) Padojinog", "22) Rivera", "23) Shrestha", "24) Uy", "25) Yao"
    ]

    for player in players:
        display(player, target='output')


