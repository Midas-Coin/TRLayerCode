
import cv2
import json
import numpy as np

def encode_video(input_video, output_video, metadata_file):
    with open(metadata_file, 'r') as f:
        metadata = json.dumps(json.load(f))
    metadata_bits = ''.join(f"{ord(c):08b}" for c in metadata) + '00000000'

    cap = cv2.VideoCapture(input_video)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_video, fourcc, cap.get(cv2.CAP_PROP_FPS),
                          (int(cap.get(3)), int(cap.get(4))))

    bit_idx = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame_flat = frame.flatten()
        for i in range(len(frame_flat)):
            if bit_idx < len(metadata_bits):
                frame_flat[i] = (frame_flat[i] & 0xFE) | int(metadata_bits[bit_idx])
                bit_idx += 1
            else:
                break
        frame = frame_flat.reshape(frame.shape)
        out.write(frame.astype(np.uint8))

    cap.release()
    out.release()
    print(f"Metadata embedded into {output_video} successfully.")
