# interface.py
import customtkinter as ctk
from tkinter import filedialog, messagebox, PhotoImage
from aiml_generator import generate_questions_and_answers_with_aiml
from cv_reader import read_cv
from tkinterdnd2 import TkinterDnD, DND_FILES
import pyperclip
import random

class CVInterviewApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CV Interview App")
        self.root.attributes('-fullscreen', True)  # Make the window fullscreen

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.frame = ctk.CTkFrame(self.root)
        self.frame.pack(pady=20, padx=20, fill="both", expand=True)

        self.canvas = ctk.CTkCanvas(self.frame, width=200, height=200, bg="gray20", highlightthickness=0)
        self.canvas.pack(pady=20)

        self.upload_icon = PhotoImage(file="stat.png")
        self.canvas.create_image(100, 100, image=self.upload_icon)
        self.canvas.create_text(100, 160, text="Drag & Drop To Upload File\nOr Click Here", fill="white", font=('Helvetica', 10, 'bold'))
        self.canvas.bind("<Button-1>", self.browse_files)
        self.canvas.drop_target_register(DND_FILES)
        self.canvas.dnd_bind('<<Drop>>', self.drop_file)

        # Load the copy.png image
        self.copy_icon = PhotoImage(file="copy.png")

        # Initialize frame
        self.init_frames()

        # Variables to store previously generated questions
        self.previous_questions = set()

    def init_frames(self):
        # Initial questions frame
        self.initial_frame = ctk.CTkFrame(self.frame)
        self.initial_frame.pack(pady=20, fill="both", expand=True)

        self.lol_image = PhotoImage(file="lol.png")
        self.image_label = ctk.CTkLabel(self.initial_frame, image=self.lol_image)
        self.image_label.pack(side=ctk.LEFT, padx=10)

        self.initial_output_text = self.create_text_area(self.initial_frame)
        self.initial_output_text.pack(side=ctk.LEFT, padx=10, expand=True, fill="both")

        self.initial_buttons_frame = ctk.CTkFrame(self.initial_frame)
        self.initial_buttons_frame.pack(pady=10, fill="x")

        self.copy_initial_button = ctk.CTkButton(self.initial_buttons_frame, image=self.copy_icon, command=self.copy_initial_text, width=40, height=40, text="")
        self.copy_initial_button.pack(side=ctk.LEFT, padx=10)

        # More questions frame
        self.more_frame = ctk.CTkFrame(self.frame)
        self.more_frame.pack(pady=20, fill="both", expand=True)

        self.generate_more_frame = ctk.CTkFrame(self.more_frame)
        self.generate_more_frame.pack(anchor="e", padx=10, pady=5)

        self.generate_more_button = ctk.CTkButton(self.generate_more_frame, text="Generate more questions", command=self.generate_more_questions, state=ctk.DISABLED, width=200, height=40)
        self.generate_more_button.pack(side=ctk.LEFT, padx=10)

        self.user_image = PhotoImage(file="user.png")
        self.user_image_label = ctk.CTkLabel(self.generate_more_frame, image=self.user_image)
        self.user_image_label.pack(side=ctk.LEFT, padx=10)

        self.more_output_frame = ctk.CTkFrame(self.more_frame)
        self.more_output_frame.pack(fill="both", expand=True)

        self.lol_image_more = PhotoImage(file="lol.png")
        self.image_label_more = ctk.CTkLabel(self.more_output_frame, image=self.lol_image_more)
        self.image_label_more.pack(side=ctk.LEFT, padx=10)

        self.more_output_text = self.create_text_area(self.more_output_frame)
        self.more_output_text.pack(side=ctk.LEFT, expand=True, fill="both")

        self.more_buttons_frame = ctk.CTkFrame(self.more_output_frame)
        self.more_buttons_frame.pack(pady=10, fill="x")

        self.copy_more_button = ctk.CTkButton(self.more_buttons_frame, image=self.copy_icon, command=self.copy_more_text, width=40, height=40, text="")
        self.copy_more_button.pack(side=ctk.LEFT, padx=10)

        # Custom request frame
        self.custom_frame = ctk.CTkFrame(self.frame)
        self.custom_frame.pack(pady=20, fill="both", expand=True)

        self.custom_request_frame = ctk.CTkFrame(self.custom_frame)
        self.custom_request_frame.pack(pady=10, fill="both", expand=True)

        self.custom_request_entry = ctk.CTkEntry(self.custom_request_frame, width=400)
        self.custom_request_entry.pack(side=ctk.LEFT, padx=10, expand=True, fill="both")

        self.custom_request_button_frame = ctk.CTkFrame(self.custom_request_frame)
        self.custom_request_button_frame.pack(side=ctk.LEFT, padx=10)

        self.custom_request_button = ctk.CTkButton(self.custom_request_button_frame, text="Personalize your request", command=self.custom_request, width=200, height=40)
        self.custom_request_button.pack(side=ctk.LEFT)

        self.user_image_custom = PhotoImage(file="user.png")
        self.user_image_label_custom = ctk.CTkLabel(self.custom_request_button_frame, image=self.user_image_custom)
        self.user_image_label_custom.pack(side=ctk.LEFT, padx=10)

        self.custom_output_frame = ctk.CTkFrame(self.custom_frame)
        self.custom_output_frame.pack(fill="both", expand=True)

        self.lol_image_custom = PhotoImage(file="lol.png")
        self.image_label_custom = ctk.CTkLabel(self.custom_output_frame, image=self.lol_image_custom)
        self.image_label_custom.pack(side=ctk.LEFT, padx=10)

        self.custom_output_text = self.create_text_area(self.custom_output_frame)
        self.custom_output_text.pack(side=ctk.LEFT, expand=True, fill="both")

        self.custom_buttons_frame = ctk.CTkFrame(self.custom_output_frame)
        self.custom_buttons_frame.pack(pady=10, fill="x")

        self.copy_custom_button = ctk.CTkButton(self.custom_buttons_frame, image=self.copy_icon, command=self.copy_custom_text, width=40, height=40, text="")
        self.copy_custom_button.pack(side=ctk.LEFT, padx=10)

    def create_text_area(self, parent_frame):
        return ctk.CTkTextbox(parent_frame, height=10, width=60, wrap="word", state=ctk.DISABLED)

    def browse_files(self, event=None):
        file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        if file_path:
            self.process_file(file_path)

    def drop_file(self, event):
        file_path = event.data.strip('{}')
        if file_path.endswith(".pdf"):
            self.process_file(file_path)
        else:
            messagebox.showerror("Invalid file", "Please upload a PDF file.")

    def process_file(self, file_path):
        cv_text = read_cv(file_path)
        self.display_questions_and_answers(cv_text)
        self.generate_more_button.configure(state=ctk.NORMAL)

    def display_questions_and_answers(self, cv_text):
        questions_and_answers = generate_questions_and_answers_with_aiml(cv_text)
        self.set_text_area_content(self.initial_output_text, questions_and_answers)

    def generate_more_questions(self):
        cv_text = self.initial_output_text.get(1.0, ctk.END)
        variation = random.choice(["variation1", "variation2", "variation3"])
        questions_and_answers = generate_questions_and_answers_with_aiml(cv_text, variation)
        self.set_text_area_content(self.more_output_text, questions_and_answers)

    def custom_request(self):
        user_request = self.custom_request_entry.get()
        cv_text = self.initial_output_text.get(1.0, ctk.END)
        questions_and_answers = generate_questions_and_answers_with_aiml(cv_text, user_request)
        self.set_text_area_content(self.custom_output_text, questions_and_answers)

    def set_text_area_content(self, text_area, content):
        text_area.configure(state=ctk.NORMAL)
        text_area.delete(1.0, ctk.END)
        text_area.insert(ctk.END, content)
        text_area.configure(state=ctk.DISABLED)
        self.adjust_text_area_height(text_area)

    def copy_initial_text(self):
        pyperclip.copy(self.initial_output_text.get(1.0, ctk.END))

    def copy_more_text(self):
        pyperclip.copy(self.more_output_text.get(1.0, ctk.END))

    def copy_custom_text(self):
        pyperclip.copy(self.custom_output_text.get(1.0, ctk.END))

    def adjust_text_area_height(self, text_area):
        text_area.update_idletasks()
        text_area.configure(height=int(text_area.index(ctk.END).split('.')[0]))

if __name__ == "__main__":
    root = TkinterDnD.Tk()
    root.attributes('-topmost', True)  # Keep the window on top
    root.after(0, lambda: root.attributes('-topmost', False))  # Allow other windows to be on top later
    app = CVInterviewApp(root)
    root.mainloop()
