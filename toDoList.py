import streamlit as st

def app():
    st.title("To Do List")

    # Buat list kosong untuk menyimpan tasks
    if 'tasks' not in st.session_state:
        st.session_state.tasks = []

    # Tampilkan input text untuk menambahkan task baru
    new_task = st.text_input("")

    # Jika tombol "Tambah" ditekan, tambahkan task baru ke dalam list
    if st.button("Tambah"):
        if new_task != "":
            st.session_state.tasks.append({"task": new_task, "completed": False})
            new_task = ""  # Reset input setelah task ditambahkan

    # Tampilkan tasks pada list
    if len(st.session_state.tasks) > 0:
        st.subheader("Tasks:")
        for i, task_data in enumerate(st.session_state.tasks):
            task = task_data["task"]
            completed = task_data["completed"]
            
            # Tampilkan checkbox untuk setiap task
            task_col, delete_button_col = st.columns([10, 1])
            with task_col:
                completed = st.checkbox(f"{i+1}. {task}", completed, key=f"task_checkbox_{i}")
                st.session_state.tasks[i]["completed"] = completed

            # Tampilkan tombol hapus kecil di sebelah opsi
            with delete_button_col:
                delete_button = st.button(label="x", key=f"delete_{i}", help=f"x {task}")
                if delete_button:
                    st.session_state.tasks.pop(i)
                    break  # Keluar dari loop setelah menghapus task