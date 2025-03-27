import tkinter as tk
from tkinter import messafebox
from datetime import datetime

class AttendanceApp:
    def __init__(self, w):
        self.w = w
        self.w.title('출석부')
        self.stu_list = []
        self.create_widgets()
    def create_widgets(self):
        self.label= tk.Label(self.w, text='학생이름')
        self.label.pack(pady=10)
        self.entry= tk.Entry(self.w)