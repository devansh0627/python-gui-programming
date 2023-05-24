from tkinter import *
from tkinter import filedialog
from tkinter import simpledialog
import os
import shutil
window =Tk()
window.title("File Manager")
window.geometry("400x300")
def browse_directory():
    directory = filedialog.askdirectory()
    if directory:
        current_directory.set(directory)
        update_file_list()

def update_file_list():
    directory = current_directory.get()
    files = os.listdir(directory)
    file_listbox.delete(0,END)
    for file in files:
        file_listbox.insert(END, file)

def delete_file():
    selected_file = file_listbox.get(ACTIVE)
    if selected_file:
        file_path = os.path.join(current_directory.get(), selected_file)
        os.remove(file_path)
        update_file_list()

def rename_file():
    selected_file = file_listbox.get(ACTIVE)
    if selected_file:
        file_path = os.path.join(current_directory.get(), selected_file)
        extension = os.path.splitext(selected_file)[1]
        new_name = simpledialog.askstring("Rename File", "Enter new name:", initialvalue=selected_file)
        if new_name:
            new_file_path = os.path.join(current_directory.get(), new_name + extension)
            os.rename(file_path, new_file_path)
            update_file_list()
def move_file():
    selected_file = file_listbox.get(ACTIVE)
    if selected_file:
        source_path = os.path.join(current_directory.get(), selected_file)
        destination = filedialog.askdirectory()
        if destination:
            destination_path = os.path.join(destination, selected_file)
            shutil.move(source_path, destination_path)
            update_file_list()

def copy_file():
    selected_file = file_listbox.get(ACTIVE)
    if selected_file:
        file_path = os.path.join(current_directory.get(), selected_file)
        destination = filedialog.askdirectory()
        if destination:
            new_file_path = os.path.join(destination, selected_file)
            with open(file_path, 'rb') as source:
                with open(new_file_path, 'wb') as destination:
                    destination.write(source.read())
            update_file_list()

current_directory = StringVar()

# Frame for directory selection
directory_frame = Frame(window)
directory_frame.pack(pady=10)

directory_label = Label(directory_frame, text="Current Directory:")
directory_label.pack(side=LEFT)

directory_entry = Entry(directory_frame, textvariable=current_directory)
directory_entry.pack(side=LEFT)

browse_button = Button(directory_frame, text="Browse", command=browse_directory)
browse_button.pack(side=LEFT)

# File Listbox
file_listbox = Listbox(window,width=100,relief=SUNKEN,borderwidth=6)
file_listbox.pack(fill=X,pady=10)

# Buttons for file operations
button_frame = Frame(window)
button_frame.pack()

delete_button = Button(button_frame, text="Delete", command=delete_file)
delete_button.grid(row=0, column=0, padx=5)

rename_button = Button(button_frame, text="Rename", command=rename_file)
rename_button.grid(row=0, column=1, padx=5)

move_button = Button(button_frame, text="Move", command=move_file)
move_button.grid(row=0, column=2, padx=5)

copy_button = Button(button_frame, text="Copy", command=copy_file)
copy_button.grid(row=0, column=3, padx=5)

window.mainloop()
