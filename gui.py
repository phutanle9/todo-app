from cProfile import label

import FreeSimpleGUI as sg

label= sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter a to-do")
add_button = sg.Button("Add")

window = sg.Window('My To-do App',layout=[[label],[input_box],[add_button]])
window.read()

print("Hello")


window.close()