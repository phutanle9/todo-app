import time
import FreeSimpleGUI as sg
import functions
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt","w") as file:
        pass
sg.theme("Black")

# Text element for displaying the time
clock = sg.Text('', key='clock')

# Label for to-do input
todo_label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter a to-do", key='todo')

# Listbox to display current todos
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[45, 10])

# Buttons for adding, editing, completing, and exiting
edit_button = sg.Button("Edit")
add_button = sg.Button(size=2, image_source="add.png", mouseover_colors="LightBlue2", tooltip="Add Todo", key="Add")
complete_button = sg.Button(size=10, image_source="complete.png", mouseover_colors="LightBlue2", tooltip="Complete Todo", key="Complete")
exit_button = sg.Button("Exit")

# Create window layout
window = sg.Window('My To-do App',
                   layout=[[clock],
                           [todo_label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read(timeout=200)  # Update every 200ms to keep clock current
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))  # Update the clock
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
            window['todo'].update('')  # Clear the input box after adding a to-do

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
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)  # Remove the completed task from the list
                functions.write_todos(todos)
                window['todos'].update(values=todos)  # Refresh Listbox with updated todos
                window['todo'].update('')  # Clear the input box after completing a to-do
            except IndexError:
                sg.popup("Please select an item to mark as complete")

        case 'Exit':
            break

        case 'todos':
            if values['todos']:
                window['todo'].update(value=values['todos'][0])  # Show selected todo in input box

        case sg.WIN_CLOSED:
            break

window.close()
