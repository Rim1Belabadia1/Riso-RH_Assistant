import customtkinter as ctk
from tkinter import PhotoImage
import subprocess

class StartPageApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Starting Page")
        self.root.geometry("800x600")

        ctk.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
        ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

        # Set the background image
        self.background_image = PhotoImage(file="toph.PNG")
        self.background_label = ctk.CTkLabel(self.root, image=self.background_image)
        self.background_label.place(relwidth=1, relheight=1)

        # Create the smaller oval button at the bottom with transparent effect
        self.start_button = ctk.CTkButton(
            self.root, text="Let's Start", 
            width=40, height=40, 
            fg_color=None, corner_radius=50, 
            text_color="white", font=('Helvetica', 16, 'bold'),
            command=self.start_app,
            hover_color=None
        )
        self.start_button.place(relx=0.5, rely=0.9, anchor="center")

    def start_app(self):
        print("Let's Start button clicked")
        subprocess.Popen(["python", "interface.py"])
        self.root.destroy()

if __name__ == "__main__":
    root = ctk.CTk()
    app = StartPageApp(root)
    root.mainloop()