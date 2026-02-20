import json
import pyaudio
import subprocess
import time
import os
import numpy as np
import socket
import re
from datetime import datetime
from scipy.signal import resample
from vosk import Model, KaldiRecognizer


# ================= CONFIG =================

# CHANGE this if your username is different
MODEL_PATH = "vosk-model-small-hi-0.22"

RATE = 16000
BUFFER = 2048

# eSpeak settings (slow + loud)
ESPEAK_CMD = [
    "espeak",
    "-v", "hi",
    "-s", "110",   # Speed (lower = slower)
    "-a", "180"    # Volume (0–200)
]


# ================= CHECK MODEL =================

if not os.path.exists(MODEL_PATH):
    print("❌ Vosk model not found at:", MODEL_PATH)
    print("Download it using:")
    print("wget https://alphacephei.com/vosk/models/vosk-model-small-hi-0.22.zip")
    print("unzip vosk-model-small-hi-0.22.zip")
    exit(1)


# ================= LOAD MODEL =================

print("🔄 Loading Hindi ASR model...")

model = Model(MODEL_PATH)
rec = KaldiRecognizer(model,16000)


# ================= AUDIO =================

p = pyaudio.PyAudio()

stream = p.open(
    format=pyaudio.paInt16,
    channels=1,
    rate=RATE,
    input=True,
    frames_per_buffer=512
)

stream.start_stream()


# ================= SPEAK =================

def speak(text):
    """Speak Hindi text using eSpeak"""

    print("🤖 Assistant:", text)

    try:
        subprocess.run(ESPEAK_CMD + [text])
    except Exception as e:
        print("TTS Error:", e)

    #time.sleep(0.3)


# ================= START MESSAGE =================

speak("हिंदी वॉयस असिस्टेंट तैयार है। कृपया बोलिए।")

print("\n🎤 Listening... (Press Ctrl+C to stop)\n")


# ================= MAIN LOOP =================

try:

    while True:

        data = stream.read(BUFFER, exception_on_overflow=False)

        # ---- Energy Detection ----
        
        audio_data = np.frombuffer(data, dtype=np.int16).astype(np.float32)
        energy = np.sqrt(np.mean(audio_data * audio_data))

        if energy < 200:
            continue

        print("Energy:", energy)

        # ---- Resample 48000 → 16000 ----
        
        audio_int16 = np.frombuffer(data, dtype=np.int16)
        resampled = audio_int16[::3]   # Faster + lighter than scipy
        resampled = resampled.astype(np.int16)

        # ---- Send to Vosk ----
        
        if rec.AcceptWaveform(audio_int16.tobytes()):

            result = json.loads(rec.Result())
            text = result.get("text", "").strip()

            if not text or len(text) < 2:
                continue

            print("🗣 You said:", text)

            # -------- COMMANDS --------

            if "समय" in text:
                now = datetime.now().strftime("%I:%M %p")
                speak("अभी समय है " + now)
                
            # Date
            elif "तारीख" in text or "तारिक" in text:
                today = datetime.now().strftime("%d %B %Y")
                speak("आज की तारीख है " + today)

            # Day
            elif "day" in text:
                day = datetime.now().strftime("%A")
                speak("आज " + day + " है")

            elif "नमस्ते" in text or "नमस्कार" in text:
                speak("नमस्ते, मैं आपकी मदद कर सकता हूँ।")
                
            
            # CPU Temperature (Raspberry Pi)
            elif "तापमान" in text:
                try:
                    temp = subprocess.check_output(
                        ["vcgencmd", "measure_temp"]
                    ).decode()
                    temp = temp.replace("temp=", "")
                    speak("सी पी यू तापमान " + temp)
                except:
                    speak("तापमान उपलब्ध नहीं है")

            # System Uptime
            elif "अपटाइम" in text:
                try:
                    uptime = subprocess.check_output(
                        ["uptime", "-p"]
                    ).decode().strip()
                    speak(uptime)
                except:
                    speak("अपटाइम जानकारी उपलब्ध नहीं है")

            # Disk Usage
            elif "डिस्क" in text:
                try:
                    disk = subprocess.check_output(
                        ["df", "-h", "/"]
                    ).decode().split("\n")[1]
                    speak("डिस्क उपयोग इस प्रकार है")
                    speak(disk)
                except:
                    speak("डिस्क जानकारी उपलब्ध नहीं है")

            # IP Address
            elif "आईपी" in text:
                try:
                    ip = socket.gethostbyname(socket.gethostname())
                    speak("आपका आईपी पता " + ip)
                except:
                    speak("आईपी जानकारी उपलब्ध नहीं है")


            elif "बंद" in text or "रुको" in text or "exit" in text:
                speak("धन्यवाद। कार्यक्रम बंद किया जा रहा है।")
                break

            else:
                speak("माफ कीजिए, मैं समझ नहीं पाया।")


except KeyboardInterrupt:

    print("\n🛑 Stopped by user")
    speak("कार्यक्रम बंद किया गया।")


finally:

    stream.stop_stream()
    stream.close()
    p.terminate()

    print("✅ Program closed")
