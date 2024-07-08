import pyautogui
import os
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog

class ScreenshotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Screenshot App")
        self.save_path = "screenshots"
        os.makedirs(self.save_path, exist_ok=True)
        self.count = 0

        # Configure the root window
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        self.root.configure(bg="#f5f5f5")

        # Bind shortcut
        self.root.bind('<Control-c>', self.take_screenshot_shortcut)

        # Main frame
        self.main_frame = ttk.Frame(root, padding="10 10 10 10")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Title
        self.title_label = ttk.Label(self.main_frame, text="Screenshot App", font=("Helvetica", 18, "bold"))
        self.title_label.pack(pady=10)

        # Preview current screenshot
        self.preview_label = ttk.Label(self.main_frame, text="No screenshot taken yet")
        self.preview_label.pack(pady=10)

        # Contador de capturas tomadas
        self.counter_label = ttk.Label(self.main_frame, text="Screenshots taken: 0")
        self.counter_label.pack(pady=10)

        # Buttons frame
        self.buttons_frame = ttk.Frame(self.main_frame)
        self.buttons_frame.pack(pady=10)

        self.capture_button = ttk.Button(self.buttons_frame, text="Take Screenshot", command=self.take_screenshot)
        self.capture_button.grid(row=0, column=0, padx=5)

        self.save_button = ttk.Button(self.buttons_frame, text="Save to PDF", command=self.create_pdf_from_screenshots)
        self.save_button.grid(row=0, column=1, padx=5)

        self.reset_button = ttk.Button(self.buttons_frame, text="Reset Captures", command=self.reset_captures)
        self.reset_button.grid(row=0, column=2, padx=5)

        # Scrollable frame for preview list
        self.scroll_frame = ttk.LabelFrame(self.main_frame, text="Previous Screenshots")
        self.scroll_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.canvas = tk.Canvas(self.scroll_frame, bg="#ffffff")
        self.scrollbar = ttk.Scrollbar(self.scroll_frame, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas, bg="#ffffff")

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill=tk.BOTH, expand=True)
        self.scrollbar.pack(side="right", fill="y")

        self.image_labels = []

    def take_screenshot(self):
        screen_width, screen_height = pyautogui.size()  # Get the size of the primary monitor
        screenshot = pyautogui.screenshot(region=(0, 0, screen_width, screen_height))
        screenshot_path = os.path.join(self.save_path, f"screenshot_{self.count}.png")
        screenshot.save(screenshot_path)
        self.count += 1

        # Update current preview
        img = Image.open(screenshot_path)
        img.thumbnail((400, 300))
        img = ImageTk.PhotoImage(img)
        self.preview_label.config(image=img, text="")
        self.preview_label.image = img

        # Add to scrollable preview list
        self.add_to_preview_list(screenshot_path)

        # Actualizar contador de capturas tomadas
        self.counter_label.config(text=f"Screenshots taken: {self.count}")

    def take_screenshot_shortcut(self, event):
        self.take_screenshot()

    def add_to_preview_list(self, image_path):
        img = Image.open(image_path)
        img.thumbnail((200, 150))
        img = ImageTk.PhotoImage(img)
        label = tk.Label(self.scrollable_frame, image=img, bg="#ffffff")
        label.image = img

        row = len(self.image_labels) // 3
        column = len(self.image_labels) % 3
        label.grid(row=row, column=column, padx=5, pady=5)
        
        self.image_labels.append(label)

    def create_pdf_from_screenshots(self):
        image_files = [os.path.join(self.save_path, file) for file in os.listdir(self.save_path) if file.endswith(".png")]
        image_files.sort(key=lambda x: int(os.path.splitext(os.path.basename(x))[0].split('_')[1]))  # Ensure correct order

        if not image_files:
            messagebox.showerror("Error", "No screenshots found to create a PDF.")
            return

        # Open the first image and convert to RGB
        first_image = Image.open(image_files[0]).convert("RGB")
        
        # Convert the rest of the images to RGB and append
        images = [Image.open(image).convert("RGB") for image in image_files[1:]]

        output_pdf_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        if output_pdf_path:
            first_image.save(output_pdf_path, save_all=True, append_images=images)
            messagebox.showinfo("Success", f"All screenshots have been saved to {output_pdf_path}")

    def reset_captures(self):
        for label in self.image_labels:
            label.destroy()
        self.image_labels.clear()
        self.count = 0

        for file in os.listdir(self.save_path):
            file_path = os.path.join(self.save_path, file)
            if os.path.isfile(file_path) and file.endswith(".png"):
                os.unlink(file_path)

        self.preview_label.config(image="", text="No screenshot taken yet")

        # Resetear el contador de capturas tomadas
        self.counter_label.config(text="Screenshots taken: 0")
        messagebox.showinfo("Reset", "All screenshots have been reset.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ScreenshotApp(root)
    root.mainloop()
