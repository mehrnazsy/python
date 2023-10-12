import tkinter as tk

app=tk.Tk()
app.title('to do list!')

tasks=[]
def save_task_in_file():
    with open ("to_do-list.txt","w") as file:
        for task in tasks:    
            file.write(f'{task}\n')

def view_task():
    try:
        with open ("to_do-list.txt","r") as file:
            lens=file.readlines()
            for len in lens:
                task = len.strip()
                tasks.append(task)
    except FileNotFoundError:
        pass

def add_task():
    task=entry.get()
    if task:
        tasks.append(task)
        update_task_list()
        entry.delete(0,tk.END)
        save_task_in_file()

def update_task_list():
    task_list.delete(0, tk.END)
    for task in tasks:
        task_list.insert(tk.END, task)       

def remove_task():
    selected_task_index = task_list.curselection()
    if selected_task_index:
        tasks.pop(selected_task_index[0])
        update_task_list()
        save_task_in_file()

frame = tk.Frame(app)
frame.pack(pady=10)


label = tk.Label(frame, text="Enter Task:",fg="purple4",font=('arial',10,'bold'))
label.grid(row=0, column=0, padx=5)

entry = tk.Entry(frame, width=30,fg='purple4',background='gray80',font=('arial',8,'bold'),bd=3)
entry.grid(row=0, column=1, padx=5)

add_button = tk.Button(frame, text="Add Task",
                        command=add_task,fg="white",background="purple4",bd=2)
add_button.grid(row=0, column=2, padx=5)

remove_button = tk.Button(frame, text="Remove Task",
                           command=remove_task,fg="white",background="purple4",bd=2)
remove_button.grid(row=0, column=3, padx=5)

task_list = tk.Listbox(app, selectmode=tk.SINGLE
                       ,width=40,fg="purple4",background="gray80"
                       ,highlightcolor="purple4",font=('arial',11,'bold'),bd=3)
task_list.pack(padx=10, pady=5)

view_task()
update_task_list()

app.mainloop()