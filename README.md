
#  Offline Hindi Voice Assistant

### 🗣️ Raspberry Pi 4 Model B | Fully Offline | Privacy-Preserving

---

## 📌 Project Overview

This project implements a **fully offline Hindi Voice Assistant** deployed on a Raspberry Pi platform. The system performs real-time speech recognition, command processing, and text-to-speech synthesis without using any cloud services.

The objective is to design a **low-latency, privacy-preserving embedded speech pipeline** suitable for edge deployment in low-resource environments.

---

## 👥 Team

* **Moulishwaran V** – Audio Pipeline Design, Testing & Validation
* **Raghul S** – System Architecture & Embedded Integration
* **Sathya Jeeva M** – Model Deployment & Optimization

---

## 🎯 Problem Statement

### Offline, Privacy-Preserving Hindi Voice Assistant on Raspberry Pi

### Objective

Develop a low-latency, privacy-preserving voice assistant on an Arm-based SBC (e.g., Raspberry Pi) that processes Hindi voice commands entirely offline. The assistant handles local queries (time, weather, greetings, etc.) using on-device ASR and TTS.

---

## 📝 Project Description

This project builds an embedded speech pipeline performing:

* 🎙️ Speech-to-text using a lightweight Hindi ASR model (Vosk)
* 🧠 Command parsing and intent recognition in Python
* 🔊 Text-to-speech responses using local TTS (eSpeak-NG)
* 💻 End-to-end execution on Raspberry Pi CPU (No Cloud Dependency)

---

## 🔑 Key Requirements

### 🔹 Hardware

* Raspberry Pi 4 (or Raspberry Pi 5)
* USB Microphone
* Speaker (3.5 mm jack or HDMI)
* CPU-based execution (no accelerators required)

### 🔹 Software

* Python 3.9
* PyAudio (Audio I/O)
* Vosk (Offline Hindi Speech Recognition)
* eSpeak-NG (Hindi Text-to-Speech)
* ALSA / PulseAudio (Audio Interface)

---

## 🎯 Performance Targets

* ⏱️ Sub-2-second response time per command
* 🎯 Accurate recognition for 10–15 Hindi commands
* 🔒 Fully offline and robust operation

---

## 🏗️ System Architecture

### 🔹 Hardware

* Raspberry Pi 4
* USB Microphone
* Speaker

### 🔹 Software Stack

* Python 3.9
* Vosk Hindi Model (`vosk-model-small-hi-0.22`)
* eSpeak-NG
* ALSA / PulseAudio

---

## ⚙️ Working Principle

1. Audio is captured through the microphone at **16 kHz sampling rate**.
2. Speech is converted to text using the **Vosk Hindi ASR model**.
3. Commands are processed locally using rule-based intent parsing.
4. The system generates an appropriate response.
5. eSpeak synthesizes and outputs the response through the speaker.

✅ All processing is executed locally on the Raspberry Pi without any internet connectivity.

---

## 🚀 Features

* ✔ Fully offline operation
* ✔ Real-time Hindi speech recognition
* ✔ Low-latency response
* ✔ Lightweight & ARM optimized
* ✔ Privacy-preserving design
* ✔ No external API dependency

---

## 📊 Performance Metrics

| Parameter             | Value          |
| --------------------- | -------------- |
| Average Response Time | ~1–1.5 seconds |
| CPU Usage             | ~45–60%        |
| Memory Usage          | ~300–400 MB    |
| Sampling Rate         | 16 kHz         |

> Performance may vary depending on model size and hardware configuration.

---

## 📂 Project Structure

```
offline-hindi-assistant/
│
├── assistant.py
├── readme.txt
├── requirements.txt
└── setup.sh
```

---

## 🔧 Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/Deepa-0408/hindi_voice_assistant.git
cd offline-hindi-assistant
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Download Hindi Vosk Model

Download the Hindi model from the official Vosk website:

🔗 [https://alphacephei.com/vosk/models/vosk-model-small-hi-0.22.zip](https://alphacephei.com/vosk/models/vosk-model-small-hi-0.22.zip)

Unzip and place the folder inside your project directory.

### 4️⃣ Run the Application

```bash
python assistant.py
```

---

## 🧠 Applications

* 🌾 Rural and low-connectivity environments
* 🔐 Privacy-sensitive institutional setups
* 🏠 Smart home embedded systems
* 👵 Assistive technology for elderly users
* 🎓 Educational voice-based interfaces

---

## 🔮 Future Enhancements

* Model quantization for reduced memory footprint
* FPGA-based speech acceleration
* Wake-word detection integration
* Multilingual support (Hindi + English)
* Edge AI co-processor integration

---

## 📈 Technical Significance

This project demonstrates:

* Real-time embedded AI implementation
* Edge deployment of speech models
* Resource-constrained system optimization
* Practical application of signal processing and embedded programming

It bridges the gap between AI algorithms and hardware-aware deployment, making it suitable for both academic research and industrial applications in regional language AI systems.

---

If you want, I can also:

* ✨ Add badges (Python version, Raspberry Pi, License, etc.)
* ✨ Add architecture diagram (ASCII or image)
* ✨ Format it for IEEE project submission
* ✨ Make it more industry-ready for GitHub portfolio 🚀
