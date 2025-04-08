from ui.main_window import MainWindow
from logic.maskmap_builder import build_mask_map
from version import __version__
import os

if __name__ == "__main__":
    # Initialize and run the main window application
    app = MainWindow()
    app.mainloop()

def on_build_click(self):
    # Collect file paths for each map type
    input_paths = {}
    keys = ["Metallic", "AO", "Detail", "Smooth"]

    for key, label in zip(keys, self.drop_labels):
        path = label.cget("text")
        input_paths[key] = path if os.path.exists(path) else None

    # Get the export directory path
    export_dir = self.path_button.cget("text")
    if not os.path.isdir(export_dir):
        print("⚠️ Invalid export path.")
        return

    # Set the output file path
    output_file = os.path.join(export_dir, "MaskMap.png")
    
    try:
        # Attempt to build the mask map
        build_mask_map(input_paths, output_file)
    except Exception as e:
        print("Error during build:", e)
