from PIL import Image
import numpy as np
import json
import sys

def extract_metadata(image_path, output_json_path="extracted_metadata.json"):
    img = Image.open(image_path).convert("RGB")
    data = np.array(img).flatten()
    bits = [str(pixel & 1) for pixel in data[:4096]]
    chars = []
    for i in range(0, len(bits), 8):
        byte = bits[i:i+8]
        if len(byte) < 8:
            break
        char = chr(int(''.join(byte), 2))
        if char == '\x00':
            break
        chars.append(char)
    metadata_str = ''.join(chars)
    try:
        metadata = json.loads(metadata_str)
    except json.JSONDecodeError:
        metadata = {"raw": metadata_str}
    with open(output_json_path, "w") as f:
        json.dump(metadata, f, indent=2)
    print(f"✔️ Metadata extracted to {output_json_path}")

if __name__ == "__main__":
    extract_metadata(sys.argv[1])
