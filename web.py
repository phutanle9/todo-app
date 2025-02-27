import streamlit as st
import functions

# Initialize the to-do list
todos = functions.get_todos()

# Streamlit app title and description
st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity")

# Display the to-do list with checkboxes
for todo in todos:
    if st.checkbox(todo, key=todo):
        # Logic for when a checkbox is checked (optional, e.g., mark as completed)
        pass

# Input field to add a new to-do (with a label)
new_todo = st.text_input("New Todo", placeholder="Add new todo...")

# Button to add the new to-do to the list
if st.button("Add Todo") and new_todo:
    functions.add_todo(new_todo)  # Assuming `add_todo` is a function in your `functions.py` to save the new to-do
    st.experimental_rerun()  # Refresh the app to show the new to-do
