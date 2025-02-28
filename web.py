import streamlit as st
import functions

# Initialize the to-do list from functions
todos = functions.get_todos()

def add_todo():
    # Retrieve the new todo from session state and append it to the todos list
    new_todo = st.session_state["new_todo"] + "\n"
    if new_todo:  # Ensure that the new todo is not empty
        todos.append(new_todo)  # Append the new todo
        functions.write_todos(todos)  # Save the updated list
        st.session_state["new_todo"] = ""  # Clear the input field after adding

# Streamlit app title and description
st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity")

# Iterate through the todos and create checkboxes
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)  # Display each todo as a checkbox

    # If checkbox is checked, remove it from the todos list
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        st.rerun()  # Trigger a rerun of the app to reflect changes

# Input field to add a new to-do
new_todo = st.text_input("New Todo", placeholder="Add new todo...", on_change=add_todo, key='new_todo')
