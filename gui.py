import tkinter as tk
from tkinter import messagebox
from main import shorten_link
import validators
import pyperclip

class GUI:
    """This is a class for the interface for a link shortener"""
    def __init__(self):
        self.window = tk.Tk()
        # Window Configuration
        self.window.geometry("700x250")
        self.window.title("Link Shortener")
        self.window.resizable(False, False)

        # Title Label
        self.title_label = tk.Label(self.window, text="Enter the link to shorten:", font=("Helvetica", 14))
        self.title_label.pack(pady=20)

        # Textbox Configuration
        self.textbox = tk.Entry(self.window, width=50)
        self.textbox.pack(padx=20, pady=10)

        # Button Configuration
        # self.button = tk.Button(self.window, text="Shorten Link")
        self.button = tk.Button(self.window, text="Shorten Link", command=self.shorten_link)
        self.button.pack(pady=10)
        
        
        
        # Add a label to display the shortened link
        self.label = tk.Label(self.window, text="", font=("Helvetica", 12), fg="blue")
        self.label.pack(pady=10)
        
        # Add a button to copy the shortened link
        # self.copy_button = tk.Button(self.window, text="Copy to Clipboard")
        self.copy_button = tk.Button(self.window, text="Copy to Clipboard", command=self.copy_to_clipboard, state=tk.DISABLED)
        self.copy_button.pack(pady=10)
        

        
        self.window.mainloop()
    
    def shorten_link(self):
        link = self.textbox.get().strip()
        if not validators.url(link):
            messagebox.showerror("Invalid URL", "Please enter a valid URL.")
            return
        s_link = shorten_link(link)
        self.label.config(text=s_link)
        self.copy_button.config(state=tk.NORMAL)

    def copy_to_clipboard(self):
        s_link = self.label.cget("text")
        pyperclip.copy(s_link)
        messagebox.showinfo("Copied", "Shortened link copied to clipboard!")

if __name__ == "__main__":
    GUI()
