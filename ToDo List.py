import streamlit as st

st.title("To-Do List") # Set title

if "task_list" not in st.session_state: # Ensure list exists for memory
    st.session_state["task_list"] = []

task = st.text_input("Enter your task", " ") # Input field

if st.button("Add Task"): # Add task button
    if task.strip():
        st.session_state["task_list"].append(task.strip()) # Add task to list

st.subheader("Your Tasks")
completed_tasks = []

for i, t in enumerate(st.session_state["task_list"]):
    # Give each checkbox a unique key to keep Streamlit happy
    if st.checkbox(f"{i + 1}. {t}", key=f"task_{i}"):
        completed_tasks.append(t)

# Remove completed tasks after collecting them
for task in completed_tasks:
    st.session_state["task_list"].remove(task)
    st.rerun()

if st.button("Clear All Tasks"):
    st.session_state["task_list"] = []
    st.rerun()

