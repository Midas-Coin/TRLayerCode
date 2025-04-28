
import wave
import json

def decode_audio(encoded_wav, output_metadata_file):
    audio = wave.open(encoded_wav, 'rb')
    frames = bytearray(audio.readframes(audio.getnframes()))
    audio.close()

    bits = [str(frames[i] & 1) for i in range(len(frames))]
    chars = []
    for b in range(0, len(bits), 8):
        byte = ''.join(bits[b:b+8])
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
