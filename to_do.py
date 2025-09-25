import tkinter as tk
from tkinter import ttk
import sql
from sql import *


class TodoList(tk.Tk):
    task_listbox = []
    def __init__(self, screenName = None, baseName = None, className = "Tk", useTk = True, sync = False, use = None):
        super().__init__(screenName, baseName, className, useTk, sync, use)
        self.geometry("600x600")
        self.title("To do list")
        self.create_widgets()
        
    def create_widgets(self):
        
        self.task_subject_label = tk.Label(self, text="Task Subject:")
        self.task_subject_label.pack()
        self.task_subject_input = tk.Entry(self, width=30)
        self.task_subject_input.pack(pady=10)
        
        self.task_description_label = tk.Label(self, text="Task description:")
        self.task_description_label.pack()
        self.task_description_input = tk.Entry(self, width=30)
        self.task_description_input.pack(pady=10)
        
        
        
        self.task_priority_label = tk.Label(self, text="Task priority:")
        self.task_priority_label.pack()
        options = ["very important", "important", "casual"]
        self.combobox = ttk.Combobox(self, values=options)
        self.combobox.set("Select priority") # Set a default placeholder text
        self.combobox.pack(pady=10)

        
      
        
        
        
        
        self.add_task_button = tk.Button(self , text="ajouter tache" , command=self.add_task)
        self.add_task_button.pack(pady=5)
        
        self.tasks_listbox = tk.Listbox(self , selectmode=tk.SINGLE )
        self.tasks_listbox.pack(pady=5)
        
        self.button_frame = tk.Frame(self)
        self.button_frame.pack(padx=5)
        
        self.edit_task_button = tk.Button(self.button_frame , text="modifier" , command=self.edit_task)
        self.edit_task_button.grid(row=0 , column=0 , padx=5)
        
        
     

        
        
    def add_task(self):
        subject = self.task_subject_input.get()
        description = self.task_description_input.get()
        priority = self.combobox.get()
        print(priority , description , subject)
        if subject and description and priority:
            ajouter_task(subject , description , priority)
            self.task_subject_input.delete(0 , tk.END)
            self.task_description_input.delete(0 , tk.END)
            self.combobox.delete(0 , tk.END)
            
            
      
        
            
            
    def edit_task(self):
        task_index = self.tasks_listbox.curselection()
        if task_index:
            new_task = self.task_input.get()
            if new_task:
                self.tasks_listbox.delete(task_index)
                self.tasks_listbox.insert(task_index , new_task)
                self.task_input.delete(0 , tk.END)
                
                
    def delete_task(self):
        task_index = self.tasks_listbox.curselection()
        if task_index:
            self.tasks_listbox.delete(task_index)
            
    