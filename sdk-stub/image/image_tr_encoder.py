from PIL import Image
import numpy as np
import json
import sys

def embed_metadata(input_image_path, metadata_path, output_image_path):
    with open(metadata_path, 'r') as f:
        metadata = json.load(f)
    metadata_str = json.dumps(metadata)
    img = Image.open(input_image_path).convert("RGB")
    data = np.array(img).flatten()
    bits = ''.join(f"{ord(c):08b}" for c in metadata_str) + '00000000'
    if len(bits) > len(data):
        raise ValueError("Image not large enough to hold metadata")
    for i in range(len(bits)):
        data[i] = (data[i] & ~1) | int(bits[i])
    encoded = data.reshape(img.size[1], img.size[0], 3)
    Image.fromarray(encoded.astype(np.uint8)).save(output_image_path)
    print(f"✔️ Metadata from {metadata_path} embedded into {output_image_path}")

if __name__ == "__main__":
    embed_metadata(sys.argv[1], sys.argv[2], sys.argv[3])
