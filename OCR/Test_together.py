import PySimpleGUI as sg
import cv2
import numpy as np
import cv2
from OCR import ocr_core
from chat_rules import rules

def main():
    sg.theme("LightGreen")

    # Define the window layout
    layout_left = [
        [sg.Text("Text right", size=(50,1), font='Courier 20', background_color='white', key='-textr-')],
        [sg.Button("Exit", size=(10, 1))],
        [sg.Button("Shoot", size=(10,1))],
        [sg.Text("", size=(50,1), font='Courier 20', background_color='white', key='-Question-')],
        [sg.Text("", size=(50,1), font='Courier 20', background_color='white', key='-Answer-')],


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
    window = sg.Window("OpenCV Integration", layout, location=(800, 400), size=(w,h), return_keyboard_events=True)

    cap = cv2.VideoCapture(0)
    
    img_counter = 0

    while True:
        event, values = window.read(timeout=20)
        if event == "Exit" or event == sg.WIN_CLOSED:
            break


        ret, frame = cap.read()
        if not ret:
            print("failed to grab frame")
            break
        
        k = cv2.waitKey(1)

        if event == "Shoot":
            # SPACE pressed
            img_name = "frame{}.png".format(img_counter)
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            img_counter += 1

            print("\n\n\Hold on for me...")
            print(img_counter)


            #Detect the text in the taken snapshop
            ocred = ocr_core(f"frame{img_counter-1}.png")
            print(f"question is {ocred}")
            answer = rules(ocred)
            window["-Question-"].update(ocred)
            window["-Answer-"].update(answer)

       
        imgbytes = cv2.imencode(".png", frame)[1].tobytes()
        window["-IMAGE-"].update(data=imgbytes)

    cap.release()
    window.close()
    
main()