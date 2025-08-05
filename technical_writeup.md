# 🧠 VisionVoice: Technical Writeup

## 🛠️ Problem Statement
Visually impaired users struggle with understanding printed text or images in real-world environments, especially where internet connectivity is poor or unavailable.

## 🚀 Solution Overview
VisionVoice is a multimodal, offline-capable AI assistant that captures images, generates captions, extracts OCR text, reads the information aloud, and responds to voice commands.

## 🧰 Technologies Used
- **BLIP**: Salesforce's BLIP model (`blip-image-captioning-base`) is used to caption images.
- **PyTesseract**: Open-source OCR engine for printed text extraction.
- **Pyttsx3**: Python-based offline text-to-speech system.
- **Vosk**: Lightweight speech recognition model (vosk-model-small-en-us-0.15) for offline commands.
- **Streamlit**: Interactive and fast UI for users.
- **OpenCV**: Real-time webcam image capture and conversion.

## 📦 Model Architecture

1. **Input Layer**:
   - User uploads image or captures via webcam.
2. **Processing Layer**:
   - Image processed by BLIP for captions.
   - OCR processed by Tesseract.
   - Text cleaned and merged.
3. **Output Layer**:
   - Text spoken via `pyttsx3`.
   - Text/PDF saved locally.
4. **Voice Input**:
   - Vosk recognizes spoken commands (e.g., upload, history).
   - Streamlit handles logic for corresponding actions.

## 🧪 Testing
- Tested on various image sizes and font types.
- Works without internet.
- Voice commands validated on noisy and quiet backgrounds.

## 🌐 Offline Efficiency
No APIs used. All models and libraries are local. Designed for full offline functionality even in remote areas.

## 🔐 Privacy
No user data is uploaded. All processing and storage happens locally on-device.

## 📁 Project Structure

Refer to the `README.md` for detailed file/folder breakdown.

## 🧠 Final Thoughts
VisionVoice shows the power of small, efficient, multimodal AI in real-world applications for accessibility. It combines privacy, speed, and usability — made possible through Gemma 3n's offline design philosophy.