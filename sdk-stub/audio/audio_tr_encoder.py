
import wave
import json

def encode_audio(input_wav, output_wav, metadata_file):
    with open(metadata_file, 'r') as f:
        metadata = json.dumps(json.load(f))
    metadata_bits = ''.join(f"{ord(c):08b}" for c in metadata) + '00000000'  # Add end marker
    
    audio = wave.open(input_wav, 'rb')
    params = audio.getparams()
    frames = bytearray(audio.readframes(audio.getnframes()))
    audio.close()

    if len(metadata_bits) > len(frames):
        raise ValueError("Audio file too small to hide all metadata.")

    for i, bit in enumerate(metadata_bits):
        frames[i] = (frames[i] & 0xFE) | int(bit)  # LSB replace

    output = wave.open(output_wav, 'wb')
    output.setparams(params)
    output.writeframes(frames)
    output.close()
    print(f"Metadata embedded into {output_wav} successfully.")
