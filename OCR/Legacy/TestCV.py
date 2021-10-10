import PySimpleGUI as sg
import cv2
import numpy as np

def main():
    sg.theme("LightGreen")

    # Define the window layout
    layout_left = [
        [sg.Text("Text right", size=(50,1), font='Courier 20', background_color='white', key='-textr-')],
        [sg.Button("Exit", size=(10, 1))],
    ]

    layout_right = [
        [sg.Image(size=(10,20), filename="", key="-IMAGE-")],
    ]

    layout = [
        [sg.Column(layout_left),
        sg.VSeparator(),
        sg.Column(layout_right)]
    ]


    w, h = sg.Window.get_screen_size()

    # Create the window and show it without the plot
    window = sg.Window("OpenCV Integration", layout, location=(800, 400), size=(w,h))

    cap = cv2.VideoCapture(0)

    while True:
        event, values = window.read(timeout=20)
        if event == "Exit" or event == sg.WIN_CLOSED:
            break

        ret, frame = cap.read()

       
        imgbytes = cv2.imencode(".png", frame)[1].tobytes()
        window["-IMAGE-"].update(data=imgbytes)

    window.close()

main()