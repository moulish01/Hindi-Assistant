#!/bin/bash

echo "=============================="
echo " Hindi Voice Assistant Setup "
echo "=============================="

sudo apt update

sudo apt install -y \
    espeak \
    portaudio19-dev \
    libasound2-dev \
    build-essential \
    python3-dev \
    unzip \
    wget

if ! command -v python3.10 &> /dev/null
then
    echo "❌ Python 3.10 not found!"
    exit 1
fi

echo "Creating virtual environment..."

python3.10 -m venv hindi_env
source hindi_env/bin/activate

pip install --upgrade pip setuptools wheel
pip install -r requirements.txt

if [ ! -d "$HOME/vosk-model-small-hi-0.22" ]; then
    echo "Downloading Hindi model..."
    cd $HOME
    wget https://alphacephei.com/vosk/models/vosk-model-small-hi-0.22.zip
    unzip vosk-model-small-hi-0.22.zip
fi

echo "=============================="
echo " Setup Completed Successfully "
echo "=============================="

echo ""
echo "To run assistant:"
echo "cd ~/hindi_assistant"
echo "source hindi_env/bin/activate"
echo "python assistant.py"

