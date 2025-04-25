from PIL import Image
import json

def embed_metadata(image_path, metadata_path, output_path):
    print(f"Encoding TR metadata into {image_path}...")
    with open(metadata_path, 'r') as f:
        metadata = json.load(f)
    img = Image.open(image_path)
    img.save(output_path)
    print(f"✔️ Metadata attached (simulated): {metadata}")
