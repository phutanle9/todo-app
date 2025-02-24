from cProfile import label

import FreeSimpleGUI as sg
from pandas.core.config_init import pc_max_info_rows_doc
from scipy.constants import value

import functions
from myapp import todo_to_remove, index

label= sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter a to-do",key='todo')

list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True,size=[45,10])
edit_button = sg.Button("Edit")

add_button = sg.Button("Add")

window = sg.Window('My To-do App',
                   layout=[[label],[input_box,add_button],[list_box,edit_button]],
                   font=('Helvetica',20))
# window.read()

while True:
    event, values = window.read()
    print(1, event)
    print(2, values)
    print(3, values['todos'])
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case 'Edit':
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']

            todos= functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(value=todos)
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break


window.close()