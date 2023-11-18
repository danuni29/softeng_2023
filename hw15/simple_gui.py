import random

import PySimpleGUI as sg
import requests  # 변경

sg.theme("Kayak")

layout = [
    [sg.Text("요일을 입력해주세요(ex.월): "), sg.InputText(key="day"), sg.Button("Get Day")],  # 수정
    [sg.Output(size=(60, 10))]
]

window = sg.Window("점메추", layout)

BASE_URL = "http://127.0.0.1:8000/menu/"

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == "Get Day":
        day = values["day"]
        url = f"{BASE_URL}{day}"

        try:
            response = requests.get(url)
            menu = response.json()
            sg.Print(f"{day}요일은 고민하지 말고~ {random.choice(menu)} 이걸 드세요^^")
        except Exception as e:
            sg.Print(f"Error: {e}")


window.close()