#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
from PIL import Image
import pytesseract
from transformers import BlipProcessor, BlipForConditionalGeneration
import pyttsx3
import cv2
import numpy as np
import os
import time
from vosk import Model, KaldiRecognizer
import wave
import json
import tempfile

# ========== Setup ==========
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base", use_fast=False)
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# Voice recognition model (Vosk)
# ✅ Full absolute path to the model
vosk_model_path = r"C:\Users\Admin\Desktop\VisionVoice\models\vosk-model-small-en-us-0.15"

# ✅ Load the model
vosk_model = Model(vosk_model_path)   # download from: https://alphacephei.com/vosk/models

# ========== Utilities ==========
def clean_text(text):
    return ' '.join(text.replace('\n', ' ').replace('\x0c', '').strip().split())

def speak_offline(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 160)
    engine.setProperty('volume', 1.0)
    engine.say(text)
    engine.runAndWait()

def process_image(img):
    ocr_text = pytesseract.image_to_string(img)
    cleaned_ocr = clean_text(ocr_text)

    inputs = processor(img, return_tensors="pt")
    out = model.generate(**inputs)
    caption = processor.decode(out[0], skip_special_tokens=True)
    cleaned_caption = clean_text(caption)

    final_description = f"{cleaned_caption}. The text on the image reads: {cleaned_ocr}."
    return final_description, cleaned_caption, cleaned_ocr

def save_description_to_txt(text, filename="description.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)

def record_and_transcribe():
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tf:
        audio_path = tf.name

    # Record audio (5 sec)
    import sounddevice as sd
    from scipy.io.wavfile import write

    duration = 5  # seconds
    fs = 16000  # Hz
    st.info("🎙️ Listening for voice command...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    write(audio_path, fs, audio)

    # Transcribe
    wf = wave.open(audio_path, "rb")
    rec = KaldiRecognizer(vosk_model, wf.getframerate())
    rec.SetWords(True)

    result = ""
    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            res = json.loads(rec.Result())
            result += res.get("text", "")

    wf.close()
    return result.strip()

# ========== Streamlit UI ==========
st.set_page_config(page_title="VisionVoice AI", layout="centered")
st.title("🧠 VisionVoice: Offline Multimodal AI Assistant")

st.sidebar.markdown("## 🎛️ Features")
st.sidebar.markdown("✔️ Upload multiple images\n✔️ Offline TTS\n✔️ Vosk voice command\n✔️ Export text/audio")

# Session state for history
if "history" not in st.session_state:
    st.session_state.history = []

# ========== Image Upload ==========
uploaded_files = st.file_uploader("📁 Upload one or more images", accept_multiple_files=True, type=["jpg", "jpeg", "png"])

if uploaded_files and st.button("🔍 Analyze All"):
    for i, uploaded_file in enumerate(uploaded_files, 1):
        img = Image.open(uploaded_file).convert("RGB")
        st.image(img, caption=f"Image {i}", use_container_width=True)

        # Process
        final_description, caption, ocr = process_image(img)

        # Display
        st.markdown(f"**Caption {i}:** {caption}")
        st.markdown(f"**OCR Text {i}:** {ocr}")
        st.markdown(f"**Final Description {i}:** {final_description}")

        # Speak
        speak_offline(final_description)

        # Save history
        st.session_state.history.append({
            "image": uploaded_file.name,
            "caption": caption,
            "ocr": ocr,
            "description": final_description
        })

        # Save text/audio
        output_txt = f"../outputs/image_{i}_description.txt"
        save_description_to_txt(final_description, output_txt)
        st.success(f"📁 Saved description to {output_txt}")

# ========== Webcam Capture ==========
if st.button("📸 Capture from Webcam"):
    cam = cv2.VideoCapture(0)
    ret, frame = cam.read()
    cam.release()
    if ret:
        img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img_rgb)
        st.image(img, caption="Captured Image", use_container_width=True)

        final_description, caption, ocr = process_image(img)

        st.markdown(f"**Caption:** {caption}")
        st.markdown(f"**OCR Text:** {ocr}")
        st.markdown(f"**Final Description:** {final_description}")

        speak_offline(final_description)

        # Save text
        save_description_to_txt(final_description, "../outputs/webcam_description.txt")
    else:
        st.error("❌ Could not capture from webcam")

# ========== Voice Command ==========
if st.button("🎙️ Give a Voice Command"):
    transcription = record_and_transcribe()
    st.success(f"🗣️ You said: `{transcription}`")

    if "upload" in transcription:
        st.info("Try uploading an image now.")
    elif "webcam" in transcription:
        st.warning("Click the 'Capture from Webcam' button.")
    elif "history" in transcription:
        if st.session_state.history:
            st.info("🔁 Showing processing history:")
            for item in st.session_state.history:
                st.markdown(f"- **Image:** {item['image']} | **Caption:** {item['caption']}")
        else:
            st.warning("No history available.")
    else:
        st.info("Command not recognized.")


# In[ ]:




