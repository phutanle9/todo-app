import time

import FreeSimpleGUI as sg
from scipy.constants import value
import time
import functions

sg.theme("DarkPurple4")

clock = sg.Text('', key='clock')
# Rename 'label' to avoid conflict
todo_label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter a to-do", key='todo')

list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
add_button = sg.Button(size=10, image_source="add.png")
complete_button = sg.Button(size=10, image_source="complete.png")
exit_button = sg.Button("Exit")


window = sg.Window('My To-do App',
                   layout=[[clock],
                           [todo_label],
                           [input_box, add_button],
                           [list_box, edit_button,complete_button],
                           [exit_button]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    print(1, event)
    print(2, values)
    print(3, values['todos'])

    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)  # Refresh Listbox with updated todos
        case 'Edit':
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)  # Refresh Listbox with updated todos
            except IndexError:
                sg.popup("Please select an item first")
        case "Complete":
            todo_to_complete = values['todos'][0]
            todos = functions.get_todos()
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todos'].update(value='')

        case 'Exit':
            break

        case 'todos':
            if values['todos']:
                window['todo'].update(value=values['todos'][0])  # Show selected todo in input box
        case sg.WIN_CLOSED:
            exit()

window.close()
