import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image
from pillow_heif import open_heif

def convert_heic_to_jpeg(input_path, output_path, progress, step):
    heif_file = open_heif(input_path)
    image = Image.frombytes(heif_file.mode, heif_file.size, heif_file.data)
    image.save(output_path, "JPEG")
    progress.step(step)

def start_conversion():
    file_paths = filedialog.askopenfilenames(filetypes=[("HEIC files", "*.heic")])
    if not file_paths:
        return
    
    output_dir = filedialog.askdirectory(title="Select Output Folder")
    if not output_dir:
        return
    
    progress_bar["maximum"] = len(file_paths)
    progress_bar["value"] = 0
    step = 100 / len(file_paths)
    
    for file_path in file_paths:
        filename = os.path.splitext(os.path.basename(file_path))[0] + ".jpg"
        output_path = os.path.join(output_dir, filename)
        convert_heic_to_jpeg(file_path, output_path, progress_bar, step)
    
    messagebox.showinfo("Conversion Complete", "All files have been converted successfully!")

def create_gui():
    global progress_bar
    root = tk.Tk()
    root.title("HEIC to JPEG Converter")
    root.geometry("400x200")
    
    frame = tk.Frame(root, padx=10, pady=10)
    frame.pack(expand=True)
    
    upload_button = tk.Button(frame, text="Upload HEIC Files", command=start_conversion)
    upload_button.pack(pady=10)
    
    progress_bar = ttk.Progressbar(frame, length=300, mode="determinate")
    progress_bar.pack(pady=10)
    
    root.mainloop()

create_gui()
