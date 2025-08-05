# 🧠 VisionVoice: Offline Multimodal AI Assistant

VisionVoice is a privacy-first, offline-capable AI assistant that helps visually impaired users understand images and printed text through OCR, image captioning, and voice commands — all without an internet connection.

## 🔍 Features
- 📸 Image captioning using BLIP
- 🔠 OCR using Tesseract
- 🧠 Offline TTS with `pyttsx3`
- 🎙️ Vosk-based voice command recognition
- 📁 Upload multiple images
- 📷 Capture from webcam
- 📄 Export to TXT and PDF
- 🔁 History tracking and clearing
- 🧑‍💻 Fully offline & privacy-first

## 🧰 Tech Stack
- Python, Streamlit
- BLIP for image captioning
- PyTesseract for OCR
- Pyttsx3 for offline speech
- Vosk for offline voice command
- OpenCV for webcam integration
- FPDF for PDF reports

## 📁 Folder Structure
```
notebooks/, app/, models/, data/, outputs/
```

## 🛠️ Run the Streamlit App

```bash
streamlit run app/streamlit_app.py
```

## ✅ Requirements

Install all required dependencies:

```bash
pip install -r requirements.txt
```

## 📄 Example Commands

- "upload" — prompts user to upload image
- "webcam" — triggers webcam capture
- "history" — shows past processed items
- "clear history" — deletes history
- "export" — saves TXT + PDF
- "exit" — closes app

## 💡 Use Case
Built for Google - Gemma 3n Impact Challenge to improve accessibility and independence for visually impaired users through fully offline, real-time image understanding.