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
VisionVoice/
│
├── data/                          # Sample images or external input files
│   ├── sample1.jpg
│   └── ...
│
├── models/                        # Local model folders (Vosk, Gemma, etc.)
│   └── vosk-model-small-en-us-0.15/
│
├── notebooks/                     # Jupyter notebooks for step-by-step development
│   ├── 1_OCR_Text_Extraction.ipynb
│   ├── 2_Image_Captioning.ipynb
│   ├── 3_Text_Cleaning_and_Merge.ipynb
│   ├── 4_Text_to_Speech.ipynb
│   ├── 5_Check_Demo.ipynb
│   ├── 6_Offline_TTS_pyttsx3.ipynb
│   └── 7_webcam_input_and_offline_tts.ipynb
│
├── app/                           # Streamlit app scripts and resources
│   └── streamlit_app.py
│
├── outputs/                       # Generated audio, text, and PDF outputs
│   ├── image_1_description.txt
│   ├── webcam_description.txt
│   ├── visionvoice_history.txt
│   └── visionvoice_history.pdf
│
├── requirements.txt              # Python dependencies
├── README.md                     # Project overview and instructions
└── technical_writeup.md          # Architecture, features, model usage, etc.
```

## 🛠️ Run the Streamlit App

```bash
streamlit run app/streamlit_app.py
```

## ✅ Requirements

Download the tesseract and vosk models. Save this files in models folder
1. https://github.com/tesseract-ocr/tesseract
2. https://alphacephei.com/vosk/models
   
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
