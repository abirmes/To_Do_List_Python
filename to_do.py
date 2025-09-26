import tkinter as tk
from tkinter import ttk
from sql import *


class TodoList(tk.Tk):
    task_listbox = []
    def __init__(self, screenName = None, baseName = None, className = "Tk", useTk = True, sync = False, use = None):
        super().__init__(screenName, baseName, className, useTk, sync, use)
        self.geometry("750x500")

        self.title("To do list")
        self.create_widgets()
        
    def create_widgets(self):
        
        self.task_subject_label = tk.Label(self, text="Add Task:")
        self.task_subject_label.grid(row=0 , column=0 , padx=3)
        
        self.task_subject_label = tk.Label(self, text="Task Subject:")
        self.task_subject_label.grid(row=0 , column=1 , padx=3)
        self.task_subject_input = tk.Entry(self, width=30)
        self.task_subject_input.grid(row=1 , column=1 , padx=3)
        
        self.task_description_label = tk.Label(self, text="Task description:")
        self.task_description_label.grid(row=0 , column=2 , padx=3)
        self.task_description_input = tk.Entry(self, width=30)
        self.task_description_input.grid(row=1 , column=2 , padx=3)
        
        
        
        self.task_priority_label = tk.Label(self, text="Task priority:")
        self.task_priority_label.grid(row=0 , column=3 , padx=3)
        
        options = ["very important", "important", "casual"]
        self.combobox = ttk.Combobox(self, values=options)
        self.combobox.set("Select priority") 
        self.combobox.grid(row=1 , column=3 , padx=3)

        
        self.add_task_button = tk.Button(self , text="ajouter tache" , command=self.add_task)
        self.add_task_button.grid(row=1 , column=4 , padx=3)
        
        self.display_tasks_button = tk.Button(self , text=" to do" , command=self.display_todo_tasks)
        self.display_tasks_button.grid(row=2 , column=1 , padx=3)
        
        self.tasks_listbox_todo = tk.Listbox(self , selectmode=tk.SINGLE )
        self.tasks_listbox_todo.grid(row=3 , column=1 , padx=3  , pady=10)
        
        
        self.display_tasks_button = tk.Button(self , text="doing" , command=self.display_doing_tasks)
        self.display_tasks_button.grid(row=2 , column=2 , padx=3)
        
        self.tasks_listbox_doing = tk.Listbox(self , selectmode=tk.SINGLE )
        self.tasks_listbox_doing.grid(row=3 , column=2 , padx=3  , pady=10)
        
        
        self.display_tasks_button = tk.Button(self , text="done" , command=self.display_done_tasks)
        self.display_tasks_button.grid(row=2 , column=3 , padx=3)
        
        self.tasks_listbox_done = tk.Listbox(self , selectmode=tk.SINGLE )
        self.tasks_listbox_done.grid(row=3 , column=3 , padx=3  , pady=10)
        
        options_status = ["to do", "doing", "done"]
        self.status_combobox = ttk.Combobox(self, values=options_status)
        self.status_combobox.set("Select new Status")
        self.status_combobox.grid(row=4, column=1, padx=3)
        
        self.button_frame = tk.Frame(self)
        self.button_frame.grid(row=4 , column=2 , padx=3)
        
        self.edit_task_button = tk.Button(self.button_frame , text="modifier" , command=self.modifier)
        self.edit_task_button.grid(row=4 , column=2 , padx=3)
        
        
        self.delete_task_button = tk.Button(self.button_frame , text="delete" , command=self.delete)
        self.delete_task_button.grid(row=4 , column=3 , padx=3)
        
        
        
     

        
        
    def add_task(self):
        subject = self.task_subject_input.get()
        description = self.task_description_input.get()
        priority = self.combobox.get()
        if subject and description and priority:
            ajouter_task(subject , description , priority)
            self.task_subject_input.delete(0 , tk.END)
            self.task_description_input.delete(0 , tk.END)
            self.combobox.delete(0 , tk.END)
            self.display_todo_tasks()
            self.display_doing_tasks()
            self.display_done_tasks()
            
    def display_todo_tasks(self):
        self.tasks_listbox_todo.delete(0, tk.END)
        self.task_data = afficher_tasks()  
        for task in self.task_data:
            if task['status'] == "to do":
                display_text = f"{task['id']} - {task['subject']} ({task['priority']})"
                self.tasks_listbox_todo.insert(tk.END, display_text)
    
    def display_doing_tasks(self):
        self.tasks_listbox_doing.delete(0, tk.END)
        self.task_data = afficher_tasks()  
        for task in self.task_data:
            if task['status'] == "doing":
                display_text = f"{task['id']} - {task['subject']} ({task['priority']})"
                self.tasks_listbox_doing.insert(tk.END, display_text)
                
    def display_done_tasks(self):
        self.tasks_listbox_done.delete(0, tk.END)
        self.task_data = afficher_tasks()  
        for task in self.task_data:
            if task['status'] == "done":
                display_text = f"{task['id']} - {task['subject']} ({task['priority']})"
                self.tasks_listbox_done.insert(tk.END, display_text)


    
    
            
   
                
    def delete_task(self):
        task_index = self.tasks_listbox.curselection()
        if task_index:
            self.tasks_listbox.delete(task_index)
   
   
   
   
    def get_id(self):
        if self.tasks_listbox_todo.curselection():
            
            selected_index = self.tasks_listbox_todo.curselection()
        elif self.tasks_listbox_doing.curselection():
            selected_index = self.tasks_listbox_doing.curselection()
        elif self.tasks_listbox_done.curselection():
            selected_index = self.tasks_listbox_done.curselection()
        else:
            print("selectionner")
        if selected_index:
            task = self.task_data[selected_index[0]]
            task_id = task['id']
            return task_id
        
    def modifier(self):
        task_id = self.get_id()
        new_status = self.status_combobox.get()
        modifier_statut_task(task_id, new_status)
        self.status_combobox.set("Select new Status")
        self.display_todo_tasks()
        self.display_doing_tasks()
        self.display_done_tasks()

        
        
    def delete(self):
        task = self.get_id()
        supprimer_task(task)
        self.display_todo_tasks()
        self.display_doing_tasks()
        self.display_done_tasks()
            
            
       
