import json
import pyaudio
import subprocess
import time
import os
from datetime import datetime

from vosk import Model, KaldiRecognizer


# ================= CONFIG =================

# CHANGE this if your username is different
MODEL_PATH = os.path.expanduser("~/vosk-model-small-hi-0.22")

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
rec = KaldiRecognizer(model, RATE)


# ================= AUDIO =================

p = pyaudio.PyAudio()

stream = p.open(
    format=pyaudio.paInt16,
    channels=1,
    rate=RATE,
    input=True,
    frames_per_buffer=BUFFER
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

    time.sleep(0.3)


# ================= START MESSAGE =================

speak("हिंदी वॉयस असिस्टेंट तैयार है। कृपया बोलिए।")

print("\n🎤 Listening... (Press Ctrl+C to stop)\n")


# ================= MAIN LOOP =================

try:

    while True:

        data = stream.read(BUFFER, exception_on_overflow=False)

        if rec.AcceptWaveform(data):

            result = json.loads(rec.Result())

            text = result.get("text", "").strip()

            if not text:
                continue

            print("🗣 You said:", text)


            # -------- COMMANDS --------

            if "समय" in text:
                now = datetime.now().strftime("%I:%M %p")
                speak("अभी समय है " + now)

            elif "नमस्ते" in text:
                speak("नमस्ते, मैं आपकी मदद कर सकता हूँ।")

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

