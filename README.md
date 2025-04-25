# TR Code Protocol · v5.0

> **Transparent Rights Code** — an open protocol for embedding verifiable metadata into images, audio, and video imperceptibly.

![Version](https://img.shields.io/badge/version-v5.0-blue)
![License](https://img.shields.io/badge/license-BUSL--1.1-green)

---

## 🧠 What Is TR Code?

TR Code Protocol allows creators to embed transparent, machine-verifiable metadata (e.g., creator info, licensing, payment links) directly into their digital media.

The embedding is:
- **Imperceptible to humans**
- **Detectable and extractable by machines**
- **Applicable to images, audio, and video**

Work in progress, we will be adding audio/ video support to the protocol soon...

---

## 📁 What’s Inside

- `protocol.md` — Full protocol specification
- `sdk-stub/` — Minimal encoder (`tr_encode.py`) and decoder (`tr_decode.py`)
- `examples/` — Doge meme examples with embedded TR Codes
- `TR_Code_Drawing_*.png` — Technical architecture diagrams
- `LICENSE.md` — Business Source License (Custom)
- `LICENSE_PURCHASE.md` — Monetization and licensing terms
- `diagrams/` — Logic Diagrams for Operation of Encoder/ Decoder

---

## 🛠 Quick Start

```bash
python sdk-stub/tr_encode.py input.png encoder_data.json output.png
python sdk-stub/tr_decode.py output.png
```

Extracted metadata will be saved to `extracted_metadata.json`.

---

## 🖼 Examples

You can decode embedded metadata from the included images:

- `/examples/AI_Sherlock.png`
- `/examples/A_classical_oil_painting-style_meme.png

---

## 📣 Licensing

TR Code Protocol is free for personal, academic, and non-commercial use.  
**Commercial use requires a paid license.**

See [`LICENSE_PURCHASE.md`](LICENSE_PURCHASE.md) for details.  
Contact: 📧 info@canterburytech.co.uk
         📧 admin@canterburytech.co.uk

We actively monitor usage for enforcement.

---

## 📖 Learn More

- [Vision](VISION.md)
- [Changelog](CHANGELOG.md)
- [Credits](CREDITS.md)

---

## 👤 Author

Created by **Fletcher Bayley**  
© 2025 Canterbury Technical Solutions Ltd  
Licensed under Business Source License 1.1 (Custom)


---

## ⚠️ Ethical Use Disclaimer

This protocol is provided for ethical use cases only.  
Any misuse of this technology for surveillance, privacy violation, harassment, or illegal activities is expressly prohibited and disavowed by the author.

TR Code was developed to empower digital creators — not to undermine human rights or privacy.

