import os
from tkinter import messagebox
from MaskMapWizard.core.maskmap_builder import build_mask_map

def on_build_click(self):
    # Collect file paths for each map type
    input_paths = {}
    keys = ["Metallic", "AO", "Detail", "Smooth"]

    for key, label in zip(keys, self.drop_labels):
        path = self.clean_path(label.cget("text"))
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
