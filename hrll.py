import tkinter as tk
from tkinter import messagebox

class HomeSecurityApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Home Security Automation Project Interface")
        
        # Colors
        self.primary_color = "#4a90e2"
        self.secondary_color = "#50e3c2"
        self.button_color = "#f5a623"
        self.background_color = "#f4f4f4"
        
        # Fonts
        self.font_large = ('Arial', 16)
        self.font_medium = ('Arial', 14)
        
        self.root.configure(bg=self.background_color)

        # Login Frame
        self.login_frame = tk.Frame(root, bg=self.background_color)
        self.login_frame.pack(padx=10, pady=10, fill='both', expand=True)
        
        tk.Label(self.login_frame, text="Username", bg=self.background_color, font=self.font_medium).grid(row=0, column=0, padx=10, pady=10, sticky='e')
        self.username_entry = tk.Entry(self.login_frame, font=self.font_medium)
        self.username_entry.grid(row=0, column=1, padx=10, pady=10, sticky='w')
        
        tk.Label(self.login_frame, text="Password", bg=self.background_color, font=self.font_medium).grid(row=1, column=0, padx=10, pady=10, sticky='e')
        self.password_entry = tk.Entry(self.login_frame, show='*', font=self.font_medium)
        self.password_entry.grid(row=1, column=1, padx=10, pady=10, sticky='w')
        
        self.login_button = tk.Button(self.login_frame, text="Login", command=self.login, bg=self.button_color, fg="white", font=self.font_medium)
        self.login_button.grid(row=2, columnspan=2, pady=20, sticky='ew')
        
        self.register_button = tk.Button(self.login_frame, text="Register", command=self.register, bg=self.button_color, fg="white", font=self.font_medium)
        self.register_button.grid(row=3, columnspan=2, pady=20, sticky='ew')
    
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        # Dummy check for demonstration
        if username == "admin" and password == "admin":
            self.open_admin_home()
        elif username == "user" and password == "user":
            self.open_user_home()
        else:
            messagebox.showerror("Login Error", "Invalid username or password")
    
    def register(self):
        # Placeholder for registration logic
        messagebox.showinfo("Register", "Registration functionality not implemented")
    
    def open_user_home(self):
        self.login_frame.pack_forget()
        self.user_home_frame = tk.Frame(self.root, bg=self.background_color)
        self.user_home_frame.pack(side="right", fill='both', expand=True)
        
        # Sidebar Frame
        self.sidebar_frame = tk.Frame(self.root, bg=self.primary_color, width=250)
        self.sidebar_frame.pack(side="left", fill='y')
        
        tk.Button(self.sidebar_frame, text="Stream Video", command=self.stream_video, bg=self.button_color, fg="white", font=self.font_large).pack(pady=15, padx=10, fill='x')
        tk.Button(self.sidebar_frame, text="View Profile", command=self.view_profile, bg=self.button_color, fg="white", font=self.font_large).pack(pady=15, padx=10, fill='x')
        tk.Button(self.sidebar_frame, text="Edit Profile", command=self.edit_profile, bg=self.button_color, fg="white", font=self.font_large).pack(pady=15, padx=10, fill='x')
        tk.Button(self.sidebar_frame, text="IOT Detector", command=self.iot_detector, bg=self.button_color, fg="white", font=self.font_large).pack(pady=15, padx=10, fill='x')

    def open_admin_home(self):
        self.login_frame.pack_forget()
        self.admin_home_frame = tk.Frame(self.root, bg=self.background_color)
        self.admin_home_frame.pack(side="right", fill='both', expand=True)
        
        # Sidebar Frame
        self.sidebar_frame = tk.Frame(self.root, bg=self.primary_color, width=250)
        self.sidebar_frame.pack(side="left", fill='y')

        tk.Button(self.sidebar_frame, text="Stream Video", command=self.stream_video, bg=self.button_color, fg="white", font=self.font_large).pack(pady=15, padx=10, fill='x')
        tk.Button(self.sidebar_frame, text="View Profile", command=self.view_profile, bg=self.button_color, fg="white", font=self.font_large).pack(pady=15, padx=10, fill='x')
        tk.Button(self.sidebar_frame, text="List Suspects", command=self.list_suspects, bg=self.button_color, fg="white", font=self.font_large).pack(pady=15, padx=10, fill='x')
        tk.Button(self.sidebar_frame, text="Register Suspects", command=self.register_suspects, bg=self.button_color, fg="white", font=self.font_large).pack(pady=15, padx=10, fill='x')
    
    def stream_video(self):
        # Placeholder for streaming video functionality
        messagebox.showinfo("Stream Video", "Streaming video functionality not implemented")
    
    def view_profile(self):
        # Placeholder for viewing profile functionality
        messagebox.showinfo("View Profile", "View Profile functionality not implemented")
    
    def edit_profile(self):
        # Placeholder for editing profile functionality
        messagebox.showinfo("Edit Profile", "Edit Profile functionality not implemented")
    
    def iot_detector(self):
        # Placeholder for IOT detector functionality
        messagebox.showinfo("IOT Detector", "IOT Detector functionality not implemented")
    
    def list_suspects(self):
        # Placeholder for listing suspects functionality
        messagebox.showinfo("List Suspects", "List Suspects functionality not implemented")
    
    def register_suspects(self):
        # Placeholder for registering suspects functionality
        messagebox.showinfo("Register Suspects", "Register Suspects functionality not implemented")

# Main execution
if __name__ == "__main__":
    root = tk.Tk()
    app = HomeSecurityApp(root)
    root.mainloop()