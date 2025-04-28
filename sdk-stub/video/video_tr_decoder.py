
import cv2
import json
import numpy as np

def decode_video(encoded_video, output_metadata_file):
    cap = cv2.VideoCapture(encoded_video)
    bits = []

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frame_flat = frame.flatten()
        bits.extend([(pixel & 1) for pixel in frame_flat])

    cap.release()

    chars = []
    for b in range(0, len(bits), 8):
        byte = ''.join(str(bit) for bit in bits[b:b+8])
        if byte == '00000000':
            break
        chars.append(chr(int(byte, 2)))
    metadata_str = ''.join(chars)
    
    try:
        metadata = json.loads(metadata_str)
    except json.JSONDecodeError:
        metadata = {"error": "Failed to decode metadata properly."}

    with open(output_metadata_file, 'w') as f:
        json.dump(metadata, f, indent=4)
    print(f"Extracted metadata written to {output_metadata_file}.")
