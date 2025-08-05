from PIL import Image
import os

def build_mask_map(inputs, output_path):
    """
    inputs: dict with keys ["Metallic", "AO", "Detail", "Smooth"]
            and paths to the images (or None)
    output_path: full path to the output file (e.g., "C:/export/MaskMap.png")
    """
    channels = {}

    # List the channels in the order of RGBA
    channel_names = ["Metallic", "AO", "Detail", "Smooth"]
    mode_map = {"L": 1, "RGB": 3, "RGBA": 4}

    # Find a reference image to determine the size
    ref_img = None
    for name in channel_names:
        path = inputs.get(name)
        if path and os.path.exists(path):
            ref_img = Image.open(path).convert("L")
            break

    if not ref_img:
        raise ValueError("No valid image provided to determine size.")

    width, height = ref_img.size

    for name in channel_names:
        path = inputs.get(name)
        if path:
            if os.path.exists(path):
                img = Image.open(path).convert("L").resize((width, height))
            else:
                print(f"Missing image for: {name}")
                img = Image.new("L", (width, height), color=0)
        else:
            print(f"No path provided for: {name}")
            img = Image.new("L", (width, height), color=0)
        channels[name] = img

    # Merge the 4 channels into an RGBA image
    mask_map = Image.merge("RGBA", (
        channels["Metallic"],  # R
        channels["AO"],        # G
        channels["Detail"],    # B
        channels["Smooth"]     # A
    ))

    # Ensure the path ends with .png
    if not output_path.lower().endswith('.png'):
        output_path += '.png'

    # Save the image
    mask_map = mask_map.convert("RGBA")
    mask_map.save(output_path)
    print("Metallic: ", channels["Metallic"].getextrema())
    print("AO: ", channels["AO"].getextrema())
    print("Detail: ", channels["Detail"].getextrema())
    print("Smooth: ", channels["Smooth"].getextrema())
    print(f"MaskMap generated → {output_path}")
    return output_path
