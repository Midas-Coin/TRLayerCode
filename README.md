# TR Code Protocol · v5.2

> **Transparent Rights Code** — an open protocol for embedding verifiable metadata into images, audio, and video imperceptibly.
![TR Code Example](examples/A_classical_oil_painting-style_meme.png)
The image above is an example of an image embedded with imperceptible metadata; which does not majorly affect the appearance of the original image, but still allows for encoded metadata to be present.

![Version](https://img.shields.io/badge/version-v5.1-blue)
![License](https://img.shields.io/badge/license-BUSL--1.1-green)

---

## 🧠 What Is TR Code?

TR Code Protocol allows creators to embed transparent, machine-verifiable metadata (e.g., creator info, licensing, payment links) directly into their digital media.

The embedding is:
- **Imperceptible to humans**
- **Detectable and extractable by machines**
- **Applicable to images, audio, and video**

---

## ✅ Current Functional Implementation

- **Image/ Audio/ Video Modulation (LSB Encoding/Decoding)**
  - Proof-of-concept using Least Significant Bit (LSB) modulation to encode metadata directly into PNG image pixels, soundwaves via .wav files, and videoframes via .mp4 files.
  - Includes both encoder and decoder modules.
  - Example metadata is stored in `tr_metadata.json`, and output is written to `extracted_metadata.json`.

---

## 🔧 Modulation Methods (Supported by Protocol)

> ⚠️ Note: This SDK uses **LSB (Least Significant Bit)** encoding as a working example.  
> The TR Layer Code protocol is not limited to LSB and can be expanded modularly.

### 🖼️ Image Domain

| Method                        | Description |
|-------------------------------|-------------|
| **LSB (Least Significant Bit)** | Pixel-level bit encoding (used in this SDK) |
| **DCT Coefficient Modulation** | Encoding in frequency domain (JPEG-like images) |
| **Color Channel Biasing**      | Slight RGB shifts to represent encoded values |
| **Pixel Cluster Modulation**   | Encoding via parity across adjacent pixel groups |

### 🔊 Audio Domain

| Method                            | Description |
|-----------------------------------|-------------|
| **Echo Hiding**                   | Delayed audio echoes encode binary patterns |
| **Phase Modulation**              | Subtle shifts in phase spectrum encode values |
| **Frequency Masking**             | High-frequency or low-volume modulation |
| **Envelope Shaping**              | Modulate amplitude envelope patterns |

### 🎥 Video Domain

| Method                            | Description |
|-----------------------------------|-------------|
| **Frame LSB Modulation**          | Apply LSB per frame across time |
| **Temporal Pixel Drift**          | Encode metadata in shifting frame sequences |
| **Invisible Flicker Encoding**    | Modulation of brightness in imperceptible bands |


##  World's first Transparent Rights (TR) Layer Code SDK.

This is a functional prototype implementation of the TR Layer Code — a protocol for embedding imperceptible, machine-readable metadata into media such as images, audio, and video. The goal is to create a universal provenance and rights-tracking layer for digital assets.

Now Supports imperceptible metadata embedding into:
- Images (pixel LSB modulation) *(Encoder/Decoder ready)*
- Audio (soundwave LSB modulation) *(Encoder/Decoder ready — user must provide audio files)*
- Video (frame LSB modulation) *(Encoder/Decoder ready — user must provide video files)*

## 📁 What’s Inside

- `protocol.md` — Full protocol specification
- `sdk-stub/` — Minimal encoder (`tr_encode.py`) and decoder (`tr_decode.py`)
- `examples/` — Doge meme examples with embedded TR Codes
- `TR_Code_Drawing_*.png` — Technical architecture diagrams
- `LICENSE.md` — Business Source License (Custom)
- `LICENSE_PURCHASE.md` — Monetization and licensing terms
- `diagrams/` — Logic Diagrams for Operation of Encoder/ Decoder
- `image/` - image module folder 
- `audio/` - audio module folder 
- `video/` - video module folder 

---

## 🗂 Modules

| Domain | Files |
|:-------|:------|
| Image  | `image/image_tr_encoder.py`, `image/image_tr_decoder.py` |
| Audio  | `audio/audio_tr_encoder.py`, `audio/audio_tr_decoder.py` |
| Video  | `video/video_tr_encoder.py`, `video/video_tr_decoder.py` |

Each domain uses:
- `tr_metadata.json` ➔ Input metadata to embed
- `extracted_metadata.json` ➔ Output decoded metadata

---

## 🖼 Examples

Located inside `/examples/`:

You can decode embedded metadata from the included images:

- `/examples/AI_Sherlock.png`
- `/examples/A_classical_oil_painting-style_meme.png`

> **Note:** Audio and video examples are not included — users can supply their own WAV/MP4 files for testing.

---

## 🚀 Usage Examples

```bash
# Image Encoding
python image/image_tr_encoder.py input_image.png output_image.png

# Audio Encoding
python audio/audio_tr_encoder.py input.wav output.wav

# Video Encoding
python video/video_tr_encoder.py input.mp4 output.mp4
```

---

## 📣 Licensing

TR Code Protocol is free for personal, academic, and non-commercial use.  
**Commercial use requires a paid license.**

See [`LICENSE_PURCHASE.md`](LICENSE_PURCHASE.md) for details.  
Contact: 📧 info@canterburytech.co.uk

We actively monitor usage for enforcement.

---

## 📖 Learn More

- [Vision](VISION.md)
- [Changelog](CHANGELOG.md)
- [Credits](CREDITS.md)

---

## 👤 Original Author

Created by **Fletcher Bayley**  
© 2025 Canterbury Technical Solutions Ltd  
Licensed under Business Source License 1.1 (Custom)


---

## ⚠️ Ethical Use Disclaimer

This protocol is provided for ethical use cases only.  
Any misuse of this technology for surveillance, privacy violation, harassment, or illegal activities is expressly prohibited and disavowed by the author.

TR Code was developed to empower digital creators — not to undermine human rights or privacy.

---

## ⚡ Version

- **Current:** TR Layer Code V5.1
- **Next:** Future updates may include streaming input support, additional robustness features.
