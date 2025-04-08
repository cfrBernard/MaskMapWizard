import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinterdnd2 import DND_FILES, TkinterDnD
from logic.maskmap_builder import build_mask_map
from PIL import Image, ImageOps
import os

class MainWindow(TkinterDnD.Tk):
    def __init__(self):
        super().__init__()
        self.title("Mask Map Wizard")
        self.geometry("560x200")

        self.drop_labels = []

        self.create_ui()
    
    def create_ui(self):
        # Create rows for different map types (Metallic, AO, Detail, Smooth)
        self.create_row("MetallicMap", 0)
        self.create_row("AOMap", 1)
        self.create_row("DetailMap", 2)
        self.create_row("SmoothMap", 3)

        # Separator
        separator = tk.Frame(self, height=2, bd=1, relief="sunken")
        separator.grid(row=4, column=0, columnspan=3, pady=5, sticky="ew")

        # Export path button
        self.path_button = tk.Button(self, text="Export Path", command=self.choose_build_path, font=("Arial", 9), height=1, width=15)
        self.path_button.grid(row=5, column=0, padx=10, pady=5, sticky="nsew")

        # Build button
        self.build_button = tk.Button(self, text="Build", command=self.on_build_click, font=("Arial", 10, "bold"), height=2, width=15)
        self.build_button.grid(row=5, column=1, padx=10, pady=5, sticky="nsew")

        # Reset button
        reset_button = tk.Button(self, text="Reset", command=self.reset_all, font=("Arial", 9), height=1, width=5)
        reset_button.grid(row=5, column=2, padx=10, pady=5, sticky="nsew")

        # Grid configuration
        for i in range(6):
            self.grid_rowconfigure(i, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=3)
        self.grid_columnconfigure(2, weight=1)

    def create_row(self, label_text, row_number):
        # Create label and drag-and-drop area for each map type
        label = tk.Label(self, text=label_text, font=("Arial", 10, "bold"))
        label.grid(row=row_number, column=0, padx=10, pady=5, sticky="nsew")

        drop_label = tk.Label(self, text="Drop here", relief="solid", bd=1, width=50, height=2, bg="#f0f0f0", font=("Arial", 9))
        drop_label.grid(row=row_number, column=1, padx=10, pady=5, sticky="nsew")

        drop_label.drop_target_register(DND_FILES)
        drop_label.dnd_bind('<<Drop>>', lambda e, l=drop_label: l.config(text=e.data))

        button = tk.Button(self, text="...", command=lambda: self.open_file_dialog(drop_label), font=("Arial", 10, "bold"), height=1, width=3)
        button.grid(row=row_number, column=2, padx=10, pady=5, sticky="nsew")

        self.drop_labels.append(drop_label)

    def open_file_dialog(self, label):
        # Open a file dialog to select a file
        file_path = filedialog.askopenfilename(title="Select a file")
        if file_path:
            label.config(text=file_path)

    def reset_all(self):
        # Reset the UI (clear the paths and reset buttons)
        for label in self.drop_labels:
            label.config(text="Drop here")
        self.path_button.config(text="Export Path")

    def choose_build_path(self):
        # Choose a directory for export
        path = filedialog.askdirectory(title="Select an export directory")
        if path:
            self.path_button.config(text=path)
    
    def ask_if_roughness(self):
        result = messagebox.askyesno(
            "Roughness", 
            "Is the 'Smooth' map actually a Roughness map? (Yes = Roughness, No = Smooth)"
        )
        return result
    
    def invert_image(self, image_path):
        # Invert the colors of the image
        img = Image.open(image_path)
        inverted_img = ImageOps.invert(img.convert("RGB"))
        inverted_image_path = image_path.replace(".png", "_inverted.png")
        inverted_img.save(inverted_image_path)
        print(f"Inverted image saved as: {inverted_image_path}")
        return inverted_image_path
    
    def on_build_click(self):
        # Collect file paths for each map type
        input_paths = {}
        keys = ["Metallic", "AO", "Detail", "Smooth"]
    
        for key, label in zip(keys, self.drop_labels):
            path = label.cget("text")
            input_paths[key] = path if os.path.exists(path) else None
    
        # Ask for confirmation if "Smooth" map is actually "Roughness"
        if input_paths["Smooth"]:
            is_rough = self.ask_if_roughness()
            if is_rough:
                print("Inverting colors of the Smooth map (Roughness).")
                # Invert the color of the Smooth map here before proceeding
                input_paths["Smooth"] = self.invert_image(input_paths["Smooth"])
    
        # Get the export path
        export_dir = self.path_button.cget("text")
        if not os.path.isdir(export_dir):
            print("⚠️ Invalid export path.")
            return
    
        output_file = os.path.join(export_dir, "MaskMap.png")
    
        # Check if the file already exists and generate a unique name
        output_file = self.get_unique_filename(output_file)
    
        try:
            result = build_mask_map(input_paths, output_file)
            if result:
                messagebox.showinfo("Success", f"MaskMap successfully generated!\n{result}")
        except Exception as e:
            print("Error during build:", e)
            messagebox.showerror("Error", f"An error occurred: {e}")

    def get_unique_filename(self, output_file):
        """
        Check if the file already exists, and if so, add a suffix _x
        to avoid overwriting it.
        """
        if not os.path.exists(output_file):
            return output_file
        
        base, ext = os.path.splitext(output_file)
        counter = 1
        new_output_file = f"{base}_{counter}{ext}"
        
        # Search for a unique name by incrementing the counter
        while os.path.exists(new_output_file):
            counter += 1
            new_output_file = f"{base}_{counter}{ext}"
        
        print(f"File already exists. New file: {new_output_file}")
        return new_output_file