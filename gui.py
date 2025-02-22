from cProfile import label

import FreeSimpleGUI as sg
from pandas.core.config_init import pc_max_info_rows_doc

import functions

label= sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter a to-do")
add_button = sg.Button("Add")

window = sg.Window('My To-do App',layout=[[label],[input_box],[add_button]],
                   font=('Helvetica',20))
# window.read()


while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break

window.close()